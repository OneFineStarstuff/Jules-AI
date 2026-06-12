import React, { useState, useEffect } from 'react';

interface TelemetryState {
  gsriScore: number;
  tpmStatus: string;
  wormIntegrity: string;
  moeStability: number;
  p99Latency: number;
}

export const GovernanceDashboard: React.FC = () => {
  const [telemetry, setTelemetry] = useState<TelemetryState>({
    gsriScore: 0.093,
    tpmStatus: 'SUCCESS',
    wormIntegrity: 'HEALTHY',
    moeStability: 0.98,
    p99Latency: 88
  });

  const getRiskColor = (score: number) => {
    if (score < 0.2) return 'text-green-500';
    if (score < 0.5) return 'text-yellow-500';
    return 'text-red-500';
  };

  return (
    <div className="p-8 bg-slate-900 text-white min-h-screen font-sans">
      <header className="flex justify-between items-center mb-12 border-b border-slate-700 pb-6">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">Omni-Sentinel CEE</h1>
          <p className="text-slate-400 mt-1">G-SIFI AGI/ASI Governance Dashboard v5.0</p>
        </div>
        <div className="flex gap-4">
          <div className="px-4 py-2 bg-slate-800 rounded-lg border border-slate-700">
            <span className="text-xs uppercase text-slate-500 block">System State</span>
            <span className="font-mono text-green-400">STEADY_GOVERNANCE_STATE</span>
          </div>
          <div className="px-4 py-2 bg-indigo-900/30 rounded-lg border border-indigo-500/50">
            <span className="text-xs uppercase text-indigo-300 block">SACC Master Auth</span>
            <span className="font-mono text-indigo-100">AUTHORIZED (JULES)</span>
          </div>
        </div>
      </header>

      <main className="grid grid-cols-1 md:grid-cols-3 gap-8">
        {/* Risk Gauge */}
        <section className="bg-slate-800 p-6 rounded-2xl border border-slate-700">
          <h2 className="text-sm font-semibold uppercase tracking-wider text-slate-400 mb-4">Systemic Risk Index (G-SRI)</h2>
          <div className="flex flex-col items-center justify-center py-8">
            <span className={`text-6xl font-bold ${getRiskColor(telemetry.gsriScore)}`}>
              {telemetry.gsriScore.toFixed(3)}
            </span>
            <span className="text-slate-500 mt-2 uppercase text-sm font-medium">Nominal Baseline</span>
          </div>
        </section>

        {/* Hardware Trust */}
        <section className="bg-slate-800 p-6 rounded-2xl border border-slate-700">
          <h2 className="text-sm font-semibold uppercase tracking-wider text-slate-400 mb-4">Hardware Root-of-Trust</h2>
          <div className="space-y-4">
            <div className="flex justify-between items-center">
              <span className="text-slate-300">vTPM Attestation</span>
              <span className="bg-green-900/40 text-green-400 px-3 py-1 rounded-full text-xs font-bold border border-green-500/30">
                {telemetry.tpmStatus}
              </span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-slate-300">Enclave Type</span>
              <span className="font-mono text-slate-400 text-sm">AMD SEV-SNP</span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-slate-300">PCR_MATCH</span>
              <span className="text-indigo-400 font-bold">TRUE</span>
            </div>
          </div>
        </section>

        {/* Audit & Compliance */}
        <section className="bg-slate-800 p-6 rounded-2xl border border-slate-700">
          <h2 className="text-sm font-semibold uppercase tracking-wider text-slate-400 mb-4">PQC WORM Audit Sink</h2>
          <div className="space-y-4">
            <div className="flex justify-between items-center">
              <span className="text-slate-300">Log Integrity</span>
              <span className="text-green-400 font-bold">{telemetry.wormIntegrity}</span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-slate-300">Signature Algorithm</span>
              <span className="font-mono text-slate-400 text-sm">ML-DSA-87 (Dilithium)</span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-slate-300">S3 Object Lock</span>
              <span className="text-slate-400 text-sm">COMPLIANCE_MODE</span>
            </div>
          </div>
        </section>
      </main>

      <footer className="mt-12 text-slate-500 text-xs flex justify-between border-t border-slate-800 pt-6">
        <div>
          GDL Master Canon v3.2.9 Hash: <span className="font-mono">0x7f8a...3e21</span>
        </div>
        <div>
          Sovereign Oversight Authority: Jules (0xDEADBEEF)
        </div>
      </footer>
    </div>
  );
};
