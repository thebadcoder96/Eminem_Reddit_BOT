import praw, time, spotipy, configparser, math
from spotipy.oauth2 import SpotifyClientCredentials

#Authentication
def authenticate():
    print('Authenticating...')
    r = praw.Reddit('embot', user_agent = 'Eminem comment bot v0.1')
    print(f"Authenicated!:) Username: {r.user.me()}")
    return r

#Convert duration from ms 
def totime(ms):
    seconds = math.floor((ms/1000)%60)
    minutes = math.floor((ms/(1000*60))%60)
    hours = math.floor((ms/(1000*60*60))%24)

    if hours == 1:
        dur= f'{hours}:{minutes}:{seconds}'
    elif minutes == 0 and hours == 0:
        dur= f'00:00:{seconds}'
    else:
        dur= f'00:{minutes}:{seconds}'
    return dur

#Search Spotify for song/album
def spotify_search(comment):
    #Reading from praw.ini
    config = configparser.ConfigParser()
    config.read('praw.ini')

    #Spotify API
    creds =SpotifyClientCredentials(client_id=config['spotify']['client_id'],
                                    client_secret=config['spotify']['client_secret'])
    sp = spotipy.Spotify(auth_manager=creds)
    
    #print(b)
    if '!album' in comment:
        try:
            name = comment.split('!album ')[1]
            results = sp.search(q="eminem" + " " + name, type="album", limit=1)
            if results['albums']['items']:
                results = results['albums']['items'][0]
                # Extracting needed information
                link = results['external_urls']['spotify']
                pop = sp.album(results['id'])['popularity']
                songs = sp.album(results['id'])['total_tracks']
                #Calculating total duration of the album
                tot=0
                tracks = sp.album(results['id'])['tracks']['items']
                for i in range(len(tracks)):
                    tot +=(tracks[i]['duration_ms'])
                #print(link, pop, songs)
                return create_message(name, link, pop, songs=songs, duration=totime(tot))
            else:
                m = (f'{name} album not found on spotify.:( Please be more specific.'
                    '\n\n^beep ^boop! ^I ^am ^a ^bot ^that ^finds ^stats ^for ^***Eminem*** ^songs!  ^Find ^out ^more [^about ^me ^here! ](https://www.reddit.com/r/u_eminem_bot)'
                    )
                print(m)
                return m
        except Exception as e:
            print(e)
            return 'Error. Could not find album name.'

    else:
        try:
            name = comment.split('!song ')[1]
            #Searching Spotify
            results = sp.search(q="eminem" + " track:" + name, type="track", limit=1)
            if results['tracks']['items']:
                results = results['tracks']['items'][0]
                # Extracting needed information
                link = results['external_urls']['spotify']
                features = sp.audio_features(results['id'])
                pop = sp.track(results['id'])['popularity']
                #print(link, "\n", features[0], "\n" ,pop)
                return create_message(name, link, pop, features=features[0])
            else:
                m = (f'{name} song not found on spotify.:( Please be more specific.'
                    '\n\n^beep ^boop! ^I ^am ^a ^bot ^that ^finds ^stats ^for ^***Eminem*** ^songs!  ^Find ^out ^more [^about ^me ^here! ](https://www.reddit.com/r/u_eminem_bot)'
                     )
                print(m)
                return m
        except Exception as e:
            print(e)
            return 'Error. Could not find song name.'

#Function to create the reply
def create_message(name, link, pop, songs=0,features={}, duration=0):
    if songs == 0:
        name = name.title()
        dur = totime(features["duration_ms"])
        
        if features["mode"] == 0:
            mode='Minor'
        else:
            mode='Major'
        
        message = (f'The spotify link for [{name} is here]({link}). \n\n'
                   f'Below are some stats and audio analysis for {name} from Spotify:\n\n'
                   '| Stat | Value |  Description |\n'
                   '|:----:|------:|:------------:|\n'
                   f'|**Duration**|{dur}| Duration of the song |\n'
                   f'|**Popularity**|{pop}%| Popularity (out of 100) |\n'
                   f'|**Key**|{features["key"]}| Pitch of the song |\n'
                   f'|**Mode**|{mode}| Major/Minor |\n'
                   f'|**Tempo**|{features["tempo"]}| Mood: Tempo in BPM |\n'
                   f'|**Energy**|{features["energy"]}| Mood: intensity/activity |\n'
                   f'|**Valence**|{features["valence"]}| Mood: Positiveness  |\n'
                   f'|**Danceability**|{features["danceability"]}| Mood: Danceable to |\n'
                   f'|**Loudness**|{features["loudness"]}| Property: Loudness in dB |\n'
                   f'|**Speechiness**|{features["speechiness"]}| Property: Speech in song |\n'
                   f'|**Instrumentalness**|{features["instrumentalness"]}| Property: only music |\n'
                   f'|**Liveness**|{features["liveness"]}| Context: Song performed Live |\n'
                   f'|**Acousticness**|{features["acousticness"]}| Context: Acoustic song |\n'
                   '\n\n **[What it all means](https://www.reddit.com/user/Eminem_Bot/comments/p0t572/what_it_all_means/)**'
                   '\n\n^beep ^boop! ^I ^am ^a ^bot ^that ^finds ^stats ^for ^***Eminem*** ^songs!  ^Find ^out ^more [^about ^me ^here! ](https://www.reddit.com/r/u_eminem_bot)'

                   )

    else:
        message = (f'The spotify link for the album [{name} is here]({link}). \n'
                   f'Below are some stats for the album from Spotify:\n\n'
                   '| Stat | Value |\n'
                   '|:----:|------:|\n'
                   f'|**No of Songs**|{songs}|\n'
                   f'|**Popularity**|{pop}%|\n'
                   f'|**Duration**|{duration}|\n'
                   '\n\n  **[What it all means](https://www.reddit.com/user/Eminem_Bot/comments/p0t572/what_it_all_means/)**'

                   '\n\n^beep ^boop! ^I ^am ^a ^bot ^that ^finds ^stats ^for ^***Eminem*** ^songs!  ^Find ^out ^more [^about ^me ^here! ](https://www.reddit.com/r/u_eminem_bot)'

                  )


    #print(type(message))
    return message

#Function to search for comments
def runbot(reddit, replied_to):
    print("Fetching comments..")
    for comment in reddit.subreddit('all').stream.comments(skip_existing=False):
        if ('!song' in comment.body.lower() or '!album' in comment.body.lower()) and (comment.id not in replied_to) and (comment.author != reddit.user.me()): 
            print('found!' + comment.body)
            message = spotify_search(comment.body.lower())
            #print(type(message))
            #print(message + '\n')
            comment.reply(message)
            print("Replied to : "+ comment.id)
            replied_to.append(comment.id)
            
            with open('replied.txt','a') as f:
                f.write(comment.id + '\n')
            time.sleep(5)
        #time.sleep(5)

def main():
    with open('replied.txt','r') as f:
        replied_to= f.read().split('\n')
        replied_to= list(filter(None, replied_to))
        
    reddit = authenticate()
    runbot(reddit, replied_to)

if __name__ == '__main__':main()