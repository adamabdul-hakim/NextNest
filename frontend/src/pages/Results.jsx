import { useLocation, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import { fetchFlights, fetchJobs, fetchCitySummary } from "../services/api";
import "../styles/results.css";
import { BASE_URL } from "../config";
import { UserAuth } from "../context/AuthContext";

export default function Results() {
  const { session, guest } = UserAuth();
  const { state } = useLocation();
  const navigate = useNavigate();
  const { originCity, destinationCity, date, field } = state || {};

  const [flight, setFlight] = useState(null);
  const [jobs, setJobs] = useState([]);
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(true);
  const [saved, setSaved] = useState(false);

  useEffect(() => {
    async function loadData() {
      try {
        const [flightData, jobsData, summaryData] = await Promise.all([
          fetchFlights(originCity, destinationCity, date),
          fetchJobs(field, destinationCity),
          fetchCitySummary(destinationCity),
        ]);
        setFlight(flightData);
        setJobs(jobsData);
        setSummary(summaryData);
      } catch (err) {
        console.error(err);
        alert("Something went wrong while loading results.");
      } finally {
        setLoading(false);
      }
    }
    if (originCity && destinationCity && date) {
      loadData();
    }
  }, [originCity, destinationCity, date, field]);

  const handleSave = async () => {
    console.log("Session before save:", session);

    // block guests and non-signed-in users
    if (!session || guest) {
      alert("Sign in to save your history.");
      return;
    }

    try {
      await fetch(`${BASE_URL}/api/history`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${session.access_token}`,
        },
        body: JSON.stringify({
          origin_city: originCity,
          destination_city: destinationCity,
          role: field,
          travel_date: date,
        }),
      });
      setSaved(true);
    } catch (err) {
      console.error("Error saving history:", err);
      alert("Could not save to history.");
    }
  };

  const handleViewHistory = () => {
    // ✅ block guests from viewing history
    if (!session || guest) {
      alert("Sign in to view your history.");
      return;
    }
    navigate("/history");
  };

  const handleSearchAgain = () => {
    navigate("/input");
  };

  if (loading) {
    return (
      <div className="loading-container">
        <div className="spinner"></div>
        <h2>Finding the best options for you...</h2>
      </div>
    );
  }

  return (
    <div className="results-container">
      <h1>Results</h1>

      {flight && (
        <section>
          <h2>Cheapest Flight</h2>
          <p>
            <strong>Airline:</strong> {flight.airline}
          </p>
          <p>
            <strong>Price:</strong> ${flight.price}
          </p>
        </section>
      )}

      {summary && (
        <section>
          <h2>City Summary</h2>
          <p>
            <strong>Average Temp:</strong> {summary.average_temp}°F
          </p>
          <p>{summary.summary}</p>
        </section>
      )}

      {jobs.length > 0 && (
        <section>
          <h2>Jobs in {field}</h2>
          <ul>
            {jobs.map((job, idx) => (
              <li key={idx}>
                <a href={job.redirect_url} target="_blank" rel="noreferrer">
                  {job.title}
                </a>
                <p>
                  {job.company} – {job.location}
                </p>
              </li>
            ))}
          </ul>
        </section>
      )}

      <div className="results-actions">
        <button onClick={handleSave} disabled={saved}>
          {saved ? "Saved!" : "Save Results"}
        </button>
        <button onClick={handleViewHistory}>View History</button>
        <button onClick={handleSearchAgain}>Search Again</button>
      </div>
    </div>
  );
}
