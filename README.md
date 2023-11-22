
# Twitter Bot

A Twitter bot with some features


## Features

- like and reply to your response to him
- retweet tweets
- get meteo of country in tweets if you tag him with "#meteo"
- get anime synopsis if you tag him with "#anime"
- send dm message with citation if you tag him with "#dm"
- randomly tweet a "cringe" photos one time per day


## Run Locally

Clone the project

```bash
  git clone https://github.com/LucasHissinger/Twitter_bot.git
```

Go to the project directory

```bash
  cd Twitter_bot
```

Install dependencies

```bash
  pip3 install -r requirement.txt
```

Install and add chromedriver
```bash
download binary at https://chromedriver.chromium.org/downloads
put the binary at the root of the repo
put it in your PATH
```

run the bot

```bash
  python3 src/main.py
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`CONSUMER_KEY`

`CONSUMER_SECRET`

`ACCESS_TOKEN`

`ACCESS_SECRET`

`URL_METEO=http://api.openweathermap.org/data/2.5/weather?q=`

`API_METEO`


## Feedback

If you have any feedback, please reach out to me at lucas.hissinger@epitech.eu


## Documentation
Some usefull links :

[Twitter Secret](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)

[Api creds](https://openweathermap.org/appid)

