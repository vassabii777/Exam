// import axios from "axios";

const authEndpoint = "https://accounts.spotify.com/authorize?";
const clientId = "10ff71b2181a4ee19909431870ef03f4";
const redirectUri = "http://localhost:3000";
const scopes = ["user-library-read", "playlist-read-private"];

export const loginEndpoint = `${authEndpoint}client_id=${clientId}&redirect_uri=${redirectUri}&scope=${scopes.join(
  "%20"
)}&response_type=token&show_dialog=true`;


// const apiClient = axios.create({
//   // baseURL: "https://api.spotify.com/v1/",
//   baseURL: `http://172.20.10.3:8000/api/v1/`,
// });

export const setClientToken = (token) => {
  apiClient.interceptors.request.use(async function (config) {
    config.headers.Authorization = "Bearer " + token;
    return config;
  });
};

// export default apiClient;

import axios from "axios";
// import Cookies from "js-cookie";

const apiClient = axios.create({
  // baseURL: `http://127.0.0.1:8000/api/v1/`,
  baseURL: `http://172.28.0.155:8000/api/v1/`,
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${localStorage.getItem("token")}`,
  },
});



export default apiClient;