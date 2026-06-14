import React from 'react';

interface Mapping {
  standard: string;
  control: string;
  artifact: string;
  status: 'VERIFIED' | 'PENDING';
}

export const RegulatoryMappingDashboard: React.FC = () => {
  const mappings: Mapping[] = [
    { standard: 'EU AI Act', control: 'Annex IV (Tech Doc)', artifact: 'PQC-WORM RCE Logs', status: 'VERIFIED' },
    { standard: 'NIST AI RMF', control: 'GOVERN 1.2', artifact: 'G-SRI Scoring Engine', status: 'VERIFIED' },
    { standard: 'Basel IV', control: 'Op Resilience', artifact: 'IRMI Hardware Kill-Switch', status: 'VERIFIED' },
    { standard: 'Fed SR 11-7', control: 'Continuous Validation', artifact: 'RGPP Probe (Variance < 0.02)', status: 'VERIFIED' },
    { standard: 'GDPR', control: 'Article 22', artifact: 'WorkflowAI Pro (EBM Explainers)', status: 'VERIFIED' },
    { standard: 'DORA', control: 'ICT Resilience', artifact: 'Multi-Region Terraform / IMDSv2', status: 'VERIFIED' }
  ];

  return (
    <div className="p-8 bg-black text-white min-h-screen">
      <h1 className="text-2xl font-bold mb-8 tracking-tight">Sentinel Regulatory Mapping Dashboard</h1>
      <div className="overflow-hidden rounded-xl border border-zinc-800 bg-zinc-900/50">
        <table className="min-w-full divide-y divide-zinc-800">
          <thead className="bg-zinc-800/50 text-zinc-400 text-xs uppercase font-bold">
            <tr>
              <th className="px-6 py-4 text-left">Regulatory Regime</th>
              <th className="px-6 py-4 text-left">Control Requirement</th>
              <th className="px-6 py-4 text-left">Implementation Artifact</th>
              <th className="px-6 py-4 text-left">Integrity Status</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-zinc-800 text-sm">
            {mappings.map((m, i) => (
              <tr key={i} className="hover:bg-zinc-800/30 transition-colors">
                <td className="px-6 py-4 font-semibold text-indigo-400">{m.standard}</td>
                <td className="px-6 py-4 text-zinc-300">{m.control}</td>
                <td className="px-6 py-4 font-mono text-xs text-zinc-500">{m.artifact}</td>
                <td className="px-6 py-4">
                  <span className="bg-emerald-900/40 text-emerald-400 px-2 py-1 rounded text-[10px] font-bold border border-emerald-500/30">
                    {m.status}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
