import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/history.css";
import { BASE_URL } from "../config";
import { UserAuth } from "../context/AuthContext";

export default function History() {
  const { session } = UserAuth();
  const [history, setHistory] = useState([]);
  const navigate = useNavigate();

  const fetchHistory = async () => {
    if (!session) return;
    const res = await fetch(`${BASE_URL}/api/history`, {
      headers: {
        Authorization: `Bearer ${session.access_token}`,
      },
    });
    const data = await res.json();
    setHistory(data);
  };

  const handleClearHistory = async () => {
    if (!window.confirm("Are you sure you want to clear all history?")) return;
    if (!session) return;
    await fetch(`${BASE_URL}/api/history/clear`, {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${session.access_token}`,
      },
    });
    setHistory([]);
  };

  const handleGoHome = () => {
    navigate("/");
  };

  useEffect(() => {
    fetchHistory();
  }, [session]); // re-fetch when session changes

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
