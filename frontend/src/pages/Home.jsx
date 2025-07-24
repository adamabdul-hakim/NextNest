import { useNavigate } from "react-router-dom";
import "../styles/home.css";

export default function Home() {
  const navigate = useNavigate();

  return (
    <div className="hero-container">
      <h1>
        Welcome to <span>NextNest</span>
      </h1>
      <p>
        Explore what life would be like in another city — check weather, jobs,
        and flights instantly.
      </p>
      <button onClick={() => navigate("/input")}>Get Started</button>
    </div>
  );
}
