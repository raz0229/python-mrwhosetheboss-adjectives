# https://www.cutyt.com/mydownloads

import subprocess
from threading import Thread
from time import sleep
import urllib.parse

SIGNAL="fiQ9wGwFIvAYChPxo5jxMQ8b71ebde1"
ADD_OFFSET=10

def sendrequest(title, url, timestamp):
    request = f'''curl 'https://www.cutyt.com/home/getdownloadlink' \
                        -H 'authority: www.cutyt.com' \
                        -H 'accept: */*' \
                        -H 'accept-language: en-US,en;q=0.9,ur-PK;q=0.8,ur;q=0.7,az;q=0.6,af;q=0.5,eo;q=0.4,et;q=0.3,sq;q=0.2' \
                        -H 'cache-control: no-cache' \
                        -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
                        -H 'cookie: _ga=GA1.1.179539826.1656945339; __atuvc=1%7C27; __atuvs=62c2faf815558587000; _ga_PK6JDTVPMV=GS1.1.1656944111.1.1.1656945450.0' \
                        -H 'dnt: 1' \
                        -H 'origin: https://www.cutyt.com' \
                        -H 'pragma: no-cache' \
                        -H 'referer: https://www.cutyt.com/' \
                        -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"' \
                        -H 'sec-ch-ua-mobile: ?1' \
                        -H 'sec-ch-ua-platform: "Android"' \
                        -H 'sec-fetch-dest: empty' \
                        -H 'sec-fetch-mode: cors' \
                        -H 'sec-fetch-site: same-origin' \
                        -H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36' \
                        -H 'x-requested-with: XMLHttpRequest' \
                        --data-raw 'ytUrl={url}&selectedOption=248%2Bbestaudio&start={timestamp}&end={int(timestamp) + ADD_OFFSET}&shouldTrim=true&title={title}&signalrId={SIGNAL}' \
    '''

    subprocess.run(request, shell=True)


if __name__ == '__main__':
    try:
        with open('url_list.txt', 'r') as f:
            for line in f:
                file = line.split()
                x = file[1].split('&')
                url = urllib.parse.quote(x[0], safe='')
                timestamp = x[1].replace('t=', '').replace('s', '')
                title = file[0].replace('-', '+')

                thread = Thread(target=sendrequest, args=(title,url,timestamp,))
                thread.start()
                sleep(6)
                subprocess.run('kill -9 curl', shell=True)
                print(f'Request sent, {title}.mp4 for video: {x[0]}')
        print('\nSee your downloads at: https://www.cutyt.com/mydownloads')        

    except Exception as e:
        print(e)
        print('\n[ERROR] File: \'url_list.txt\' not found. Please run \'main.py\' first')
