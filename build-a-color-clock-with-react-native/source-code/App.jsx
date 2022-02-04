import React, { Component } from "react";
import { View } from "react-native";
import ColorClock from "./ColorClock";

class Clock extends Component {
  render() {
    return (
      <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
        <ColorClock minuteHandLength={90} />
      </View>
    );
  }
}
