import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { UserAuth } from "../context/AuthContext";

const SignIn = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const { signInUser, signInAsGuest } = UserAuth(); // ✅ include signInAsGuest
  const navigate = useNavigate();

  const handleSignIn = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const result = await signInUser(email, password);
      if (result.success) {
        navigate("/dashboard");
      }
    } catch {
      setError("An error occurred");
    } finally {
      setLoading(false);
    }
  };

  // ✅ handle guest
  const handleGuest = () => {
    signInAsGuest();
    navigate("/dashboard");
  };

  return (
    <div>
      <form onSubmit={handleSignIn} className="signin-container">
        <h1>Eco Hub</h1>
        <h2>Sign in today!</h2>
        <p>
          Don't have an account?{" "}
          <Link to={"/signup"} className="signup-link">
            Sign up!
          </Link>
        </p>

        <input
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
          type="email"
        />
        <input
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Password"
          type="password"
        />
        <button type="submit" disabled={loading}>
          Sign in
        </button>
        {error && <p>{error}</p>}

        {/* ✅ Continue as guest */}
        <button
          type="button"
          onClick={handleGuest}
          style={{ marginTop: "1rem" }}
        >
          Continue as Guest
        </button>
      </form>
    </div>
  );
};

export default SignIn;
