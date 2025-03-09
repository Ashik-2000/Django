// Main dashboard component for logged-in users

import { useState, useEffect } from "react";
import { getAccount, logout } from "../api/api";
import Transactions from "./Transactions";

const Dashboard = ({ onLogout }) => {
    const [account, setAccount] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    const fetchAccountData = async () => {
        try {
            const response = await getAccount();
            setAccount(response.data);
            setError("");
        } catch (err) {
            setError("Failed to fetch account data");
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchAccountData();
    }, []);

    const handleLogout = async () => {
        try {
            await logout();
            onLogout();
        } catch (err) {
            setError("Logout failed");
        }
    };

    if (loading) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h2>Banking Dashboard</h2>
            {error && <p>{error}</p>}

            {account && (
                <div>
                    <h3>Welcome, {account.username}!</h3>
                    <p>Current Balance: ${account.balance}</p>

                    <Transactions onTransaction={fetchAccountData} />

                    <button onClick={handleLogout}>Logout</button>
                </div>
            )}
        </div>
    );
};

export default Dashboard;
