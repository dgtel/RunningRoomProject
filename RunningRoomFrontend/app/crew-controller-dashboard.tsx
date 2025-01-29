import React from "react";
import { View, Text, StyleSheet } from "react-native";

export default function CrewControllerDashboard() {
  return (
    <View style={styles.container}>
      <Text style={styles.header}>Crew Controller Dashboard</Text>
      <Text>Manage crew schedules, bed assignments, and approvals.</Text>
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
