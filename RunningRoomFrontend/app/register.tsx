// import React, { useState, useEffect } from "react";
// import { View, Text, TextInput, Button, StyleSheet, Alert } from "react-native";
// import { useRouter } from "expo-router";
// import API from "../app/src/config/axiosConfig";
// import { Picker } from "@react-native-picker/picker"; // ✅ Import Picker from the correct package



// export default function Register() {
//   const [username, setUsername] = useState("");
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState("");
//   const [confirmPassword, setConfirmPassword] = useState("");
//   // const [role, setRole] = useState(""); // Role selection
//   const [role, setRole] = useState<string>("");  // Role Selection

//   // const [lobbyId, setLobbyId] = useState(""); // Lobby selection
//   // const [lobbies, setLobbies] = useState([]); // List of available lobbies
//   const [lobbyId, setLobbyId] = useState<number | "">("");

//   const [lobbies, setLobbies] = useState<{ id: number; name: string }[]>([]);

//   const router = useRouter();


//   // Fetch Lobbies on Component Mount
//   useEffect(() => {
//     const fetchLobbies = async () => {
//       try {
//         const response = await API.get("/lobbies/");
//         setLobbies(response.data);
//       } catch (error) {
//         console.error("Error fetching lobbies:", error);
//       }
//     };
//     fetchLobbies();
//   }, []);

//   const handleRegister = async () => {
//     if (password !== confirmPassword) {
//       Alert.alert("Error", "Passwords do not match!");
//       return;
//     }

//     try {
//       const response = await API.post("/register/", {
//         username,
//         email,
//         password,
//         role,
//         lobby_id: lobbyId || null, // Assign lobby if applicable
//       });

//       if (response.data.success) {
//         Alert.alert("Success", "Registration successful! Please log in.");
//         router.push("/login");
//       } else {
//         Alert.alert("Registration Failed", response.data.error);
//       }
//     } catch (error) {
//       console.error("Registration error:", error);
//       Alert.alert("Error", "Unable to register. Please try again.");
//     }
//   };

//   return (
//     <View style={styles.container}>
//       <Text style={styles.header}>Register</Text>
//       <TextInput
//         style={styles.input}
//         placeholder="Username"
//         value={username}
//         onChangeText={setUsername}
//       />
//       <TextInput
//         style={styles.input}
//         placeholder="Email"
//         value={email}
//         onChangeText={setEmail}
//         keyboardType="email-address"
//       />
//       <TextInput
//         style={styles.input}
//         placeholder="Password"
//         secureTextEntry
//         value={password}
//         onChangeText={setPassword}
//       />
//       <TextInput
//         style={styles.input}
//         placeholder="Confirm Password"
//         secureTextEntry
//         value={confirmPassword}
//         onChangeText={setConfirmPassword}
//       />
//       <TextInput
//         style={styles.input}
//         placeholder="Role (admin, crew, caretaker, contractor)"
//         value={role}
//         onChangeText={setRole}
//       />

//       {/* Dropdown for Lobby Selection */}
//       {(role === "Crew Member" || role === "Crew Controller" || role === "Caretaker") && (
//         <Picker
//           selectedValue={lobbyId}
//           style={styles.input}
//           onValueChange={(itemValue) => setLobbyId(itemValue)}
//         >
//           <Picker.Item label="Select Lobby" value="" />
//           {lobbies.map((lobby) => (
//             <Picker.Item key={lobby.id} label={lobby.name} value={lobby.id} />
//           ))}
//         </Picker>
//       )}

//       <Button title="Register" onPress={handleRegister} />
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


import React, { useState, useEffect } from "react";
import { View, Text, TextInput, Button, StyleSheet, Alert } from "react-native";
import { useRouter } from "expo-router";
import API from "../app/src/config/axiosConfig";
import { Picker } from "@react-native-picker/picker"; // ✅ Import Picker from the correct package

export default function Register() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [role, setRole] = useState<string>(""); // ✅ Fixed Role Selection
  const [lobbyId, setLobbyId] = useState<number | "">(""); // ✅ Fixed Lobby Selection

  const [lobbies, setLobbies] = useState<{ id: number; name: string }[]>([]);
  const router = useRouter();

  // Allowed roles dropdown (Users should NOT type their role manually)
  const allowedRoles = [
    { label: "Crew Member", value: "Crew Member" },
    { label: "Crew Controller", value: "Crew Controller" },
    { label: "Caretaker", value: "Caretaker" },
    { label: "Contractor", value: "Contractor" },
  ];

  // Fetch Lobbies on Component Mount
  useEffect(() => {
    const fetchLobbies = async () => {
      try {
        const response = await API.get("/lobbies/");
        setLobbies(response.data);
      } catch (error) {
        console.error("Error fetching lobbies:", error);
      }
    };
    fetchLobbies();
  }, []);

  const handleRegister = async () => {
    if (password !== confirmPassword) {
      Alert.alert("Error", "Passwords do not match!");
      return;
    }

    try {
      const response = await API.post("/register/", {
        username,
        email,
        password,
        role,
        lobby_id: lobbyId || null, // Assign lobby if applicable
      });

      if (response.data.success) {
        Alert.alert("Success", "Registration successful! Please log in.");
        router.push("/login");
      } else {
        Alert.alert("Registration Failed", response.data.error);
      }
    } catch (error) {
      console.error("Registration error:", error);
      Alert.alert("Error", "Unable to register. Please try again.");
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Register</Text>

      <TextInput
        style={styles.input}
        placeholder="Username"
        value={username}
        onChangeText={setUsername}
      />
      <TextInput
        style={styles.input}
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
        keyboardType="email-address"
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />
      <TextInput
        style={styles.input}
        placeholder="Confirm Password"
        secureTextEntry
        value={confirmPassword}
        onChangeText={setConfirmPassword}
      />

      {/* ✅ Fixed Dropdown for Role Selection */}
      <Picker selectedValue={role} onValueChange={(itemValue) => setRole(itemValue)} style={styles.input}>
        <Picker.Item label="Select Role" value="" />
        {allowedRoles.map((roleOption) => (
          <Picker.Item key={roleOption.value} label={roleOption.label} value={roleOption.value} />
        ))}
      </Picker>

      {/* ✅ Fixed Dropdown for Lobby Selection */}
      {(role === "Crew Member" || role === "Crew Controller" || role === "Caretaker") && (
        <Picker selectedValue={lobbyId} onValueChange={(itemValue) => setLobbyId(itemValue)} style={styles.input}>
          <Picker.Item label="Select Lobby" value="" />
          {lobbies.map((lobby) => (
            <Picker.Item key={lobby.id} label={lobby.name} value={lobby.id} />
          ))}
        </Picker>
      )}

      <Button title="Register" onPress={handleRegister} />
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

