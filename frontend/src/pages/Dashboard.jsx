import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import { UserAuth } from "../context/AuthContext";
import { BASE_URL } from "../config";
import "../styles/dashboard.css";

export default function Dashboard() {
  const { session, guest, signOut } = UserAuth();
  const navigate = useNavigate();
  const [recentCities, setRecentCities] = useState([]);

  useEffect(() => {
    const loadRecent = async () => {
      if (guest || !session) return; // skip for guest
      try {
        const res = await fetch(`${BASE_URL}/api/history`, {
          headers: {
            Authorization: `Bearer ${session.access_token}`,
          },
        });
        const data = await res.json();

        // Extract unique destination cities in order
        const unique = [];
        for (const item of data) {
          if (!unique.includes(item.destination_city)) {
            unique.push(item.destination_city);
          }
          if (unique.length >= 5) break; // show up to 5
        }
        setRecentCities(unique);
      } catch (err) {
        console.error("Error loading recent cities:", err);
      }
    };
    loadRecent();
  }, [session, guest]);

  const handleSignOut = () => {
    signOut();
    navigate("/");
  };

  return (
    <div className="dashboard-container">
      {/* Header */}
      <header className="dashboard-header">
        <h1>NextNest</h1>
        <div className="dashboard-header-right">
          <span className="welcome-text">
            {guest
              ? "Welcome, Guest!"
              : `Welcome, ${session?.user?.user_metadata?.username || "User"}!`}
          </span>
          <button className="signout-btn" onClick={handleSignOut}>
            Sign Out
          </button>
        </div>
      </header>

      {/* Tagline */}
      <p className="dashboard-tagline">Choose what you’d like to do next.</p>

      {/* Main actions */}
      <div className="dashboard-grid">
        <div
          className="dashboard-card primary"
          onClick={() => navigate("/input")}
        >
          <h2>Start a New Search</h2>
          <p>Check flights, jobs, and city info instantly.</p>
        </div>

        <div
          className={`dashboard-card ${guest ? "disabled" : ""}`}
          onClick={() => {
            if (!guest) navigate("/history");
          }}
        >
          <h2>View History</h2>
          <p>
            {guest ? "Sign in to view history." : "See your saved searches."}
          </p>
        </div>
      </div>

      {/* Extras */}
      <div className="dashboard-extras">
        <div className="tips-panel">
          <h3>Tips</h3>
          <ul>
            <li>Search different cities to compare opportunities.</li>
            <li>Save results to revisit later.</li>
            <li>Sign in for full features!</li>
          </ul>
        </div>

        {!guest && recentCities.length > 0 && (
          <div className="recent-panel">
            <h3>Recently Viewed Cities</h3>
            <div className="recent-tags">
              {recentCities.map((city) => (
                <span key={city} className="tag">
                  {city}
                </span>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
