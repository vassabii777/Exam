import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import routes from "./routes/routes";
import Layout from "./components/Layout/Layout";

// Страницы
import LoginPage from "./pages/AuthPage/LoginPage";
import RegisterPage from "./pages/AuthPage/RegisterPage";
import ProfilePage from "./pages/ProfilePage/ProfilePage";
import HomePage from './pages/HomePage/HomePage';
import NotFoundPage from "./pages/404/NotFoundPage";

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          {/* Статические маршруты */}
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="/" element={<HomePage />} />

          {/* Перенаправление на NotFoundPage */}
          {/* <Route path="*" element={<NotFoundPage />} /> */}
          {/* Динамические приватные маршруты */}
          {routes.map((route, index) => (
            <Route key={index} path={route.path} element={route.element} />
          ))}
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
