import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/history.css";

export default function History() {
  const [history, setHistory] = useState([]);
  const navigate = useNavigate();

  const fetchHistory = async () => {
    const res = await fetch("http://127.0.0.1:5001/api/history");
    const data = await res.json();
    setHistory(data);
  };

  const handleClearHistory = async () => {
    if (!window.confirm("Are you sure you want to clear all history?")) return;
    await fetch("http://127.0.0.1:5001/api/history/clear", {
      method: "DELETE",
    });
    setHistory([]);
  };

  const handleGoHome = () => {
    navigate("/");
  };

  useEffect(() => {
    fetchHistory();
  }, []);

  return (
    <div className="history-container">
      <h1>Search History</h1>

      {history.length === 0 ? (
        <p className="empty">No history yet.</p>
      ) : (
        <ul className="history-list">
          {history.map((item, idx) => (
            <li key={idx} className="history-item">
              <div>
                <strong>{item.origin_city}</strong> ➡️{" "}
                <strong>{item.destination_city}</strong>
              </div>
              <div>
                {item.role && <span>Role: {item.role}</span>}
                {item.travel_date && <span> | Date: {item.travel_date}</span>}
              </div>
            </li>
          ))}
        </ul>
      )}

      <div className="history-actions">
        <button className="clear-btn" onClick={handleClearHistory}>
          Clear History
        </button>
        <button className="home-btn" onClick={handleGoHome}>
          Home
        </button>
      </div>
    </div>
  );
}
