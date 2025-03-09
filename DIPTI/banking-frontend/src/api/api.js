// src/api/api.js
import axios from "axios";

const API_URL = "http://localhost:8000/api/";

// Create axios instance with credentials
const api = axios.create({
    baseURL: API_URL,
    withCredentials: true,
});

// Add a request interceptor to include the CSRF token from cookies
api.interceptors.request.use(
    function (config) {
        // Find the CSRF token in cookies
        const csrfCookie = document.cookie
            .split("; ")
            .find((row) => row.startsWith("csrftoken="));

        if (csrfCookie) {
            const csrfToken = csrfCookie.split("=")[1];
            config.headers["X-CSRFToken"] = csrfToken;
        }

        return config;
    },
    function (error) {
        return Promise.reject(error);
    }
);

// Auth services
export const register = async (username, password) => {
    return await api.post("register/", { username, password });
};

export const login = async (username, password) => {
    // After login, we need to get a CSRF token for subsequent requests
    const response = await api.post("login/", { username, password });
    // Make a simple GET request to ensure we have the CSRF cookie
    await api.get("account/");
    return response;
};

export const logout = async () => {
    return await api.post("logout/");
};

// Account services
export const getAccount = async () => {
    return await api.get("account/");
};

export const deposit = async (amount) => {
    return await api.post("deposit/", { amount });
};

export const withdraw = async (amount) => {
    return await api.post("withdraw/", { amount });
};
