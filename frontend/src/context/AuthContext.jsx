import { createContext, useEffect, useState, useContext } from "react";
import { supabase } from "../client";

const AuthContext = createContext();

export const AuthContextProvider = ({ children }) => {
  const [session, setSession] = useState(undefined);
  const [guest, setGuest] = useState(false);

  const signInAsGuest = () => {
    setGuest(true);
    setSession(null);
  };

  // Sign up
  const signUpNewUser = async (email, password, username) => {
    console.log("Attempting sign-up with:", email, username);

    const { data, error } = await supabase.auth.signUp({
      email,
      password,
      options: {
        data: { username },
      },
    });

    if (error) {
      console.error("Sign-up failed:", error.message, error);
      return { success: false, error };
    }

    console.log("Sign-up success:", data);
    return { success: true, data };
  };

  // Sign in
  const signInUser = async (email, password) => {
    try {
      const { data, error } = await supabase.auth.signInWithPassword({
        email: email,
        password: password,
      });
      if (error) {
        console.error("sign in error occurred:", error);
        return { success: false, error: error.message };
      }
      console.log("sign-in success");
      return { success: true, data };
    } catch (error) {
      console.error("An unexpected error occurred during sign-in:", error);
      return { success: false, error: error.message };
    }
  };

  useEffect(() => {
    supabase.auth.getSession().then(({ data: { session } }) => {
      setSession(session);
    });

    supabase.auth.onAuthStateChange((_event, session) => {
      setSession(session);
    });
  }, []);

  // Sign Out
  const signOut = () => {
    const { error } = supabase.auth.signOut();
    if (error) {
      console.error("there was an error");
    }
    setGuest(false);
  };

  return (
    <AuthContext.Provider
      value={{
        session,
        guest,
        signInAsGuest,
        signUpNewUser,
        signInUser,
        signOut,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const UserAuth = () => {
  return useContext(AuthContext);
};
