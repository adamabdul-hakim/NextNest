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
        <h2 style={{ marginBottom: "1rem" }}>
          Welcome, <span>{username}</span>!
        </h2>
        <p>
          Welcome to <strong>NextNest</strong>: Explore what life would be like
          in another city — check weather, jobs, and flights instantly.
        </p>
        <button className="start-button" onClick={() => navigate("/dashboard")}>
          Get Started
        </button>
      </div>

      <div className="A">
        <h2>Why choose us</h2>
        <p>..........</p>
      </div>

      <div className="B">
        <h2>SOmething</h2>
        <p>..........</p>
      </div>

      <div className="C">
        <h2>Contact Us</h2>
        <p>Have questions or feedback? We'd love to hear from you.</p>
      </div>

      <footer className="footer">
        <p>&copy; 2025 NextNest. All rights reserved.</p>
      </footer>
    </>
  );
}
