require('dotenv').config()

const Twit = require('twit')
const twitAPIConfig = require('./config.js')

console.log("Starting twitter bot...")

const twit = new Twit(twitAPIConfig) 

const sendTweet = (text) => {
  twit.post('statuses/update', { status: text }, (err, data, response) => {
    if(err) throw err.message
    console.log(data)
  })
}

sendTweet("Hello, Twitterverse!")

// const likeTweet = tweetIdString => {
//   twit.post('favorites/create', { id: tweetIdString }, (err, data, response) => {
//     if(err) throw err 
//     console.log(data)
//   })
// }

// likeTweet("1423734592691900422")

// const follow = (twitterHandle, userID = null) => {
//   twit.post("friendships/create", { screen_name: twitterHandle, id: userID }, (err, data, response) => {
//     if(err) throw err

//     console.log(data)
//   })
// }

// follow("codecademy")