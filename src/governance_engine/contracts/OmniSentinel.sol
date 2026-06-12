// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title OmniSentinelGovernance
 * @dev Immutable ledger for G-SRI index tracking and BBOM assurance.
 */
contract OmniSentinel {
    struct RiskReport {
        uint256 gsriScore;
        uint256 timestamp;
        string metadataHash; // IPFS hash of the full audit trace
        address reporter;
    }

    address public admin;
    mapping(address => bool) public authorizedReporters;
    RiskReport[] public riskHistory;

    event RiskLogged(uint256 score, string metadataHash);

    constructor() {
        admin = msg.sender;
    }

    modifier onlyAdmin() {
        require(msg.sender == admin, "Not Admin");
        _;
    }

    function authorizeReporter(address reporter) external onlyAdmin {
        authorizedReporters[reporter] = true;
    }

    /**
     * @dev Logs the Global Systemic Risk Index (G-SRI) to the chain.
     */
    function logGSRI(uint256 score, string calldata metadataHash) external {
        require(authorizedReporters[msg.sender], "Unauthorized Reporter");

        RiskReport memory report = RiskReport({
            gsriScore: score,
            timestamp: block.timestamp,
            metadataHash: metadataHash,
            reporter: msg.sender
        });

        riskHistory.push(report);
        emit RiskLogged(score, metadataHash);
    }

    function getLatestScore() external view returns (uint256) {
        if (riskHistory.length == 0) return 0;
        return riskHistory[riskHistory.length - 1].gsriScore;
    }
}
