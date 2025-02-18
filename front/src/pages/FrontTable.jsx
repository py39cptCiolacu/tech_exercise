import React, { useState, useEffect } from "react";
import Orders from "./Orders";
import Materials from "./Materials";
import Aircrafts from "./Aircrafts";
import Upload from "./Upload";
import "../styles/FrontTable.css";

export default function FrontTable() {
  const [activeTab, setActiveTab] = useState(localStorage.getItem("activeTab") || "orders");
  const [refreshKey, setRefreshKey] = useState(0);

  useEffect(() => {
    localStorage.setItem("activeTab", activeTab);
  }, [activeTab]);

  const handleUploadSuccess = () => {
    setRefreshKey((prevKey) => prevKey + 1);
  };

  return (
    <div>
      {/* Title Bar */}
      <div className="title-bar">DATABASE DEMO APP</div>

      {/* Header buttons */}
      <div className="header">
        <button
          onClick={() => setActiveTab("orders")}
          className={activeTab === "orders" ? "active" : ""}
        >
          ORDERS
        </button>
        <button
          onClick={() => setActiveTab("materials")}
          className={activeTab === "materials" ? "active" : ""}
        >
          MATERIALS
        </button>
        <button
          onClick={() => setActiveTab("aircrafts")}
          className={activeTab === "aircrafts" ? "active" : ""}
        >
          AIRCRAFTS
        </button>
      </div>

      {/* Table */}
      <div className="content">
        {activeTab === "orders" && <Orders key={refreshKey} />}
        {activeTab === "materials" && <Materials key={refreshKey} />}
        {activeTab === "aircrafts" && <Aircrafts key={refreshKey} />}
      </div>

      {/* Upload Buttons */}
      <Upload activeTab={activeTab} onUploadSuccess={handleUploadSuccess} />
    </div>
  );
}
