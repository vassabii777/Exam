import { useSelector } from "react-redux";
import { Navigate } from "react-router-dom";

const PrivateRoute = ({ children }) => {
  const token = useSelector((state) => state.user.token); // Проверяем токен

  return token ? children : <Navigate to="/login" />; // Если токена нет, редиректим на login
};

export default PrivateRoute;