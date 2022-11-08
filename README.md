# `TWITTER_BOT`

It's just a simple twitter bot that has a few features.
* https://twitter.com/WonderfullBot

### Comment installer les dépendances ?
```
git clone https://github.com/LucasHissinger/Twitter_bot.git
cd Twitter_bot
pip install -r requirements.txt
```

### Mise en place
Next, download chromedriver.exe and put it in the root of the repo

* chromedriver: https://chromedriver.chromium.org/downloads
Don't forget to add it to the PATH

Create a .env file and fill it like this:

```
CONSUMER_KEY=consumer_key
CONSUMER_SECRET=consumer_secret
ACCESS_TOKEN=access_token
ACCESS_SECRET=access_secret
URL_METEO=http://api.openweathermap.org/data/2.5/weather?q=
API_METEO =api_meteo_from_
```

link to help with this
* https://openweathermap.org/appid
* https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens



# comment lancer le programme ?
Il faut lancer le programme avec une console linux (ubuntu, fedora ou kali peu importe) pour que le programme puisse lancer le script "setup.sh" pour installer les dépendances

    $ python3 src/main.py
