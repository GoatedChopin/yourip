import os
import time
import random as r


URLS = open('urls.txt').readlines()
OUTPUT_FOLDER = '/home/colby/Documents/Guitar/rip/songs/'
DEFAULT_ARGS = f' -x --audio-format best --audio-quality 0 --output \'{OUTPUT_FOLDER}%(title)s.%(ext)s\' '


def main():
    # os.system('./youtube-dl-2023.06.25.810/youtube-dl ' + DEFAULT_ARGS + " ".join(URLS))
    for URL in URLS:
        os.system('./yt-dlp' + DEFAULT_ARGS + URL)
        seconds = r.randint(4, 17)
        time.sleep(seconds)


if __name__ == '__main__':
    main()
