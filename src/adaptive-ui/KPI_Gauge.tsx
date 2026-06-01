import React from 'react';

interface KPIGaugeProps {
  label: string;
  value: number;
  threshold: number;
}

const KPIGauge: React.FC<KPIGaugeProps> = ({ label, value, threshold }) => {
  const isHealthy = value >= threshold;
  const color = isHealthy ? '#4CAF50' : '#F44336';

  return (
    <div className="kpi-gauge" style={{ border: '1px solid #ccc', padding: '10px', borderRadius: '8px', width: '200px' }}>
      <h4>{label}</h4>
      <div style={{ fontSize: '24px', fontWeight: 'bold', color }}>
        {(value * 100).toFixed(1)}%
      </div>
      <div style={{ fontSize: '12px', color: '#666' }}>
        Target: >{(threshold * 100).toFixed(0)}%
      </div>
      <div style={{ marginTop: '10px', background: '#eee', height: '10px', borderRadius: '5px' }}>
        <div style={{ background: color, width: `${value * 100}%`, height: '100%', borderRadius: '5px' }} />
      </div>
    </div>
  );
};

export default KPIGauge;
