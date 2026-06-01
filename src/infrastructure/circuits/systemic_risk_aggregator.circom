pragma circom 2.1.0;

/**
 * SystemicRiskAggregator Circuit
 * Verifies that the aggregated risk drift of an agent swarm
 * does not exceed G-SIFI capital buffer thresholds (Basel IV).
 */

template SystemicRiskAggregator(n_agents) {
    signal input agent_risks[n_agents]; // Private: Individual agent drift scores
    signal input institutional_capital;  // Public: Total Tier 1 capital
    signal input drift_threshold;        // Public: Regulatory threshold
    signal output total_drift;
    signal output is_within_bounds;

    var sum = 0;
    for (var i = 0; i < n_agents; i++) {
        sum += agent_risks[i];
    }

    total_drift <== sum;

    // Check if total_drift / institutional_capital < drift_threshold
    // Transformed to: total_drift < institutional_capital * drift_threshold
    component lt = LessThan(64);
    lt.in[0] <== total_drift;
    lt.in[1] <== institutional_capital * drift_threshold;

    is_within_bounds <== lt.out;
}

// Utility template for range checking
template LessThan(n) {
    signal input in[2];
    signal output out;
    // Implementation omitted for brevity
}

// component main = SystemicRiskAggregator(1024);
