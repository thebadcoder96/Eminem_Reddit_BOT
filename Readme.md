# Reddit Bot that displays Eminem songs stats from Spotify and Youtube

This is a reddit bot that will search for any Eminem song or album and give you the link and some statistics for a song pulled from the Spotify API and Youtube Data API v3 as the reply message. This bot is currently only monitoring [r/Eminem](https://www.reddit.com/r/eminem), [r/Music](https://www.reddit.com/r/music/), and [r/hiphopheads](https://www.reddit.com/r/hiphopheads/).

### Motivation
I love [Reddit](https://www.reddit.com/), I love Eminem and I love Python! So I combined all of them to program an account to reply with the data from Spotify and YouTube of any Eminem songs :)

### Frameworks
- PRAW - Framework build on top of Reddit API.
- Spotipy - Library for the Spotify Web API.
- google-api-python-client - Library to acess Youtube Data API.

### How to use
Simply comment '!song' or '!album' followed by the song or album you would like to search anywhere on [r/Eminem](https://www.reddit.com/r/eminem), [r/Music](https://www.reddit.com/r/music/), and [r/hiphopheads](https://www.reddit.com/r/hiphopheads/). For example:

```!song Survival``` or ```!album Kamikaze```

[You can learn more about the bot and the Spotify analysis here](https://www.reddit.com/user/Eminem_Bot/comments/p0t572/what_it_all_means/).

### How to run

- Install required packages by ```pip install -r requirements.txt```.
- ```PRAW```, ```spotipy```, ```google-api-python-client``` are the main libraries used.
- Must have a reddit account. Visit the [apps page](https://www.reddit.com/prefs/apps) to get your  ```client_id``` and ```client_secret```.
- Must also have an Spotify account to get the ```client_id``` and ```client_secret``` for spotify as well.
- Please enter the credentials in the [*praw.ini*](/praw.ini) file.
