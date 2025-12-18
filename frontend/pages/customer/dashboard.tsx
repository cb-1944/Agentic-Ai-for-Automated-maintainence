import { useEffect, useState } from "react";

export default function CustomerDashboard() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:8000/run-diagnosis", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        phone : "+919665070980",
        vehicle_id: 101,
        rpm: 4300,
        temp: 110,
        speed: 22
      })
    })
      .then(res => res.json())
      .then(result => {
        setData(result);
        setLoading(false);
      });
  }, []);
  function getShortDiagnosis(diagnosis) {

    if (!diagnosis) return "No issues detected.";
  
    if (diagnosis.severity === "HIGH") {
      return "Critical engine issue detected — immediate service recommended.";
    }
  
    if (diagnosis.severity === "MEDIUM") {
      return "Vehicle performance issue detected — service advised.";
    }
  
    return "Minor issue detected — monitor vehicle performance.";
  }
  

  if (loading) return <p>Loading vehicle health...</p>;

  return (
    <div className="p-10">
      <h1 className="text-2xl font-semibold">Vehicle Health</h1>

      {data.anomaly_result.is_anomaly && (
        <div className="mt-6 p-4 border-l-4 border-red-500 bg-red-50">
          <h2 className="font-medium">Anomaly Detected</h2>
          <p className="text-sm mt-1">
            {data.anomaly_result.anomalies.join(", ")}
           
          </p>
          <p className="text-sm mt-1" >{getShortDiagnosis(data.diagnosis)}</p>

        </div>
      )}

      <div className="mt-6">
        Vehicle Health Score : 85 
      </div>
    </div>
  );
}
