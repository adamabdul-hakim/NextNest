import { useState } from "react";
import { Link, Navigate, useNavigate } from "react-router-dom";
import { UserAuth } from "../context/AuthContext";

const SignIn = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState("");

    const {session, signInUser} = UserAuth()
    const navigate = useNavigate()
    const handleSignIn = async (e) =>
    {
        e.preventDefault()
        setLoading(true)
        try {
            const result = await signInUser(email, password)

            if(result.success) {
                navigate("/")
            }

        }
        catch (err){
            setError("an error occurred")
        }
        finally{
            setLoading(false)
        }
    }

    return (
        <div>
            <form onSubmit={handleSignIn} className="signin-container">
                <h1>Eco Hub</h1>
                <h2> Sign in today!</h2>
                <p>
                   Don't have an account? <Link to={"/signup"} className="signup-link">Sign up!</Link>
                </p>

                <input 
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Email" 
                type="email" 
                />
                <input 
                onChange={(e)=> setPassword(e.target.value)} 
                placeholder="Password"
                type="password"
                />
                <button type="submit" disabled={loading}>
                  Sign in
                </button>
                {error && <p>{error}</p>}
            </form>
        </div>
    )
}

export default SignIn;
