import React from "react";
import { View, Text, StyleSheet } from "react-native";

export default function CrewDashboard() {
  return (
    <View style={styles.container}>
      <Text style={styles.header}>Crew Dashboard</Text>
      <Text>Manage Check-In/Out, food tokens, and feedback.</Text>
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
    marginBottom: 16,
  },
});
