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
    event FailSafeReset(address indexed by);
    event ApexArchitectTransferred(address indexed previousArchitect, address indexed newArchitect);

    modifier onlyApex() {
        require(msg.sender == apexArchitect, "Unauthorized: Requires Apex Architect authority");
        _;
    }

    constructor() {
        apexArchitect = msg.sender;
        failSafeTriggered = false;
        emit ApexArchitectTransferred(address(0), msg.sender);
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
        emit FailSafeReset(msg.sender);
    }

    /**
     * @dev Transfers Apex authority to a new address.
     */
    function transferApexAuthority(address newArchitect) external onlyApex {
        require(newArchitect != address(0), "New architect is the zero address");
        emit ApexArchitectTransferred(apexArchitect, newArchitect);
        apexArchitect = newArchitect;
    }
}
