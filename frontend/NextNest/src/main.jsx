import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { StrictMode } from 'react';
import App from './App.jsx';
import InputForm from './InputForm.jsx'


ReactDOM.createRoot(document.getElementById('root')).render(
  <StrictMode>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<App />}/>
          <Route path="/InputForm" element={<InputForm />}/>
        </Routes>
      </BrowserRouter>
  </StrictMode>
);