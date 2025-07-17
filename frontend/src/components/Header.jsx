import { Link } from "react-router-dom";

const Header = () => {
  return (
    <>
      <div className="header">
        <h1></h1>
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
