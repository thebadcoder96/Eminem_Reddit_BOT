# Eminem Reddit Bot

This is a reddit bot that will search for any Eminem song or album and give you the link and statistics for a song pulled from Spotify API as the reply message.

### How to use
Simply comment '!song' or '!album' followed by the song or album you would like to search anywhere on reddit. For example:

```!song Survival``` or ```!album Kamikaze```

[You can learn more about the bot and the Spotify analysis here](https://www.reddit.com/user/Eminem_Bot/comments/p0t572/what_it_all_means/).

### How to run

- Install required packages by ```pip install -r requirements.txt```.
- ```PRAW``` and ```spotipy``` are the main libraries used.
- Must have a reddit account. Visit the [apps page](https://www.reddit.com/prefs/apps) to get your  ```client_id``` and ```client_secret```.
- Must also have an Spotify account to get the ```client_id``` and ```client_secret``` for spotify as well.
- Please enter the credentials in the [*praw.ini*](/praw.ini) file.

**Note:** I am still working on this project so if you have any feedback, insights or suggestions for improvement, please ping me on [Reddit](https://www.reddit.com/user/thebatgamer/).