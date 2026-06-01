import React from 'react';

interface DecisionTrace {
  uuid: string;
  timestamp: string;
  input: string;
  output: string;
  policy: string;
  evidence_hash: string;
}

const AuditReplay: React.FC<{ trace: DecisionTrace }> = ({ trace }) => {
  return (
    <div className="audit-replay" style={{ background: '#f9f9f9', padding: '20px', border: '1px solid #ddd' }}>
      <h3>Deterministic Audit Replay: {trace.uuid}</h3>
      <p><strong>Timestamp:</strong> {trace.timestamp}</p>
      <div style={{ display: 'flex', gap: '20px' }}>
        <div style={{ flex: 1 }}>
          <h4>Input Context</h4>
          <pre style={{ background: '#eee', padding: '10px' }}>{trace.input}</pre>
        </div>
        <div style={{ flex: 1 }}>
          <h4>Policy Logic ({trace.policy})</h4>
          <pre style={{ background: '#e3f2fd', padding: '10px' }}>IF input.risk > 0.5 THEN DENY</pre>
        </div>
        <div style={{ flex: 1 }}>
          <h4>Model Output</h4>
          <pre style={{ background: '#e8f5e9', padding: '10px' }}>{trace.output}</pre>
        </div>
      </div>
      <p style={{ fontSize: '10px', color: '#999' }}>Evidence Integrity Hash: {trace.evidence_hash}</p>
      <button style={{ padding: '10px 20px', background: '#007bff', color: '#fff', border: 'none', borderRadius: '4px' }}>
        Validate Evidence Manifest
      </button>
    </div>
  );
};

export default AuditReplay;
