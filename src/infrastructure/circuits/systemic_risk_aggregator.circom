pragma circom 2.0.0;

template SystemicRiskAggregator(n) {
    signal input riskScores[n];
    signal input threshold;
    signal output totalRisk;
    signal output isAboveThreshold;

    var sum = 0;
    for (var i = 0; i < n; i++) {
        sum += riskScores[i];
    }

    totalRisk <== sum;

    // Simplified comparison logic for ZK proof of threshold compliance
    // In a real circuit, this would use a less-than template from circom-lib
    isAboveThreshold <== totalRisk - threshold;
}

component main = SystemicRiskAggregator(10);
