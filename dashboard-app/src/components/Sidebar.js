// src/components/Sidebar.js
import React from "react";

export default function Sidebar({ onNavigate }) {
  return (
    <div style={{
      width: "180px",
      background: "#1a1a1a",
      height: "100vh",
      padding: "20px",
      borderRight: "1px solid #333"
    }}>
      <h2 style={{ color: "#00e5ff" }}>⚡ Monitor</h2>
      <ul style={{ listStyle: "none", padding: 0, marginTop: "30px" }}>
        <li onClick={() => onNavigate("dashboard")}
            style={{ cursor: "pointer", margin: "15px 0", color: "#e0e0e0" }}>
          🏠 Dashboard
        </li>
        <li onClick={() => onNavigate("settings")}
            style={{ cursor: "pointer", margin: "15px 0", color: "#e0e0e0" }}>
          ⚙ Configuración
        </li>
      </ul>
    </div>
  );
}
