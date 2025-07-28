import { useNavigate } from "react-router-dom";
import { useEffect, useRef } from "react";
import { UserAuth } from "../context/AuthContext";
import "../styles/home.css";
import { Link } from "react-router-dom";

export default function Home() {
  const navigate = useNavigate();
  const bgStaticRef = useRef(null);
  const { session, signOut } = UserAuth(); // ← Grab signOut

  useEffect(() => {
    function handleScroll() {
      if (!bgStaticRef.current) return;

      const windowTop = window.scrollY || window.pageYOffset;
      const elementTop =
        bgStaticRef.current.getBoundingClientRect().top + windowTop;
      const leftPosition = windowTop - elementTop;

      const bgMove = bgStaticRef.current.querySelector(".bg-move");
      if (bgMove) {
        bgMove.style.left = `${leftPosition}px`;
      }
    }

    window.addEventListener("load", handleScroll);
    window.addEventListener("resize", handleScroll);
    window.addEventListener("scroll", handleScroll);

    handleScroll(); // set on load

    return () => {
      window.removeEventListener("load", handleScroll);
      window.removeEventListener("resize", handleScroll);
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <>
      <div style={{ display: "flex", justifyContent: "flex-end", padding: "1rem" }}>
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
      <div className="hero-container">
        {session?.user?.user_metadata?.username && (
          <h2 style={{ marginBottom: "1rem" }}>
            Welcome, <span>{session.user.user_metadata.username}</span>!
          </h2>
        )}

        <h1>
          Welcome to <span>NextNest</span>
        </h1>
        <p>
          Explore what life would be like in another city — check weather, jobs,
          and flights instantly.
        </p>
        <button className="start-button" onClick={() => navigate("/dashboard")}>
        Get Started
        </button>
      </div>

      <div className="section bg-static" ref={bgStaticRef}>
        <div className="bg-move"></div>
      </div>
      <div className="section"></div>
    </>
  );
}
