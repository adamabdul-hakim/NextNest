import { useNavigate } from "react-router-dom";

export default function Home() {
  const navigate = useNavigate();

  const handleStart = () => {
    navigate("/input");
  };

  return (
    <div className="home-container">
      <h1 className="home-title">
        Welcome to <span className="highlight">NextNest</span>
      </h1>
      <p className="home-subtitle">
        Explore what life would be like in another city — check weather, jobs,
        and flights instantly.
      </p>
      <button className="start-button" onClick={handleStart}>
        Get Started
      </button>
    </div>
  );
}
