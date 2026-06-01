import React from 'react';

const PopulationHeatmap: React.FC = () => {
  return (
    <div className="population-heatmap" style={{ height: '300px', width: '100%', background: '#1a1a1a', color: '#fff', padding: '20px' }}>
      <h3>Cross-Jurisdictional Alignment Heatmap</h3>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(10, 1fr)', gap: '2px', height: '200px' }}>
        {Array.from({ length: 100 }).map((_, i) => (
          <div key={i} style={{
            background: i % 7 === 0 ? '#ff5252' : '#4caf50',
            opacity: 0.5 + (Math.random() * 0.5),
            border: '1px solid #333'
          }} />
        ))}
      </div>
      <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '10px' }}>
        <span>EU (Frankfurt) - ALIGNED</span>
        <span>US (Ohio) - DRIFT DETECTED</span>
        <span>SG (Changi) - ALIGNED</span>
      </div>
    </div>
  );
};

export default PopulationHeatmap;
