import { Navigate } from 'react-router-dom';
import PrivateRoute from '../components/PrivateRoute';

// Страницы
import HomePage from '../pages/HomePage/HomePage';
import ProfilePage from '../pages/ProfilePage/ProfilePage';
import NotFoundPage from '../pages/404/NotFoundPage';

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
        element: (
            <PrivateRoute>
                <NotFoundPage />
            </PrivateRoute>
        )
    },
];

export default routes;
