// Component for deposit and withdrawal transactions

import { useState } from "react";
import { deposit, withdraw } from "../api/api";

const Transactions = ({ onTransaction }) => {
    const [amount, setAmount] = useState("");
    const [error, setError] = useState("");
    const [message, setMessage] = useState("");

    const handleDeposit = async (e) => {
        e.preventDefault();
        setError("");
        setMessage("");

        try {
            // Make sure the amount is a number
            const numAmount = parseFloat(amount);
            if (isNaN(numAmount) || numAmount <= 0) {
                setError("Please enter a valid positive amount");
                return;
            }
            // This should call the deposit API endpoint
            const response = await deposit(numAmount);
            setMessage(response.data.message);
            setAmount("");
            onTransaction();
        } catch (err) {
            console.error("Deposit error:", err); // Add this for debugging
            setError(err.response?.data?.error || "Deposit failed");
        }
    };

    const handleWithdraw = async (e) => {
        e.preventDefault();
        setError("");
        setMessage("");

        try {
            const response = await withdraw(parseFloat(amount));
            setMessage(response.data.message);
            setAmount("");
            onTransaction();
        } catch (err) {
            setError(err.response?.data?.error || "Withdrawal failed");
        }
    };

    return (
        <div>
            <h3>Transactions</h3>
            {error && <p>{error}</p>}
            {message && <p>{message}</p>}
            <form>
                <div>
                    <label>Amount ($):</label>
                    <input
                        type="number"
                        step="0.01"
                        min="0.01"
                        value={amount}
                        onChange={(e) => setAmount(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <button onClick={handleDeposit}>Deposit</button>
                    <button onClick={handleWithdraw}>Withdraw</button>
                </div>
            </form>
        </div>
    );
};

export default Transactions;
