// Main application component
import { useState, useEffect } from "react";
import Login from "./components/Login";
import Register from "./components/Register";
import Dashboard from "./components/Dashboard";
import { getAccount } from "./api/api";

function App() {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [showRegister, setShowRegister] = useState(false);
    const [loading, setLoading] = useState(true);

    // Check if user is already logged in
    useEffect(() => {
        const checkLoginStatus = async () => {
            try {
                await getAccount();
                setIsLoggedIn(true);
            } catch (err) {
                setIsLoggedIn(false);
            } finally {
                setLoading(false);
            }
        };

        checkLoginStatus();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>Simple Banking System</h1>

            {isLoggedIn ? (
                <Dashboard onLogout={() => setIsLoggedIn(false)} />
            ) : (
                <div>
                    {showRegister ? (
                        <>
                            <Register
                                onRegisterSuccess={() => setShowRegister(false)}
                            />
                            <p>
                                Already have an account?{" "}
                                <button onClick={() => setShowRegister(false)}>
                                    Login
                                </button>
                            </p>
                        </>
                    ) : (
                        <>
                            <Login onLoginSuccess={() => setIsLoggedIn(true)} />
                            <p>
                                Don't have an account?{" "}
                                <button onClick={() => setShowRegister(true)}>
                                    Register
                                </button>
                            </p>
                        </>
                    )}
                </div>
            )}
        </div>
    );
}

export default App;
