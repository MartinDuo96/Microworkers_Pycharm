from googleapiclient.discovery import build

api_key = 'AIzaSyBK064kZLO0ov7N9aTFAMhwXb-u0WYJIQE'
youtube = build('youtube', 'v3', developerKey=api_key)

part_string = 'contentDetails'
url = 'https://www.youtube.com/watch?v=OL0ssUpvBmY&ab_channel=OnlineCheckWriter'
video_id = url[url.index('v=')+2:url.index('&ab')]

response = youtube.videos().list(
    part=part_string,
    id=video_id
).execute()

duration = response['items'][0]['contentDetails']['duration']
duration = duration.strip('PT')
print(duration)

if 'S' in duration:
    if 'M' in duration:
        min = duration[:duration.index('M')]
        sec = duration[duration.index('M') + 1:duration.index('S')]
        print(min, 'Minuten', sec, 'Sekunden')
    else:
        sec = duration.strip('S')
        print(sec, 'Sekunden')
else:
    min = duration.strip('M')
    print(min, 'Minuten')


'''
if 'M' in duration:
    min = duration[duration.index('T')+1:duration.index('M')]
    sec = duration[duration.index('M') + 1:duration.index('S')]
    print(min, 'Minuten', sec, 'Sekunden')

else:
    sec = duration[duration.index('T') + 1:duration.index('S')]
    print(sec, 'Sekunden')
'''