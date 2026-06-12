// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title OmegaActual Treaty Engine
 * @dev Implements civilizational FLOP limits and planetary dead-man's switch.
 */
contract OmegaActual {
    uint256 public constant GLOBAL_FLOP_LIMIT = 10**26;
    uint256 public totalAllocatedFlops;
    address public apexArchitect;
    bool public failSafeTriggered;

    event ComputeAllocated(address indexed institution, uint256 flops);
    event FailSafeTriggered(string reason);

    modifier onlyApex() {
        require(msg.sender == apexArchitect, "Unauthorized: Requires Apex Architect authority");
        _;
    }

    constructor() {
        apexArchitect = msg.sender;
        failSafeTriggered = false;
    }

    /**
     * @dev Allocates FLOP quotas to G-SIFI institutions.
     * Enforces the civilizational redline.
     */
    function allocateCompute(uint256 flops) external onlyApex {
        require(!failSafeTriggered, "Fail-safe active: All compute allocations suspended");

        if (totalAllocatedFlops + flops > GLOBAL_FLOP_LIMIT) {
            failSafeTriggered = true;
            emit FailSafeTriggered("CIVILIZATIONAL_FLOP_LIMIT_EXCEEDED");
            return;
        }

        totalAllocatedFlops += flops;
        emit ComputeAllocated(msg.sender, flops);
    }

    /**
     * @dev Resets the fail-safe. Requires supranational consensus (simulated by Apex authority).
     */
    function resetFailSafe() external onlyApex {
        failSafeTriggered = false;
    }
}
