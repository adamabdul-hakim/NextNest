import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { UserAuth } from "../context/AuthContext";
import "../styles/signup.css";

const SignUp = () => {
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const { signUpNewUser } = UserAuth();
  const navigate = useNavigate();

  const handleSignUp = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    // Simple validation
    if (!email || !password || !username) {
      setError("Please enter email, username, and password.");
      setLoading(false);
      return;
    }

    if (password.length < 6) {
      setError("Password must be at least 6 characters.");
      setLoading(false);
      return;
    }

    try {
      const result = await signUpNewUser(
        email.trim(),
        password,
        username.trim()
      );
      if (result.success) {
        navigate("/");
      } else {
        setError(result.error.message || "Sign-up failed.");
      }
    } catch (err) {
      console.error("Unexpected error during sign-up:", err);
      setError("An unexpected error occurred. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="signup-wrapper">
      <form onSubmit={handleSignUp} className="signup-container">
        <h1>Eco Hub</h1>
        <h2>Sign up today!</h2>
        <p>
          Already have an account?{" "}
          <Link to="/signin" className="signup-link">
            Sign in!
          </Link>
        </p>

        <input
          type="email"
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
          value={email}
        />
        <input
          type="text"
          placeholder="Username"
          onChange={(e) => setUsername(e.target.value)}
          value={username}
        />
        <input
          type="password"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
          value={password}
        />
        <button type="submit" disabled={loading}>
          {loading ? "Signing up..." : "Sign up"}
        </button>

        {error && <p className="error-message">{error}</p>}
      </form>
    </div>
  );
};

export default SignUp;