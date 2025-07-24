import { useState } from "react";
import { Link, Navigate, useNavigate } from "react-router-dom";
import { UserAuth } from "../context/AuthContext";

const SignUp = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState("");

    const {session, signUpNewUser} = UserAuth()
    const navigate = useNavigate()

    const handleSignUp = async (e) =>
    {
        e.preventDefault()
        setLoading(true)
        try {
            const result = await signUpNewUser(email, password)

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
            <form onSubmit={handleSignUp} className="signup-container">
                <h1>Eco Hub</h1>
                <h2> Sign up today!</h2>
                <p>
                   Already have an account? <Link to={"/signin"} className="signup-link">Sign in!</Link>
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
                  Sign up
                </button>
                {error && <p>{error}</p>}
            </form>
        </div>
    )
}

export default SignUp;
