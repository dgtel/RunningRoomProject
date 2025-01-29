// // import { Text, View } from "react-native";

// // export default function Index() {
// //   return (
// //     <View
// //       style={{
// //         flex: 1,
// //         justifyContent: "center",
// //         alignItems: "center",
// //       }}
// //     >
// //       <Text>Edit app/index.tsx to edit this screen.</Text>
// //     </View>
// //   );
// // }

// // import React from 'react';
// // import { NavigationContainer } from '@react-navigation/native';
// // import { createNativeStackNavigator } from '@react-navigation/native-stack';
// // import HomeScreen from './src/screens/HomeScreen'; // Adjust path if needed

// // const Stack = createNativeStackNavigator();

// // export default function App() {
// //   return (
// //     <NavigationContainer>
// //       <Stack.Navigator>
// //         <Stack.Screen name="Home" component={HomeScreen} />
// //       </Stack.Navigator>
// //     </NavigationContainer>
// //   );
// // }

// // import React from "react";
// // import { Text, View } from "react-native";

// // export default function Index() {
// //   return (
// //     <View
// //       style={{
// //         flex: 1,
// //         justifyContent: "center",
// //         alignItems: "center",
// //       }}
// //     >
// //       <Text>Welcome to Running Room Project!</Text>
// //     </View>
// //   );
// // }

// // import React from "react";
// // import { createNativeStackNavigator } from "@react-navigation/native-stack";
// // import HomeScreen from "./HomeScreen"

// // const Stack = createNativeStackNavigator();

// // const AppNavigator = () => {
// //   return (
// //     <Stack.Navigator>
// //       <Stack.Screen name="Home" component={HomeScreen} />
// //     </Stack.Navigator>
// //   );
// // };

// // export default AppNavigator;

// // import { Text, View } from "react-native";
// // import { Link } from "expo-router";

// // export default function Index() {
// //   return (
// //     <View
// //       style={{
// //         flex: 1,
// //         justifyContent: "center",
// //         alignItems: "center",
// //       }}
// //     >
// //       <Text>Welcome to the Home Screen!</Text>
// //       <Link href="/details">Go to Details</Link>
// //       <Link href="/details">Go to Profiles</Link>
// //     </View>
// //   );
// // }

// import React from "react";
// import { View, Text, StyleSheet } from "react-native";
// import { Link } from "expo-router";

// export default function Index() {
//   return (
//     <View style={styles.container}>
//       <Text style={styles.header}>Welcome to the Running Room Project!</Text>
//       <Link href="/login">Go to Login</Link>
//       <Link href="/admin-dashboard">Go to Admin Dashboard</Link>
//       <Link href="/crew-dashboard">Go to Crew Dashboard</Link>

//       <Link href="/care-taker-dashboard">Go to care-taker-dashboard</Link>
//       <Link href="/contractor-dashboard">Go to contractor-dashboard</Link>
//       <Link href="/crew-controller-dashboard">Go to crew-controller-dashboard</Link>
      

//     </View>
//   );
// }

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     justifyContent: "center",
//     alignItems: "center",
//   },
//   header: {
//     fontSize: 24,
//     fontWeight: "bold",
//   },
// });



// import React from "react";
// import { View, Text, StyleSheet } from "react-native";
// import { Link } from "expo-router";

// export default function Index() {
//   return (
//     <View style={styles.container}>
//       <Text style={styles.header}>Welcome to the Running Room Project!</Text>
//       <Link href="/login">Go to Login</Link>
//     </View>
//   );
// }

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     justifyContent: "center",
//     alignItems: "center",
//   },
//   header: {
//     fontSize: 24,
//     fontWeight: "bold",
//   },
// });

import React from "react";
import { View, Text, StyleSheet } from "react-native";
import { Link } from "expo-router";

export default function Index() {
  return (
    <View style={styles.container}>
      <Text style={styles.header}>Welcome to the Running Room Project!</Text>
      <Link href="/login">Go to Login</Link>
      <Link href="/register">Register</Link>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  header: {
    fontSize: 24,
    fontWeight: "bold",
  },
});
