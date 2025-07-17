import { Outlet } from "react-router-dom";
import "./App.css";

function App() {
  return (
    <div className="app">
      {/* <Header /> could go here later */}
      <Outlet /> {/* This is where Home, InputPage, etc. will render */}
    </div>
  );
}

export default App;
