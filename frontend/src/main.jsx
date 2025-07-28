import React from "react";
import ReactDOM from "react-dom/client";
import { createRoot } from "react-dom/client";
import { StrictMode } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import InputPage from "./pages/InputPage";
import Results from "./pages/Results";
import History from "./pages/History";
import Header from "./components/Header";
import "./styles/index.css";
import SignIn from "./components/SignIn.jsx";
import SignUp from "./components/Signup.jsx";
import { AuthContextProvider } from "./context/AuthContext.jsx";
import PrivateRoute from "./components/PrivateRoute.jsx";


createRoot(document.getElementById("root")).render(
  <StrictMode>
    <AuthContextProvider>
      <BrowserRouter>
        <Routes>
          <Route
            path="/"
            element={
              <PrivateRoute>
                <Home />
              </PrivateRoute>
            }
          >
            <Route index={true} element={<Header />} />
          </Route>

          <Route
            path="/input"
            element={
              <PrivateRoute>
                <InputPage />
              </PrivateRoute>
            }
          >
            <Route index={true} element={<Header />} />
          </Route>

          <Route
            path="/results"
            element={
              <PrivateRoute>
                <Results />
              </PrivateRoute>
            }
          >
            <Route index={true} element={<Header />} />
          </Route>

          <Route
            path="/history"
            element={
              <PrivateRoute>
                <History />
              </PrivateRoute>
            }
          >
            <Route index={true} element={<Header />} />
          </Route>

          <Route path="/signin" element={<SignIn />} />

          <Route path="/signup" element={<SignUp />} />
        </Routes>
      </BrowserRouter>
    </AuthContextProvider>
  </StrictMode>
);
