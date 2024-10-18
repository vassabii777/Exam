import { Navigate } from 'react-router-dom';
import PrivateRoute from '../components/PrivateRoute';

// Страницы
import HomePage from '../pages/HomePage/HomePage';
import ProfilePage from '../pages/ProfilePage/ProfilePage';

const routes = [
    {
        path: "/",
        element: (
            <PrivateRoute>
                <HomePage />
            </PrivateRoute>
        ),
    },
    {
        path: "/profile",
        element: (
            <PrivateRoute>
                <ProfilePage />
            </PrivateRoute>
        ),
    },
    {
        path: "*",
        element: <Navigate to="/NotFoundPage" />,
    },
];

export default routes;
