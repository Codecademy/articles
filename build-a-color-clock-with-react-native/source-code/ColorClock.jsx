import React, { Component } from "react";
import { Image, View } from "react-native";

class ColorClock extends Component {
  constructor(props) {
    super(props);

    let d = new Date();
    let currentSecond = d.getSeconds() * 6;
    let currentMinute = d.getMinutes() * 6 + currentSecond / 60;
    let currentHour =
      ((d.getHours() % 12) / 12) * 360 + 90 + currentMinute / 12;
    this.state = {
      sec: currentSecond,
      min: currentMinute,
      hour: currentHour,
    };
  }
  componentDidMount() {
    this.timer = setInterval(() => {
      let d = new Date();
      this.setState({ sec: d.getSeconds() * 6 });
      this.setState({ min: d.getMinutes() * 6 + (d.getSeconds() * 6) / 60 });
      this.setState({
        hour:
          ((d.getHours() % 12) / 12) * 360 +
          90 +
          (d.getMinutes() * 6 + (d.getSeconds() * 6) / 60) / 12,
      });
    }, 1000);
  }
  componentWillUnmount() {
    clearInterval(this.timer);
  }
  getClockFrame() {
    return {
      width: this.props.clockSize,
      height: this.props.clockSize,
      position: "relative",
      borderColor: "black",
      borderWidth: this.props.clockBorderWidth,
      borderRadius: this.props.clockSize / 2,
    };
  }
  getClockContainer() {
    return {
      width: this.props.clockSize,
      height: this.props.clockSize,
      position: "absolute",
      right: -this.props.clockBorderWidth,
      bottom: -this.props.clockBorderWidth,
    };
  }
  getClockFace() {
    return {
      width: this.props.clockCentreSize,
      height: this.props.clockCentreSize,
      backgroundColor: this.props.clockCentreColor,
      borderRadius: this.props.clockCentreSize / 2,
      top: (this.props.clockSize - this.props.clockCentreSize) / 2,
      left: (this.props.clockSize - this.props.clockCentreSize) / 2,
    };
  }
  hourHand() {
    return {
      width: 0,
      height: 0,
      position: "absolute",
      backgroundColor: this.props.hourHandColor,
      top: this.props.clockSize / 2,
      left: this.props.clockSize / 2,
      marginVertical: -this.props.hourHandWidth,
      marginLeft: -this.props.hourHandLength / 2,
      paddingVertical: this.props.hourHandWidth,
      paddingLeft: this.props.hourHandLength,
      borderTopLeftRadius: this.props.hourHandCurved
        ? this.props.hourHandWidth
        : 0,
      borderBottomLeftRadius: this.props.hourHandCurved
        ? this.props.hourHandWidth
        : 0,
    };
  }
  minuteHand() {
    return {
      width: 0,
      height: 0,
      position: "absolute",
      backgroundColor: this.props.minuteHandColor,
      top: this.props.clockSize / 2,
      left: this.props.clockSize / 2,
      marginTop: -(this.props.minuteHandLength / 2),
      marginHorizontal: -this.props.minuteHandWidth,
      paddingTop: this.props.minuteHandLength,
      paddingHorizontal: this.props.minuteHandWidth,
      borderTopLeftRadius: this.props.minuteHandCurved
        ? this.props.minuteHandWidth
        : 0,
      borderTopRightRadius: this.props.minuteHandCurved
        ? this.props.minuteHandWidth
        : 0,
    };
  }
  secondHand() {
    return {
      width: 0,
      height: 0,
      position: "absolute",
      backgroundColor: "black",
      top: this.props.clockSize / 2,
      left: this.props.clockSize / 2,
      marginTop: -(this.props.secondHandLength / 2),
      marginHorizontal: -this.props.secondHandWidth,
      paddingTop: this.props.secondHandLength,
      paddingHorizontal: this.props.secondHandWidth,
      borderTopLeftRadius: this.props.secondHandCurved
        ? this.props.secondHandWidth
        : 0,
      borderTopRightRadius: this.props.secondHandCurved
        ? this.props.secondHandWidth
        : 0,
    };
  }
  render() {
    return (
      <View style={this.getClockFrame()}>
        {
          <Image
            style={{
              width: this.props.clockSize - this.props.clockBorderWidth * 2,
              height: this.props.clockSize - this.props.clockBorderWidth * 2,
            }}
            resizeMode="stretch"
            source={require("./clock.jpg")}
          />
        }
        <View style={this.getClockContainer()}>
          <View
            style={[
              this.hourHand(),
              {
                transform: [
                  { rotate: this.state.hour + "deg" },
                  {
                    translateX: -(
                      this.props.hourHandOffset +
                      this.props.hourHandLength / 2
                    ),
                  },
                ],
              },
            ]}
          />
          <View
            style={[
              this.minuteHand(),
              {
                transform: [
                  { rotate: this.state.min + "deg" },
                  {
                    translateY: -(
                      this.props.minuteHandOffset +
                      this.props.minuteHandLength / 2
                    ),
                  },
                ],
              },
            ]}
          />
          <View
            style={[
              this.secondHand(),
              {
                transform: [
                  { rotate: this.state.sec + "deg" },
                  {
                    translateY: -(
                      this.props.secondHandOffset +
                      this.props.secondHandLength / 2
                    ),
                  },
                ],
              },
            ]}
          />
          <View style={this.getClockFace()} />
        </View>
      </View>
    );
  }
}

ColorClock.defaultProps = {
  backgroundImage: "./clock.jpg",
  clockSize: 270,
  clockBorderWidth: 7,
  clockCentreSize: 15,
  clockCentreColor: "red",
  hourHandColor: "blue",
  hourHandCurved: true,
  hourHandLength: 70,
  hourHandWidth: 5.5,
  hourHandOffset: 0,
  minuteHandColor: "blue",
  minuteHandCurved: true,
  minuteHandLength: 100,
  minuteHandWidth: 5,
  minuteHandOffset: 0,
  secondHandColor: "blue",
  secondHandCurved: false,
  secondHandLength: 100,
  secondHandWidth: 2,
  secondHandOffset: 0,
};
