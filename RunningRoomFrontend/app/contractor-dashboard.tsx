import React from "react";
import { View, Text, StyleSheet } from "react-native";

export default function ContractorDashboard() {
  return (
    <View style={styles.container}>
      <Text style={styles.header}>Contractor Dashboard</Text>
      <Text>Manage food tokens and generate bills.</Text>
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
