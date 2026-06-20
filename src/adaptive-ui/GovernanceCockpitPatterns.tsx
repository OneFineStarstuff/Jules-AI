import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, AreaChart, Area } from 'recharts';
import { Shield, AlertTriangle, Activity, Lock, Zap, Share2, Eye, Terminal, Play } from 'lucide-react';

/**
 * Omni-Sentinel Governance Cockpit Components (Phase I/II Implementation)
 * Standardizing on Deep Onyx / Governance Blue palette for G-SIFI environments.
 */

// 1. G-SRI Drift Simulator (Bayesian Trajectory)
export const GSRIDriftSimulator: React.FC<{ currentScore: number }> = ({ currentScore }) => {
  const [data, setData] = useState([{ time: 0, score: currentScore, uncertainty: 2 }]);

  useEffect(() => {
    const interval = setInterval(() => {
      setData(prev => {
        const last = prev[prev.length - 1];
        const drift = (Math.random() - 0.48) * 1.5; // Slight upward bias for simulation
        const nextScore = Math.max(0, Math.min(100, last.score + drift));
        return [...prev.slice(-30), {
          time: last.time + 1,
          score: nextScore,
          uncertainty: Math.max(1, last.uncertainty + (Math.random() - 0.5))
        }];
      });
    }, 2000);
    return () => clearInterval(interval);
  }, [currentScore]);

  return (
    <div className="bg-slate-950 p-6 rounded-xl border border-blue-900/50 shadow-2xl">
      <div className="flex justify-between items-center mb-6">
        <h3 className="text-blue-400 font-bold flex items-center gap-2">
          <Activity size={18} className="text-blue-500" /> G-SRI Systemic Risk Index
        </h3>
        <span className="text-xs font-mono text-blue-800 bg-blue-950/50 px-2 py-1 rounded">BAYESIAN_UPDATE_ACTIVE</span>
      </div>
      <div className="h-48">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={data}>
            <defs>
              <linearGradient id="colorScore" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.3}/>
                <stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/>
              </linearGradient>
            </defs>
            <CartesianGrid strokeDasharray="3 3" stroke="#0f172a" vertical={false} />
            <XAxis dataKey="time" hide />
            <YAxis domain={[0, 1.0]} stroke="#1e293b" fontSize={10} tickFormatter={(val) => val.toFixed(2)} />
            <Tooltip
              contentStyle={{ backgroundColor: '#020617', border: '1px solid #1e3a8a', borderRadius: '8px' }}
              itemStyle={{ color: '#60a5fa' }}
            />
            <Area type="monotone" dataKey="score" stroke="#3b82f6" strokeWidth={2} fillOpacity={1} fill="url(#colorScore)" />
          </AreaChart>
        </ResponsiveContainer>
      </div>
      <div className="mt-6 flex justify-between items-end">
        <div>
          <p className="text-[10px] text-slate-500 uppercase tracking-widest font-semibold">Current G-SRI</p>
          <p className="text-2xl font-bold text-white font-mono">{data[data.length-1].score.toFixed(4)}</p>
        </div>
        <div className="text-right">
          <p className="text-[10px] text-slate-500 uppercase tracking-widest font-semibold">Status</p>
          <span className={`text-xs font-bold ${data[data.length-1].score < 0.85 ? "text-green-500" : "text-red-500"}`}>
            {data[data.length-1].score < 0.85 ? "NOMINAL" : "CRITICAL_INTERVENTION"}
          </span>
        </div>
      </div>
    </div>
  );
};

// 2. PQC WORM Integrity Card
export const PQCIntegrityPanel: React.FC = () => (
  <div className="bg-slate-950 p-6 rounded-xl border border-blue-900/50 shadow-2xl">
    <h3 className="text-blue-400 font-bold flex items-center gap-2 mb-6">
      <Lock size={18} className="text-emerald-500" /> PQC WORM Anchor (ML-DSA-87)
    </h3>
    <div className="space-y-4">
      <div className="flex justify-between border-b border-slate-900 pb-2">
        <span className="text-slate-500 text-xs">Signature Engine</span>
        <span className="text-blue-300 font-mono text-xs">CRYSTALS-Dilithium-v3</span>
      </div>
      <div className="flex justify-between border-b border-slate-900 pb-2">
        <span className="text-slate-500 text-xs">Audit Sink</span>
        <span className="text-blue-300 font-mono text-xs">AWS_S3_OBJECT_LOCK</span>
      </div>
      <div className="flex justify-between border-b border-slate-900 pb-2">
        <span className="text-slate-500 text-xs">Anchoring Frequency</span>
        <span className="text-blue-300 font-mono text-xs">60s_EPOCH</span>
      </div>
      <div className="pt-2">
        <div className="flex items-center gap-2 text-emerald-500 text-[10px] font-bold">
          <div className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
          INTEGRITY_CHAIN_VERIFIED
        </div>
      </div>
    </div>
  </div>
);

// 3. GIEN Gossip Mesh & OmegaActual Status
export const GIENMeshStatus: React.FC = () => (
  <div className="bg-slate-950 p-6 rounded-xl border border-blue-900/50 shadow-2xl">
    <h3 className="text-blue-400 font-bold flex items-center gap-2 mb-6">
      <Share2 size={18} className="text-indigo-500" /> GIEN Gossip Mesh
    </h3>
    <div className="flex flex-col gap-4">
      <div className="p-3 bg-blue-950/20 rounded border border-blue-800/30">
        <p className="text-[10px] text-blue-500 uppercase font-bold mb-1">OmegaActual Heartbeat</p>
        <div className="flex justify-between items-center">
          <span className="text-sm font-bold text-white">3-of-5 QUORUM</span>
          <Zap size={14} className="text-yellow-500" />
        </div>
      </div>
      <div className="p-3 bg-red-950/20 rounded border border-red-800/30">
        <p className="text-[10px] text-red-500 uppercase font-bold mb-1">On-chain Kill-switch</p>
        <div className="flex justify-between items-center">
          <span className="text-sm font-bold text-white font-mono">0xOmega_STABLE</span>
          <AlertTriangle size={14} className="text-red-500" />
        </div>
      </div>
    </div>
  </div>
);

// 4. OPA/Rego Policy Join-Point Editor (Minimal Preview)
export const PolicyJoinPointEditor: React.FC = () => (
  <div className="bg-slate-950 p-6 rounded-xl border border-slate-800 shadow-2xl col-span-1 lg:col-span-2">
    <div className="flex justify-between items-center mb-4">
      <h3 className="text-slate-300 font-bold flex items-center gap-2">
        <Terminal size={18} /> GDL / OPA Policy Editor
      </h3>
      <div className="flex gap-2">
        <button className="px-3 py-1 bg-slate-900 text-[10px] rounded border border-slate-700 hover:bg-slate-800 transition-colors">TEST_TLA+</button>
        <button className="px-3 py-1 bg-blue-600 text-[10px] rounded font-bold hover:bg-blue-500 transition-colors">COMMIT_CANON</button>
      </div>
    </div>
    <div className="bg-black p-4 rounded border border-slate-900 font-mono text-xs text-emerald-400 overflow-x-auto">
      <p>package sentinel.authz</p>
      <p className="mt-2 text-slate-600"># Enforce G-SRI Threshold for Trading Swarm</p>
      <p><span className="text-blue-400">deny</span> if {'{'}</p>
      <p className="pl-4">input.gsri_score {'>'} 0.85</p>
      <p className="pl-4 text-slate-600"># Trigger PACIFIC_SHIELD containment</p>
      <p className="pl-4">data.active_protocols["PACIFIC_SHIELD"] == <span className="text-orange-400">true</span></p>
      <p>{'}'}</p>
    </div>
  </div>
);

// 5. Main Governance Cockpit v2.4
export const GovernanceCockpit: React.FC = () => {
  return (
    <div className="min-h-screen bg-black text-slate-200 p-8 font-sans selection:bg-blue-500/30">
      <header className="mb-12 flex justify-between items-start border-b border-slate-900 pb-8">
        <div>
          <h1 className="text-4xl font-black text-white tracking-tighter flex items-center gap-3">
            <Shield className="text-blue-500" size={32} />
            OMNI-SENTINEL <span className="text-blue-500 font-extralight italic">CEE v2.4</span>
          </h1>
          <p className="text-slate-500 mt-2 font-medium">Global AI Supervisory Control Plane | Apex-G-SIFI Node</p>
        </div>
        <div className="text-right">
          <div className="inline-flex items-center gap-2 px-3 py-1 bg-emerald-950/30 border border-emerald-800/50 rounded-full text-emerald-500 text-xs font-bold mb-2">
            <div className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
            STEADY_GOVERNANCE_STATE
          </div>
          <p className="text-[10px] font-mono text-slate-600 uppercase">Timestamp: 2026-06-18T12:00:00Z</p>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <GSRIDriftSimulator currentScore={0.093} />
        <PQCIntegrityPanel />
        <GIENMeshStatus />
        <PolicyJoinPointEditor />
        <div className="bg-slate-950 p-6 rounded-xl border border-slate-800 shadow-2xl flex flex-col justify-center items-center gap-4 group cursor-pointer hover:border-blue-900 transition-all">
          <Play size={48} className="text-slate-800 group-hover:text-blue-500 transition-colors" />
          <p className="text-xs font-bold text-slate-500 group-hover:text-blue-400">LAUNCH_CONTAINMENT_SIMULATION</p>
          <div className="flex gap-2 mt-2">
            <span className="text-[8px] bg-slate-900 px-2 py-0.5 rounded text-slate-500">RED_DAWN</span>
            <span className="text-[8px] bg-slate-900 px-2 py-0.5 rounded text-slate-500">RY-99</span>
          </div>
        </div>
      </div>

      <footer className="mt-16 pt-8 border-t border-slate-900 flex justify-between items-center text-[10px] text-slate-700 font-mono">
        <div className="flex gap-6">
          <span>PCR_MATCH: TRUE</span>
          <span>vTPM: ACTIVE</span>
          <span>SPIFFE: VERIFIED</span>
        </div>
        <div className="flex gap-2 items-center">
          <Eye size={12} /> READ_ONLY_AUDIT_LOGS_STREAMING
        </div>
      </footer>
    </div>
  );
};

export default GovernanceCockpit;
