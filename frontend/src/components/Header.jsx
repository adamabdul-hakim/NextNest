import { Link } from "react-router-dom";
import "../styles/header.css";

const Header = () => {
  return (
    <>
      <div className="header">
        <h1 className="logo">NextNest</h1>
        <div className="header-links">
          <Link to={"/"}>
            <p>Home</p>
          </Link>
          <Link to={"/history"}>
            <p>History</p>
          </Link>
        </div>
      </div>
    </>
  );
};

export default Header;
