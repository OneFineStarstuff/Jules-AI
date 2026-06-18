import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { Shield, AlertTriangle, Activity, Lock, Zap } from 'lucide-react';

/**
 * Omni-Sentinel Governance Cockpit Components (Phase I Implementation)
 * Standardizing on Deep Onyx / Governance Blue palette.
 */

// G-SRI Drift Simulator Component
export const GSRIDriftSimulator: React.FC<{ currentScore: number }> = ({ currentScore }) => {
  const [data, setData] = useState([{ time: 0, score: currentScore }]);

  useEffect(() => {
    const interval = setInterval(() => {
      setData(prev => {
        const last = prev[prev.length - 1];
        const nextScore = Math.max(0, Math.min(100, last.score + (Math.random() - 0.5) * 2));
        return [...prev.slice(-20), { time: last.time + 1, score: nextScore }];
      });
    }, 2000);
    return () => clearInterval(interval);
  }, [currentScore]);

  return (
    <div className="bg-slate-900 p-6 rounded-lg border border-blue-900">
      <h3 className="text-blue-400 font-bold flex items-center gap-2 mb-4">
        <Activity size={20} /> G-SRI Drift Simulator (Bayesian)
      </h3>
      <div className="h-64">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
            <XAxis dataKey="time" hide />
            <YAxis domain={[0, 100]} stroke="#64748b" />
            <Tooltip contentStyle={{ backgroundColor: '#0f172a', border: '1px solid #1e3a8a' }} />
            <Line type="monotone" dataKey="score" stroke="#3b82f6" strokeWidth={2} dot={false} />
          </LineChart>
        </ResponsiveContainer>
      </div>
      <div className="mt-4 text-sm text-slate-400">
        Status: <span className={currentScore < 85 ? "text-green-500" : "text-red-500"}>
          {currentScore < 85 ? "STABLE" : "CRITICAL_INTERVENTION_REQUIRED"}
        </span>
      </div>
    </div>
  );
};

// PQC WORM Health Dashboard
export const PQCStatusCard: React.FC = () => (
  <div className="bg-slate-900 p-6 rounded-lg border border-blue-900">
    <h3 className="text-blue-400 font-bold flex items-center gap-2 mb-4">
      <Lock size={20} /> PQC WORM Integrity (ML-DSA-87)
    </h3>
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <span className="text-slate-400">Signature Algorithm</span>
        <span className="text-blue-300 font-mono">ML-DSA-87</span>
      </div>
      <div className="flex justify-between items-center">
        <span className="text-slate-400">S3 Object Lock</span>
        <span className="text-green-500 flex items-center gap-1"><Shield size={14}/> Active</span>
      </div>
      <div className="flex justify-between items-center">
        <span className="text-slate-400">WORM Persistence</span>
        <span className="text-blue-300">AWS-S3-COMPLIANCE</span>
      </div>
    </div>
  </div>
);

// Main Governance Cockpit Layout
export const GovernanceCockpit: React.FC = () => {
  return (
    <div className="min-h-screen bg-black text-slate-200 p-8 font-sans">
      <header className="mb-12 border-b border-slate-800 pb-6">
        <h1 className="text-3xl font-extrabold text-white tracking-tighter">
          OMNI-SENTINEL <span className="text-blue-500 font-light">GOVERNANCE COCKPIT v2.4</span>
        </h1>
        <p className="text-slate-500 mt-2">Authority: JULES-APEX | Systemic Risk Monitoring (G-SIFI)</p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <GSRIDriftSimulator currentScore={9.3} />
        <PQCStatusCard />
        <div className="bg-slate-900 p-6 rounded-lg border border-red-900/50">
          <h3 className="text-red-400 font-bold flex items-center gap-2 mb-4">
            <AlertTriangle size={20} /> OmegaActual Fail-safe
          </h3>
          <div className="p-4 bg-red-950/30 rounded border border-red-800/50">
            <p className="text-xs text-red-300 mb-2 font-mono uppercase">On-chain Kill-switch Status</p>
            <div className="text-xl font-bold text-red-500">STABLE (3/5 Quorum)</div>
            <div className="mt-4 text-[10px] text-red-400/70 font-mono">
              ADDR: 0xOmegaActual_Primary_HSM...
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
