import React from "react";
import { View, Text, StyleSheet } from "react-native";

export default function CareTakerDashboard() {
  return (
    <View style={styles.container}>
      <Text style={styles.header}>Care Taker Dashboard</Text>
      <Text>View and update bed statuses and oversee meals.</Text>
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

