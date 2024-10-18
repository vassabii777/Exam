import axios from "axios";

const axiosInstance = axios.create({
    baseURL: `http://172.20.10.3:8000/`,
    headers: {
        "Content-Type": "application/json",
    },
});


export default axiosInstance;

