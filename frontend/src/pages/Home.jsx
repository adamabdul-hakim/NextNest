import { useNavigate } from "react-router-dom";
import { useEffect, useRef } from "react";
import { UserAuth } from "../context/AuthContext";
import "../styles/home.css";

export default function Home() {
  const navigate = useNavigate();
  const bgStaticRef = useRef(null);
  const { session } = UserAuth();

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
      <div className="hero-container">
        {/* ✅ Show username if available */}
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
        <button onClick={() => navigate("/input")}>Get Started</button>
      </div>

      <div className="section bg-static" ref={bgStaticRef}>
        <div className="bg-move"></div>
      </div>
      <div className="section"></div>
    </>
  );
}
