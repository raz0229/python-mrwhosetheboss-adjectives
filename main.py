from youtube_transcript_api import YouTubeTranscriptApi as yt

#video_id = input("Enter Video ID: ")
# AaxPLnvCy08 (video with no given text)

def getDurationOfText(text, video_id):
    transcript = yt.get_transcript(video_id) #'Wuq7lS9rljw'
    result = list(filter(lambda e: text in e['text'].lower(), transcript))
    return (int(result[0]['start']) + 1)

if __name__ == '__main__':
    id = 'Wuq7lS9rljw'
    try:
        start_time = getDurationOfText('sub to the channel', video_id=id)
        print(f'https://www.youtube.com/watch?v={id}&t={start_time}s')
    except Exception:
        print('Search substring not found in video ID: ', id)