import { UserAuth } from "../context/AuthContext";
import { Navigate } from "react-router-dom";

const PrivateRoute = ({ children }) => {
  const { session, guest } = UserAuth();

  if (session === undefined) {
    return null;
  }

  if (session || guest) {
    return <>{children}</>;
  }

  return <Navigate to="/signin" />;
};

export default PrivateRoute;
