import React from "react";
import ReactDOM from "react-dom/client";
import { createRoot } from 'react-dom/client'
import { StrictMode } from 'react'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import InputPage from "./pages/InputPage";
import Results from "./pages/Results";
import History from "./pages/History";
import Header from "./components/Header";
import "./styles/index.css"; // make sure this file exists


createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<Home />}>
          <Route index={true} element={<Header/>} />
        </Route>

        <Route path="/input" element={ <InputPage />}>
        <Route index={true} element={<Header/>} />
        </Route>

        <Route path="/results" element={<Results />}>
          <Route index={true} element={<Header/>} />
        </Route>

        <Route path="/history" element={ <History />}>
          <Route index={true} element={<Header/>} />
        </Route>
      </Routes>
    </BrowserRouter>
  </StrictMode>,
)