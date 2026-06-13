import React, { useState } from 'react';

interface Incident {
  id: string;
  type: string;
  severity: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
  status: 'OPEN' | 'RESOLVED' | 'MITIGATED';
  timestamp: string;
}

export const GAISOCDashboard: React.FC = () => {
  const [incidents] = useState<Incident[]>([
    { id: 'INC-2026-001', type: 'MOE_DRIFT', severity: 'MEDIUM', status: 'RESOLVED', timestamp: '2026-06-05' },
    { id: 'INC-2026-002', type: 'RED_DAWN_SIM', severity: 'HIGH', status: 'MITIGATED', timestamp: '2026-06-10' },
    { id: 'INC-2026-003', type: 'LATENCY_SPIKE', severity: 'LOW', status: 'RESOLVED', timestamp: '2026-06-12' }
  ]);

  return (
    <div className="p-8 bg-zinc-950 text-slate-100 min-h-screen">
      <h1 className="text-2xl font-bold mb-8">GAI-SOC: Global Intelligence Security Operations Center</h1>

      <div className="grid grid-cols-1 gap-4">
        {incidents.map(inc => (
          <div key={inc.id} className="p-4 bg-zinc-900 border border-zinc-800 rounded-xl flex justify-between items-center">
            <div>
              <span className="text-zinc-500 text-xs font-mono">{inc.id}</span>
              <h3 className="font-semibold">{inc.type}</h3>
            </div>
            <div className="flex gap-6 items-center">
              <span className={`px-3 py-1 rounded-full text-xs font-bold ${
                inc.severity === 'CRITICAL' ? 'bg-red-900 text-red-200' :
                inc.severity === 'HIGH' ? 'bg-orange-900 text-orange-200' :
                'bg-blue-900 text-blue-200'
              }`}>
                {inc.severity}
              </span>
              <span className="text-zinc-400 text-sm">{inc.timestamp}</span>
              <span className="text-emerald-500 text-sm font-bold">{inc.status}</span>
            </div>
          </div>
        ))}
      </div>

      <footer className="mt-12 border-t border-zinc-800 pt-6 text-zinc-600 text-xs">
        GAI-SOC Telemetry Mesh Status: <span className="text-emerald-600 font-bold uppercase">Healthy</span> |
        Sync Latency: <span className="font-mono">14ms</span>
      </footer>
    </div>
  );
};
