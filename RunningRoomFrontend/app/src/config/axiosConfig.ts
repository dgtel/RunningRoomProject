// // import axios from "axios";

// // const API = axios.create({
// //   baseURL: "http://127.0.0.1:8000/api/", // Replace with your actual backend URL
// // });

// // const API = axios.create({
// //   baseURL: process.env.REACT_APP_API_BASE_URL || "http://127.0.0.1:8000/api/",
// // });


// // // Add token to headers for authenticated requests
// // API.interceptors.request.use((config) => {
// //   const token = ""; // Replace with token handling logic (e.g., AsyncStorage or state)
// //   if (token) {
// //     config.headers.Authorization = `Bearer ${token}`;
// //   }
// //   return config;
// // });

// // export default API;

// import axios from "axios";
// import AsyncStorage from "@react-native-async-storage/async-storage";

// const API = axios.create({
//   baseURL: process.env.REACT_APP_API_BASE_URL || "http://127.0.0.1:8000/api/" || "http://192.168.1.100:8000/api/"
// });

// // Add token to headers for authenticated requests
// API.interceptors.request.use(async (config) => {
//   const token = await AsyncStorage.getItem("access_token");
//   if (token) {
//     config.headers.Authorization = `Bearer ${token}`;
//   }
//   return config;
// });

// export default API;
import axios from "axios";
import AsyncStorage from "@react-native-async-storage/async-storage";

// Get the IPv4 address manually
const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || "http://192.168.39.216:8000/api/";

const API = axios.create({
  baseURL: API_BASE_URL,
});

// Add token to headers for authenticated requests
API.interceptors.request.use(async (config) => {
  const token = await AsyncStorage.getItem("access_token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default API;
