import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import App from "./App";
import Home from "./pages/Home";
import InputPage from "./pages/InputPage";
import Results from "./pages/Results";
import History from "./pages/History";
import "./styles/index.css"; // make sure this file exists

// Define the routes
const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/input",
        element: <InputPage />,
      },
      {
        path: "/results",
        element: <Results />,
      },
      {
        path: "/history",
        element: <History />,
      },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
