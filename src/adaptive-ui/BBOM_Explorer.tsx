import React from 'react';

export const BBOMExplorer: React.FC = () => {
  return (
    <div className="p-8 bg-zinc-900 text-zinc-100 min-h-screen font-mono text-sm">
      <h1 className="text-xl font-bold mb-8 border-b border-zinc-700 pb-4">Blockchain Bill of Materials (BBOM) Explorer</h1>

      <div className="space-y-6">
        <section className="p-4 bg-zinc-800 rounded border border-zinc-700">
          <h2 className="text-indigo-400 font-bold mb-2">Core Kernel</h2>
          <p>ID: spiffe://gsifi.internal/sentinel/kernel</p>
          <p className="text-zinc-500">Hash: 0x7f8a3e21b0c9d4e5f6a1b2c3d4e5f6a1</p>
        </section>

        <section className="p-4 bg-zinc-800 rounded border border-zinc-700">
          <h2 className="text-indigo-400 font-bold mb-2">Safety Invariants (GDL)</h2>
          <p>Version: v3.2.9-Canonical</p>
          <p className="text-zinc-500">Hash: 0x9d8e6a1b2c3d4e5f0a1b2c3d4e5f6a1b</p>
        </section>

        <section className="p-4 bg-zinc-800 rounded border border-zinc-700">
          <h2 className="text-indigo-400 font-bold mb-2">Attestation State</h2>
          <p>Status: PCR_MATCH_TRUE</p>
          <p>Timestamp: 2026-06-14T12:00:00Z</p>
        </section>
      </div>
    </div>
  );
};
