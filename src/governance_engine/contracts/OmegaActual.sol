// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;

/**
 * @title OmegaActualTreatyEngine
 * @notice Implements the planetary dead-man's switch and compute compliance ledger.
 * @dev All external calls are restricted to sovereign or authorized institutions.
 */
contract OmegaActual {
    address public sovereign;
    uint256 public constant COMPUTE_LIMIT_FLOP = 1e26;
    uint256 public lastHeartbeat;
    bool public isFailSafeTriggered;

    mapping(address => bool) public authorizedInstitutions;

    event HeartbeatReceived(uint256 timestamp);
    event FailSafeTriggered(string reason);
    event ComputeComplianceLogged(address indexed institution, uint256 flops);
    event InstitutionAuthorized(address indexed institution);

    modifier onlySovereign() {
        require(msg.sender == sovereign, "Unauthorized: Not Sovereign Authority");
        _;
    }

    modifier onlyAuthorized() {
        require(authorizedInstitutions[msg.sender] || msg.sender == sovereign, "Unauthorized: Not an Authorized Institution");
        _;
    }

    constructor() {
        sovereign = msg.sender;
        lastHeartbeat = block.timestamp;
        authorizedInstitutions[msg.sender] = true;
    }

    /**
     * @notice Authorizes a new institution to log compute usage.
     * @param institution The address of the institution to authorize.
     */
    function authorizeInstitution(address institution) external onlySovereign {
        authorizedInstitutions[institution] = true;
        emit InstitutionAuthorized(institution);
    }

    /**
     * @notice Records periodic heartbeats from the GIEN gossip mesh.
     */
    function postHeartbeat() external onlySovereign {
        lastHeartbeat = block.timestamp;
        emit HeartbeatReceived(block.timestamp);
    }

    /**
     * @notice Logs compute usage for institutional attestation.
     * @param flops The number of floating point operations used.
     */
    function logComputeUsage(uint256 flops) external onlyAuthorized {
        if (flops > COMPUTE_LIMIT_FLOP) {
            _triggerFailSafe("Planetary FLOP Limit Exceeded");
        }
        emit ComputeComplianceLogged(msg.sender, flops);
    }

    function _triggerFailSafe(string memory reason) internal {
        isFailSafeTriggered = true;
        emit FailSafeTriggered(reason);
    }

    /**
     * @notice Checks the current status of the dead-man's switch.
     * @return bool True if nominal, False if triggered.
     */
    function checkStatus() external view returns (bool) {
        // If no heartbeat for > 24 hours, trigger fail-safe
        if (block.timestamp > lastHeartbeat + 1 days) {
            return false; // Dead-man's switch triggered
        }
        return !isFailSafeTriggered;
    }
}
