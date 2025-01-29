// // import { View, Text, StyleSheet } from "react-native";

// // export default function Details() {
// //   return (
// //     <View style={styles.container}>
// //       <Text style={styles.text}>This is the Profiles Screen!</Text>
// //     </View>
// //   );
// // }

// // const styles = StyleSheet.create({
// //   container: {
// //     flex: 1,
// //     justifyContent: "center",
// //     alignItems: "center",
// //   },
// //   text: {
// //     fontSize: 20,
// //     color: "#333",
// //   },
// // });

// // import React, { useEffect, useState } from "react";
// // import { View, Text, StyleSheet } from "react-native";
// // import axios from "axios";
// // import API from "../app/src/config/axiosConfig";


// // export default function Profile() {
// //   const [profile, setProfile] = useState(null);

// //   useEffect(() => {
// //     const fetchProfile = async () => {
// //       try {
// //         const token = "your-access-token"; // Replace with your token handling logic
// //         const response = await axios.get("http://<your-backend-url>/api/profile/", {
// //           headers: {
// //             Authorization: `Bearer ${token}`,
// //           },
// //         });
// //         setProfile(response.data);
// //       } catch (error) {
// //         console.error("Error fetching profile:", error);
// //       }
// //     };

// //     fetchProfile();
// //   }, []);

// //   if (!profile) {
// //     return (
// //       <View style={styles.container}>
// //         <Text>Loading...</Text>
// //       </View>
// //     );
// //   }

// //   return (
// //     <View style={styles.container}>
// //       <Text style={styles.header}>Profile Page</Text>
// //       <Text>Username: {profile.username}</Text>
// //       <Text>Email: {profile.email}</Text>
// //       <Text>Role: {profile.role}</Text>
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
// //     fontWeight: "bold",
// //     marginBottom: 16,
// //   },
// // });

// import React, { useEffect, useState } from "react";
// import { View, Text, StyleSheet } from "react-native";
// import API from "../app/src/config/axiosConfig"

// export default function Profile() {
//   const [profile, setProfile] = useState<any>(null); // Use `any` for now; replace with proper types later.

//   useEffect(() => {
//     const fetchProfile = async () => {
//       try {
//         const response = await API.get("/profile/");
//         setProfile(response.data);
//       } catch (error) {
//         console.error("Error fetching profile:", error);
//       }
//     };

//     fetchProfile();
//   }, []);

//   if (!profile) {
//     return (
//       <View style={styles.container}>
//         <Text>Loading...</Text>
//       </View>
//     );
//   }

//   return (
//     <View style={styles.container}>
//       <Text style={styles.header}>Profile Page</Text>
//       <Text>Username: {profile.username}</Text>
//       <Text>Email: {profile.email}</Text>
//       <Text>Role: {profile.role}</Text>
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
//     fontWeight: "bold",
//     marginBottom: 16,
//   },
// });


import React, { useEffect, useState } from "react";
import { View, Text, StyleSheet } from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import API from "../app/src/config/axiosConfig";

export default function Profile() {
  const [profile, setProfile] = useState<any>(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const token = await AsyncStorage.getItem("access_token");
        if (!token) {
          console.error("No token found");
          return;
        }

        const response = await API.get("/profile/", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setProfile(response.data);
      } catch (error) {
        console.error("Error fetching profile:", error);
      }
    };

    fetchProfile();
  }, []);

  if (!profile) {
    return (
      <View style={styles.container}>
        <Text>Loading...</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Profile Page</Text>
      <Text>Username: {profile.username}</Text>
      <Text>Email: {profile.email}</Text>
      <Text>Role: {profile.role}</Text>
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
    fontWeight: "bold",
    marginBottom: 16,
  },
});
