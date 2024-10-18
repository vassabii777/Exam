import React from "react";
import { useLocation } from "react-router-dom";
import Header from "../Header/Header";
import Footer from "../Footer/Footer";
import style from './Layout.module.css';

function Layout({ children }) {
    const location = useLocation();
    const hideHeaderOnPaths = ["/login", "/register", "*"];

    const shouldHideHeader = hideHeaderOnPaths.includes(location.pathname);

    return (
        <>
            {!shouldHideHeader && <Header />}
            <div className={style.pageWrapper}>
                <div className={style.content}>
                    {children}
                </div>
            </div>
            {!shouldHideHeader && <Footer />}
        </>
    );
}

export default Layout;
