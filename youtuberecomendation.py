import json
import requests
from isodate import parse_duration


with open("info.json", "r") as c:
    parameters = json.load(c)["parameters"]


search_url = 'https://www.googleapis.com/youtube/v3/search'
video_url = 'https://www.googleapis.com/youtube/v3/videos'


def youvideo():
    a = [{'id': 'jo505ZyaCbA', 'url': 'https://www.youtube.com/watch?v=jo505ZyaCbA', 'thumbnail': 'https://i.ytimg.com/vi/jo505ZyaCbA/hqdefault.jpg', 'duration': 2, 'title': 'The Beatles - Yesterday'}, {'id': 'k4V3Mo61fJM', 'url': 'https://www.youtube.com/watch?v=k4V3Mo61fJM', 'thumbnail': 'https://i.ytimg.com/vi/k4V3Mo61fJM/hqdefault.jpg', 'duration': 4, 'title': 'Coldplay - Fix You (Official Video)'}, {'id': 'IXdNnw99-Ic', 'url': 'https://www.youtube.com/watch?v=IXdNnw99-Ic', 'thumbnail': 'https://i.ytimg.com/vi/IXdNnw99-Ic/hqdefault.jpg', 'duration': 4, 'title': 'Pink Floyd - Wish You Were Here'}]
    return a


def youvideoauth(x):
    videos = []

    for i in x:
        search_params = {
            'key' : parameters['key'],
            'q' : i,
            'part' : 'snippet',
            'maxResults' : 1,
            'type' : 'video'
        }

        r = requests.get(search_url, params=search_params)

        results = r.json()['items']

        video_ids = []

        for result in results:
            video_ids.append(result['id']['videoId'])

        video_params = {
                'key' : parameters['key'],
                'id' : ','.join(video_ids),
                'part' : 'snippet,contentDetails',
                'maxResults' : 1
            }
        
        r = requests.get(video_url, params=video_params)
        results = r.json()['items']

        for result in results:
            video_data = {
                'id' : result['id'],
                'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                'thumbnail' : result['snippet']['thumbnails']['high']['url'],
                'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'title' : result['snippet']['title'],
                }
            videos.append(video_data)
    return videos
