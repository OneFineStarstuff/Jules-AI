// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;

/**
 * @title OmniSentinelGovernance
 * @notice Immutable ledger for G-SRI index tracking and BBOM assurance.
 * @dev Uses authorized reporters to maintain the integrity of systemic risk indexing.
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

    /**
     * @notice Authorizes a reporter to log systemic risk scores.
     * @param reporter The address of the reporter.
     */
    function authorizeReporter(address reporter) external onlyAdmin {
        authorizedReporters[reporter] = true;
    }

    /**
     * @notice Logs the Global Systemic Risk Index (G-SRI) to the chain.
     * @param score The systemic risk score (scaled).
     * @param metadataHash The IPFS hash of the full audit trace.
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

    /**
     * @notice Returns the latest G-SRI score.
     * @return uint256 The latest score.
     */
    function getLatestScore() external view returns (uint256) {
        if (riskHistory.length == 0) return 0;
        return riskHistory[riskHistory.length - 1].gsriScore;
    }
}
