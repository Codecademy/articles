import SwiftUI

struct ContentView: View {
  // State property wrapper is required to change value of var
  @State var randomNum = 1
  var body: some View {
    VStack {
      Text("Roll Me!")

      Image("dice\(randomNum)")
        .overlay(RoundedRectangle(cornerRadius: 5.0).stroke(lineWidth: 1.0))

      Button("Roll",
        action: {
          // This line of code will run when the button is clicked
          randomNum = Int.random(in: 1...6)
      })
    }
  }
}

struct ContentView_Previews: PreviewProvider {
  static var previews: some View {
    Group {
      ContentView()
    }
  }
}
