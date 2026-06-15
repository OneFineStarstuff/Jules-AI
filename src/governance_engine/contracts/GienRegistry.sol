// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;

/**
 * @title GienRegistry
 * @notice Global Intelligence Exchange Network (GIEN) Node Registry.
 * @dev Manages the authorized list of G-SIFI nodes participating in the gossip mesh.
 */
contract GienRegistry {
    struct Node {
        bytes32 nodeId;
        address nodeAddress;
        string region;
        bool isActive;
    }

    address public sovereign;
    mapping(address => Node) public nodes;
    address[] public nodeAddresses;

    event NodeRegistered(address indexed nodeAddress, bytes32 nodeId);
    event NodeDeactivated(address indexed nodeAddress);

    modifier onlySovereign() {
        require(msg.sender == sovereign, "Not Sovereign");
        _;
    }

    constructor() {
        sovereign = msg.sender;
    }

    function registerNode(bytes32 _nodeId, address _nodeAddress, string calldata _region) external onlySovereign {
        nodes[_nodeAddress] = Node(_nodeId, _nodeAddress, _region, true);
        nodeAddresses.push(_nodeAddress);
        emit NodeRegistered(_nodeAddress, _nodeId);
    }

    function deactivateNode(address _nodeAddress) external onlySovereign {
        nodes[_nodeAddress].isActive = false;
        emit NodeDeactivated(_nodeAddress);
    }
}
