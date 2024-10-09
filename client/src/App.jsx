import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./components/Header/Header";
import routes from "./routes/routes";
import LoginPage from "./pages/AuthPage/AuthPage";
import ProfilePage from "./pages/ProfilePage/ProfilePage";
import HomePage from './pages/HomePage/HomePage';
import Footer from "./components/Footer/Footer";

function App() {
  return (
    <Router>
      <Header />
      <main>
        <Routes>
          <Route path="/Auth" element={<LoginPage />} />
          {/* <Route path="/profile" element={<ProfilePage />} />
          <Route path="/" element={<HomePage />} /> */}
          {routes.map((route, index) => (
            <Route key={index} path={route.path} element={route.element} />
          ))}
        </Routes>
      </main>
      <Footer />
    </Router>
  );
}

export default App;