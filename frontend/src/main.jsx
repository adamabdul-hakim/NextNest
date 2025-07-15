import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { StrictMode } from 'react';
import App from './App.jsx';
import InputForm from './InputForm.jsx'
import Header from './Header.jsx';


ReactDOM.createRoot(document.getElementById('root')).render(
  <StrictMode>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<App />}>
            <Route index={true} element={<Header />} />
          </Route>
          <Route path="/InputForm" element={<InputForm />}>
            <Route index={true} element={<Header />} />
          </Route>
        </Routes>
      </BrowserRouter>
  </StrictMode>
);