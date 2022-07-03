from youtube_transcript_api import YouTubeTranscriptApi as yt
import scrapetube
import os

# CONFIGURATION
CHANNEL_ID="UCMiJRAwDNSNzuYeN2uWa0pA"
SEARCH_STRING="sub to the channel"

# https://commentpicker.com/youtube-channel-id.php
videos = scrapetube.get_channel(CHANNEL_ID)
#video_id = input("Enter Video ID: ")
f = open(f"url_list_{CHANNEL_ID}.txt", "a")    
# AaxPLnvCy08 (video with no given text)

def getDurationOfTextAndNextLines(text, video_id):
    transcript = yt.get_transcript(video_id) #'Wuq7lS9rljw'
    result = list(filter(lambda e: text in e[1]['text'].lower(), enumerate(transcript)))
    temp = result[0]
    concat = transcript[int(temp[0]) + 1]['text'] + ' ' + transcript[int(temp[0]) + 2]['text']
    return (int(temp[1]['start']) + 1, concat)

if __name__ == '__main__':
    for video in videos:
        try:
            id = video['videoId']
            
            print('\nWriting \'{}\' to file: url_list.txt')
            current = getDurationOfTextAndNextLines(SEARCH_STRING, video_id=id)
            start_time = current[0]
            arr = current[1].replace('would be ', '').split()

            # writing 2 words from script in case there is a degree adverb
            adjective = f"{arr[0]}" if len(arr) == 1 else f"{arr[0]}-{arr[1]}"
            f.write(f'{adjective} https://www.youtube.com/watch?v={id}&t={start_time}s\n')

            # Force the OS to store the file buffer to disc
            f.flush()
            os.fsync(f.fileno())
        except Exception:
            print('[MESSAGE] Search substring not found in video ID: {}\nSkipping...'.format(id))
            continue
    f.close()
    print('\n[MESSAGE] Created file: url_list.txt in current directory.')
    