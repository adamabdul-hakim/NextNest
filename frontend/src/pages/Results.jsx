import { useLocation, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import { fetchFlights, fetchJobs, fetchCitySummary, fetchTransportationSummary, fetchSalaryComparison  } from "../services/api";
import "../styles/results.css";
import { BASE_URL } from "../config";
import { UserAuth } from "../context/AuthContext";

export default function Results() {
  const { session, guest } = UserAuth();
  const { state } = useLocation();
  const navigate = useNavigate();
  const { originCity, destinationCity, current_role, date, field } = state || {};

  const [flight, setFlight] = useState(null);
  const [jobs, setJobs] = useState([]);
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(true);
  const [saved, setSaved] = useState(false);
  const [transportation, setTransportation] = useState(null);
  const [jobComparison, setJobComparison] = useState(null);

  useEffect(() => {
    async function loadData() {
      try {
        const [flightData, jobsData, summaryData, transportationData, jobComparisonData] = await Promise.all([
          fetchFlights(originCity, destinationCity, date),
          fetchJobs(field, destinationCity),
          fetchCitySummary(destinationCity),
          fetchTransportationSummary(destinationCity),  // 🆕 added line
          fetchSalaryComparison(originCity, destinationCity, current_role, field),
        ]);
        setFlight(flightData);
        setJobs(jobsData);
        setSummary(summaryData);
        setTransportation(transportationData);  // 🆕 set transportation
        setJobComparison(jobComparisonData)
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
  }, [originCity, destinationCity, date, field, current_role]);

  const handleSave = async () => {
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
          current_role: current_role,
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
          {/* ✅ Book Flight Link */}
          <a
            href={`https://www.google.com/flights?hl=en#flt=${encodeURIComponent(
              originCity
            )}.${encodeURIComponent(destinationCity)}.${encodeURIComponent(
              date
            )}`}
            target="_blank"
            rel="noopener noreferrer"
            className="book-link"
          >
            Book This Flight
          </a>
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

      {transportation && (
        <section>
          <h2>Transportation in {transportation.city}</h2>

          <p>
            <strong>Walk Score:</strong> {transportation.walk.score}/100<br />
            <em>{transportation.walk.description}</em>
          </p>

          <p>
            <strong>Bike Score:</strong> {transportation.bike.score}/100<br />
            <em>{transportation.bike.description}</em>
          </p>

          <p>
            <strong>Drive Score:</strong> {transportation.drive.score}/100<br />
            <em>{transportation.drive.description}</em>
          </p>
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

      {jobComparison && (
        <section>
          <h2>Salary Comparison</h2>

          {!jobComparison.match ? (
            <p>{jobComparison.message}</p>
          ) : (
            <>
              <p>
                <strong>{jobComparison.origin}:</strong> {jobComparison.origin_salary.amount} –{" "}
                <em>{jobComparison.origin_salary.description}</em>
              </p>
              <p>
                <strong>{jobComparison.destination}:</strong> {jobComparison.destination_salary.amount} –{" "}
                <em>{jobComparison.destination_salary.description}</em>
              </p>
              <p>
                <strong>Summary:</strong> {jobComparison.summary}
              </p>
            </>
          )}
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
