import config
from googleapiclient.discovery import build

youtube = build('youtube', 'v3', developerKey= config.API)


def get_channel_videos(channel_id):
    
    # get Uploads playlist id
    res = youtube.channels().list(id=channel_id, 
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    videos = []
    next_page_token = None
    
    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id, 
                                           part='snippet', 
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')
        
        if next_page_token is None:
            break
    
    return videos

videos = get_channel_videos('UCmh5gdwCx6lN7gEC20leNVA')


with open('videonames.txt', 'a') as filehandle:
    for video in videos:
       print(video['snippet']['title'])
       filehandle.write('%s\n' % video['snippet']['title'])

num_lines = 0
with open("videonames1.txt", 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)