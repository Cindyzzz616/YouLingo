from googleapiclient.discovery import build

# Your API key
api_key = 'AIzaSyBT2UKWCmrb9DcK_OLGSegbkd8WDE3-XBI'
youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_details(video_id):
    request = youtube.videos().list(
        part='snippet,contentDetails,statistics',
        id=video_id
    )
    response = request.execute()
    return response['items'][0]['snippet']

video_id = 'dQw4w9WgXcQ'  # Replace with your desired video ID
video_details = get_video_details(video_id)
print(video_details)

# response (yup chatgpt rickrolled me with the sample video):

# {'publishedAt': '2009-10-25T06:57:33Z', 'channelId':
# 'UCuAXFkgsw1L7xaCfnd5JJOw', 'title': 'Rick Astley - Never Gonna Give You Up
# (Official Music Video)', 'description': 'The official video for “Never
# Gonna Give You Up” by Rick Astley. \n\nNever: The Autobiography 📚 OUT NOW!
# \nFollow this link to get your copy and listen to Rick’s ‘Never’ playlist
# ❤️ #RickAstleyNever\nhttps://linktr.ee/rickastleynever\n\n“Never Gonna Give
# You Up” was a global smash on its release in July 1987, topping the charts
# in 25 countries including Rick’s native UK and the US Billboard Hot 100.
# It also won the Brit Award for Best single in 1988. Stock Aitken and
# Waterman wrote and produced the track which was the lead-off single and
# lead track from Rick’s debut LP “Whenever You Need Somebody”.  The album
# was itself a UK number one and would go on to sell over 15 million copies
# worldwide.\n\nThe legendary video was directed by Simon West – who later
# went on to make Hollywood blockbusters such as Con Air, Lara Croft – Tomb
# Raider and The Expendables 2.  The video passed the 1bn YouTube views
# milestone on 28 July 2021.\n\nSubscribe to the official Rick Astley YouTube
# channel: https://RickAstley.lnk.to/YTSubID\n\nFollow Rick
# Astley:\nFacebook: https://RickAstley.lnk.to/FBFollowID \nTwitter:
# https://RickAstley.lnk.to/TwitterID \nInstagram:
# https://RickAstley.lnk.to/InstagramID \nWebsite:
# https://RickAstley.lnk.to/storeID \nTikTok:
# https://RickAstley.lnk.to/TikTokID\n\nListen to Rick Astley:\nSpotify:
# https://RickAstley.lnk.to/SpotifyID \nApple Music:
# https://RickAstley.lnk.to/AppleMusicID \nAmazon Music:
# https://RickAstley.lnk.to/AmazonMusicID \nDeezer:
# https://RickAstley.lnk.to/DeezerID \n\nLyrics:\nWe’re no strangers to
# love\nYou know the rules and so do I\nA full commitment’s what I’m thinking
# of\nYou wouldn’t get this from any other guy\n\nI just wanna tell you how
# I’m feeling\nGotta make you understand\n\nNever gonna give you up\nNever
# gonna let you down\nNever gonna run around and desert you\nNever gonna make
# you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt
# you\n\nWe’ve known each other for so long\nYour heart’s been aching but
# you’re too shy to say it\nInside we both know what’s been going on\nWe know
# the game and we’re gonna play it\n\nAnd if you ask me how I’m
# feeling\nDon’t tell me you’re too blind to see\n\nNever gonna give you
# up\nNever gonna let you down\nNever gonna run around and desert you\nNever
# gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and
# hurt you\n\n#RickAstley #NeverGonnaGiveYouUp #WheneverYouNeedSomebody
# #OfficialMusicVideo', 'thumbnails': {'default': {'url':
# 'https://i.ytimg.com/vi/dQw4w9WgXcQ/default.jpg', 'width': 120, 'height':
# 90}, 'medium': {'url': 'https://i.ytimg.com/vi/dQw4w9WgXcQ/mqdefault.jpg',
# 'width': 320, 'height': 180}, 'high': {'url':
# 'https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg', 'width': 480, 'height':
# 360}, 'standard': {'url': 'https://i.ytimg.com/vi/dQw4w9WgXcQ/sddefault.jpg
# ', 'width': 640, 'height': 480}, 'maxres': {'url':
# 'https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg', 'width': 1280,
# 'height': 720}}, 'channelTitle': 'Rick Astley', 'tags': ['rick astley',
# 'Never Gonna Give You Up', 'nggyu', 'never gonna give you up lyrics',
# 'rick rolled', 'Rick Roll', 'rick astley official', 'rickrolled', 'Fortnite
# song', 'Fortnite event', 'Fortnite dance', 'fortnite never gonna give you
# up', 'rick roll', 'rickrolling', 'rick rolling', 'never gonna give you up',
# '80s music', 'rick astley new', 'animated video', 'rickroll', 'meme songs',
# 'never gonna give u up lyrics', 'Rick Astley 2022', 'never gonna let you
# down', 'animated', 'rick rolls 2022', 'never gonna give you up karaoke'],
# 'categoryId': '10', 'liveBroadcastContent': 'none', 'defaultLanguage':
# 'en', 'localized': {'title': 'Rick Astley - Never Gonna Give You Up (
# Official Music Video)', 'description': 'The official video for “Never Gonna
# Give You Up” by Rick Astley. \n\nNever: The Autobiography 📚 OUT NOW!
# \nFollow this link to get your copy and listen to Rick’s ‘Never’ playlist
# ❤️ #RickAstleyNever\nhttps://linktr.ee/rickastleynever\n\n“Never Gonna Give
# You Up” was a global smash on its release in July 1987, topping the charts
# in 25 countries including Rick’s native UK and the US Billboard Hot 100.
# It also won the Brit Award for Best single in 1988. Stock Aitken and
# Waterman wrote and produced the track which was the lead-off single and
# lead track from Rick’s debut LP “Whenever You Need Somebody”.  The album
# was itself a UK number one and would go on to sell over 15 million copies
# worldwide.\n\nThe legendary video was directed by Simon West – who later
# went on to make Hollywood blockbusters such as Con Air, Lara Croft – Tomb
# Raider and The Expendables 2.  The video passed the 1bn YouTube views
# milestone on 28 July 2021.\n\nSubscribe to the official Rick Astley YouTube
# channel: https://RickAstley.lnk.to/YTSubID\n\nFollow Rick
# Astley:\nFacebook: https://RickAstley.lnk.to/FBFollowID \nTwitter:
# https://RickAstley.lnk.to/TwitterID \nInstagram:
# https://RickAstley.lnk.to/InstagramID \nWebsite:
# https://RickAstley.lnk.to/storeID \nTikTok:
# https://RickAstley.lnk.to/TikTokID\n\nListen to Rick Astley:\nSpotify:
# https://RickAstley.lnk.to/SpotifyID \nApple Music:
# https://RickAstley.lnk.to/AppleMusicID \nAmazon Music:
# https://RickAstley.lnk.to/AmazonMusicID \nDeezer:
# https://RickAstley.lnk.to/DeezerID \n\nLyrics:\nWe’re no strangers to
# love\nYou know the rules and so do I\nA full commitment’s what I’m thinking
# of\nYou wouldn’t get this from any other guy\n\nI just wanna tell you how
# I’m feeling\nGotta make you understand\n\nNever gonna give you up\nNever
# gonna let you down\nNever gonna run around and desert you\nNever gonna make
# you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt
# you\n\nWe’ve known each other for so long\nYour heart’s been aching but
# you’re too shy to say it\nInside we both know what’s been going on\nWe know
# the game and we’re gonna play it\n\nAnd if you ask me how I’m
# feeling\nDon’t tell me you’re too blind to see\n\nNever gonna give you
# up\nNever gonna let you down\nNever gonna run around and desert you\nNever
# gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and
# hurt you\n\n#RickAstley #NeverGonnaGiveYouUp #WheneverYouNeedSomebody
# #OfficialMusicVideo'}, 'defaultAudioLanguage': 'en'}
