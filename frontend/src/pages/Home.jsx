import { useNavigate } from "react-router-dom";
import { useEffect, useRef } from "react";
import { UserAuth } from "../context/AuthContext";
import "../styles/home.css";
import { Link } from "react-router-dom";

export default function Home() {
  const navigate = useNavigate();
  const { session, signOut } = UserAuth();

  const bgStaticRef = useRef(null);

  useEffect(() => {
    function handleScroll() {
      if (!bgStaticRef.current) return;

      const windowTop = window.scrollY || window.pageYOffset;
      const elementTop =
        bgStaticRef.current.getBoundingClientRect().top + windowTop;

      const leftPosition = windowTop - elementTop;

      const bgMove = bgStaticRef.current.querySelector(".bg-move");
      if (bgMove) {
        bgMove.style.left = `${leftPosition * 0.8}px`;
      }
    }

    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const username = session?.user?.user_metadata?.username || "User";

  return (
    <>
      <div
        className="navbar"
        style={{ display: "flex", justifyContent: "flex-end", padding: "1rem" }}
      >
        {!session?.user ? (
          <Link to="/signin">
            <button style={{ padding: "0.5rem 1rem" }}>Sign In</button>
          </Link>
        ) : (
          <button onClick={signOut} style={{ padding: "0.5rem 1rem" }}>
            Sign Out
          </button>
        )}
      </div>

      <div className="hero-container" ref={bgStaticRef}>
        <div className="bg-move"></div>
        <h2 className="fade-in" style={{ marginBottom: "1rem" }}>
          Welcome to NextNest, <span>{username}</span>!
        </h2>
        <p className="fade-in fade-in-delay">
          Welcome to <strong>NextNest</strong>: Explore what life would be like
          in another city — check weather, jobs, and flights instantly.
        </p>
        <button
          className="start-button fade-in fade-in-delay"
          onClick={() => navigate("/dashboard")}
          style={{ animationDelay: "0.6s" }}
        >
          Get Started
        </button>
      </div>

      <div className="flippable-cards-container">
        <div className="flip-card">
          <div className="flip-card-inner">
            <div className="flip-card-front">Why choose us?</div>
            <div className="flip-card-back">Back 1</div>
          </div>
        </div>

        <div className="flip-card">
          <div className="flip-card-inner">
            <div className="flip-card-front">How do we get our data?</div>
            <div className="flip-card-back">Back 2</div>
          </div>
        </div>

        <div className="flip-card">
          <div className="flip-card-inner">
            <div className="flip-card-front">Got any feedbacks?</div>
            <div className="flip-card-back">Back 3</div>
          </div>
        </div>
      </div>

      <footer className="footer">
        <p>&copy; 2025 NextNest. All rights reserved.</p>
      </footer>
    </>
  );
}
