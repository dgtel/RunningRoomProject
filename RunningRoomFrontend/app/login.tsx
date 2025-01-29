// // // import React, { useState } from "react";
// // // import { View, Text, TextInput, Button, StyleSheet,Alert } from "react-native";
// // // import { useRouter } from "expo-router";
// // // import API from "../app/src/config/axiosConfig";

// // // export default function Login() {
// // //   const [username, setUsername] = useState("");
// // //   const [password, setPassword] = useState("");
// // //   const router = useRouter();

// // //   const handleLogin = () => {
// // //     if (username === "admin") {
// // //       router.push("/admin-dashboard");
// // //     } else if (username === "crew") {
// // //       router.push("/crew-dashboard");
// // //     } else if (username === "caretaker") {
// // //       router.push("/care-taker-dashboard");
// // //     } else if (username === "contractor") {
// // //       router.push("/contractor-dashboard");
// // //     } else {
// // //       alert("Invalid username!");
// // //     }
// // //   };

// // //   return (
// // //     <View style={styles.container}>
// // //       <Text style={styles.header}>Login</Text>
// // //       <TextInput
// // //         style={styles.input}
// // //         placeholder="Username"
// // //         value={username}
// // //         onChangeText={setUsername}
// // //       />
// // //       <TextInput
// // //         style={styles.input}
// // //         placeholder="Password"
// // //         secureTextEntry
// // //         value={password}
// // //         onChangeText={setPassword}
// // //       />
// // //       <Button title="Login" onPress={handleLogin} />
// // //     </View>
// // //   );
// // // }

// // // const styles = StyleSheet.create({
// // //   container: {
// // //     flex: 1,
// // //     justifyContent: "center",
// // //     alignItems: "center",
// // //     padding: 16,
// // //   },
// // //   header: {
// // //     fontSize: 24,
// // //     marginBottom: 16,
// // //   },
// // //   input: {
// // //     width: "80%",
// // //     padding: 8,
// // //     marginBottom: 16,
// // //     borderWidth: 1,
// // //     borderColor: "#ccc",
// // //     borderRadius: 4,
// // //   },
// // // });

// // import React, { useState } from "react";
// // import { View, Text, TextInput, Button, StyleSheet, Alert } from "react-native";
// // import { useRouter } from "expo-router";
// // import API from "../app/src/config/axiosConfig";

// // export default function Login() {
// //   const [username, setUsername] = useState("");
// //   const [password, setPassword] = useState("");
// //   const router = useRouter();

// //   // const handleLogin = async () => {
// //   //   try {
// //   //     const response = await API.post("/login/", { username, password });

// //   //     if (response.data.success) {
// //   //       const { role } = response.data;

// //   //       // Role-based redirection
// //   //       if (role === "admin") {
// //   //         router.push("/admin-dashboard");
// //   //       } else if (role === "crew") {
// //   //         router.push("/crew-dashboard");
// //   //       } else if (role === "crew_controller") {
// //   //         router.push("/crew-controller-dashboard");
// //   //       } else if (role === "caretaker") {
// //   //         router.push("/care-taker-dashboard");
// //   //       } else if (role === "contractor") {
// //   //         router.push("/contractor-dashboard");
// //   //       } else {
// //   //         router.push("/profile");
// //   //       }
// //   //     } else {
// //   //       Alert.alert("Login Failed", response.data.error || "Invalid credentials");
// //   //     }
// //   //   } catch (error) {
// //   //     console.error("Login error:", error);
// //   //     Alert.alert("Error", "Unable to log in. Please try again.");
// //   //   }
// //   // };

// //   import AsyncStorage from "@react-native-async-storage/async-storage";

// // const handleLogin = async () => {
// //   try {
// //     const response = await API.post("/login/", { username, password });
// //     if (response.data.success) {
// //       const { access, role } = response.data;
// //       await AsyncStorage.setItem("access_token", access); // Store token
// //       router.push(getRouteByRole(role)); // Redirect based on role
// //     }
// //   } catch (error) {
// //     console.error("Login error:", error);
// //   }
// // };

// // const getRouteByRole = (role) => {
// //   switch (role) {
// //     case "admin":
// //       return "/admin-dashboard";
// //     case "crew":
// //       return "/crew-dashboard";
// //     case "crew_controller":
// //       return "/crew-controller-dashboard";
// //     case "caretaker":
// //       return "/care-taker-dashboard";
// //     case "contractor":
// //       return "/contractor-dashboard";
// //     default:
// //       return "/profile";
// //   }
// // };

// //   return (
// //     <View style={styles.container}>
// //       <Text style={styles.header}>Login</Text>
// //       <TextInput
// //         style={styles.input}
// //         placeholder="Username"
// //         value={username}
// //         onChangeText={setUsername}
// //       />
// //       <TextInput
// //         style={styles.input}
// //         placeholder="Password"
// //         secureTextEntry
// //         value={password}
// //         onChangeText={setPassword}
// //       />
// //       <Button title="Login" onPress={handleLogin} />
// //     </View>
// //   );
// // }

// // const styles = StyleSheet.create({
// //   container: {
// //     flex: 1,
// //     justifyContent: "center",
// //     alignItems: "center",
// //     padding: 16,
// //   },
// //   header: {
// //     fontSize: 24,
// //     marginBottom: 16,
// //   },
// //   input: {
// //     width: "80%",
// //     padding: 8,
// //     marginBottom: 16,
// //     borderWidth: 1,
// //     borderColor: "#ccc",
// //     borderRadius: 4,
// //   },
// // });

// import React, { useState } from "react";
// import { View, Text, TextInput, Button, StyleSheet, Alert } from "react-native";
// import { useRouter } from "expo-router";
// import AsyncStorage from "@react-native-async-storage/async-storage";
// import API from "../app/src/config/axiosConfig";

// export default function Login() {
//   const [username, setUsername] = useState("");
//   const [password, setPassword] = useState("");
//   const router = useRouter();

//   const handleLogin = async () => {
//     try {
//       const response = await API.post("/login/", { username, password });

//       if (response.data.success) {
//         const { access, role } = response.data;

//         // Store the access token in AsyncStorage
//         await AsyncStorage.setItem("access_token", access);

//         // Redirect to role-based dashboards
//         router.push(getRouteByRole(role));
//       } else {
//         Alert.alert("Login Failed", response.data.error || "Invalid credentials");
//       }
//     } catch (error) {
//       console.error("Login error:", error);
//       Alert.alert("Error", "Unable to log in. Please try again.");
//     }
//   };

//   const getRouteByRole = (role: string): string => {
//     switch (role) {
//       case "admin":
//         return "/admin-dashboard";
//       case "crew":
//         return "/crew-dashboard";
//       case "crew_controller":
//         return "/crew-controller-dashboard";
//       case "caretaker":
//         return "/care-taker-dashboard";
//       case "contractor":
//         return "/contractor-dashboard";
//       default:
//         return "/profile";
//     }
//   };

//   return (
//     <View style={styles.container}>
//       <Text style={styles.header}>Login</Text>
//       <TextInput
//         style={styles.input}
//         placeholder="Username"
//         value={username}
//         onChangeText={setUsername}
//       />
//       <TextInput
//         style={styles.input}
//         placeholder="Password"
//         secureTextEntry
//         value={password}
//         onChangeText={setPassword}
//       />
//       <Button title="Login" onPress={handleLogin} />
//     </View>
//   );
// }

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     justifyContent: "center",
//     alignItems: "center",
//     padding: 16,
//   },
//   header: {
//     fontSize: 24,
//     marginBottom: 16,
//   },
//   input: {
//     width: "80%",
//     padding: 8,
//     marginBottom: 16,
//     borderWidth: 1,
//     borderColor: "#ccc",
//     borderRadius: 4,
//   },
// });

import React, { useState } from "react";
import { View, Text, TextInput, Button, StyleSheet, Alert } from "react-native";
import { useRouter } from "expo-router";
import AsyncStorage from "@react-native-async-storage/async-storage";
import API from "../app/src/config/axiosConfig";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter();

  const getRouteByRole = (role: string): 
    | "/admin-dashboard"
    | "/crew-dashboard"
    | "/crew-controller-dashboard"
    | "/care-taker-dashboard"
    | "/contractor-dashboard"
    | "/profile" => {
    switch (role) {
      case "admin":
        return "/admin-dashboard";
      case "crew":
        return "/crew-dashboard";
      case "crew_controller":
        return "/crew-controller-dashboard";
      case "caretaker":
        return "/care-taker-dashboard";
      case "contractor":
        return "/contractor-dashboard";
      default:
        return "/profile";
    }
  };

  const handleLogin = async () => {
    try {
      const response = await API.post("/login/", { username, password });

      if (response.data.success) {
        const { access, role } = response.data;

        // Store the access token in AsyncStorage
        await AsyncStorage.setItem("access_token", access);

        // Redirect to role-based dashboards
        router.push(getRouteByRole(role));
      } else {
        Alert.alert("Login Failed", response.data.error || "Invalid credentials");
      }
    } catch (error) {
      console.error("Login error:", error);
      Alert.alert("Error", "Unable to log in. Please try again.");
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Login</Text>
      <TextInput
        style={styles.input}
        placeholder="Username"
        value={username}
        onChangeText={setUsername}
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />
      <Button title="Login" onPress={handleLogin} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    padding: 16,
  },
  header: {
    fontSize: 24,
    marginBottom: 16,
  },
  input: {
    width: "80%",
    padding: 8,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 4,
  },
});
