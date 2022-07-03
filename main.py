from youtube_transcript_api import YouTubeTranscriptApi as yt
import scrapetube

CHANNEL_ID="UCMiJRAwDNSNzuYeN2uWa0pA"
SEARCH_STRING="sub to the channel"

# https://commentpicker.com/youtube-channel-id.php
videos = scrapetube.get_channel(CHANNEL_ID)
#video_id = input("Enter Video ID: ")
f = open(f"url_list_{CHANNEL_ID}.txt", "a")    
# AaxPLnvCy08 (video with no given text)

def getDurationOfText(text, video_id):
    transcript = yt.get_transcript(video_id) #'Wuq7lS9rljw'
    result = list(filter(lambda e: text in e['text'].lower(), transcript))
    return (int(result[0]['start']) + 1)

if __name__ == '__main__':
    for video in videos:
        try:
            id = video['videoId']
            print('\nWriting \'{}\' to file: url_list_{}.txt'.format(id, CHANNEL_ID))
            start_time = getDurationOfText(SEARCH_STRING, video_id=id)
            f.write(f'https://www.youtube.com/watch?v={id}&t={start_time}s\n')
        except Exception:
            print('[MESSAGE] Search substring not found in video ID: {} Skipping...'.format(id))
            continue
    f.close()
    print('\n[MESSAGE] Created file: url_list_{}.txt in current directory.'.format(CHANNEL_ID))
    