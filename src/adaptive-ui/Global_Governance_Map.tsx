import React from 'react';

/**
 * Global Governance Telemetry Map
 * Visualizes planetary AGI compliance, compute distribution (ICGC),
 * and SEV-0 containment status across global jurisdictions.
 */

interface JurisdictionNode {
  id: string;
  name: string;
  complianceScore: number;
  activeTreaties: string[];
  sevStatus: 'NORMAL' | 'WARN' | 'CRITICAL' | 'LOCKDOWN';
  computeUsage: number; // in ExaFLOPs
}

const GlobalGovernanceMap: React.FC = () => {
  const nodes: JurisdictionNode[] = [
    { id: 'us-01', name: 'USA (NIST/EO)', complianceScore: 0.98, activeTreaties: ['GASRGP', 'GASC'], sevStatus: 'NORMAL', computeUsage: 450 },
    { id: 'eu-01', name: 'EU (AI Act/ISO)', complianceScore: 0.99, activeTreaties: ['GAISM', 'GASC'], sevStatus: 'NORMAL', computeUsage: 380 },
    { id: 'sg-01', name: 'Singapore (MAS/AIMS)', complianceScore: 0.97, activeTreaties: ['GACRA', 'GACP'], sevStatus: 'NORMAL', computeUsage: 120 },
    { id: 'global-adm', name: 'ICGC Planetary Node', complianceScore: 1.0, activeTreaties: ['GLOBAL_CONSTITUTION'], sevStatus: 'LOCKDOWN', computeUsage: 10 }
  ];

  return (
    <div className="bg-slate-900 text-white p-6 rounded-xl border border-slate-700 shadow-2xl">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold tracking-tight">Planetary AGI Supervisory Mesh (EAIP v3.0)</h2>
        <span className="bg-red-900 text-red-100 px-3 py-1 rounded-full text-sm animate-pulse">
          ICGC ENFORCEMENT: ACTIVE
        </span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {nodes.map(node => (
          <div key={node.id} className="p-4 bg-slate-800 rounded-lg border border-slate-600 hover:border-blue-500 transition-all">
            <div className="flex justify-between items-start mb-2">
              <h3 className="font-semibold text-lg">{node.name}</h3>
              <span className={`px-2 py-0.5 rounded text-xs font-mono ${
                node.sevStatus === 'LOCKDOWN' ? 'bg-red-600' : 'bg-green-600'
              }`}>
                {node.sevStatus}
              </span>
            </div>

            <div className="space-y-2 text-sm text-slate-300">
              <div className="flex justify-between">
                <span>Compliance Score</span>
                <span className="font-mono text-blue-400">{(node.complianceScore * 100).toFixed(1)}%</span>
              </div>
              <div className="flex justify-between">
                <span>Compute Usage</span>
                <span className="font-mono text-yellow-400">{node.computeUsage} E-FLOPs</span>
              </div>
              <div className="mt-3">
                <p className="text-xs text-slate-500 mb-1 uppercase tracking-widest">Active Stability Protocols</p>
                <div className="flex flex-wrap gap-2">
                  {node.activeTreaties.map(t => (
                    <span key={t} className="bg-slate-700 px-2 py-0.5 rounded text-[10px] font-bold text-slate-400">
                      {t}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className="mt-6 border-t border-slate-700 pt-4 flex items-center justify-between">
        <div className="text-xs text-slate-500 italic">
          Homeostatic Drift Delta: <span className="text-green-500">+0.003%</span>
        </div>
        <button className="bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold px-4 py-2 rounded uppercase tracking-widest transition-colors">
          Initiate Cross-Border Audit
        </button>
      </div>
    </div>
  );
};

export default GlobalGovernanceMap;
