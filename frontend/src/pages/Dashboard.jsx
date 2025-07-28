import { useNavigate } from "react-router-dom";
import { UserAuth } from "../context/AuthContext";
import { BASE_URL } from "../config";
import "../styles/dashboard.css";

export default function Dashboard() {
  const { session, guest, signOut } = UserAuth();
  const navigate = useNavigate();

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
      </div>
    </div>
  );
}
