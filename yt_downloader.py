
**`yt_downloader.py`**
```python
import argparse
from pytube import YouTube

def download(url, path='.', audio_only=False):
    yt = YouTube(url)
    if audio_only:
        stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    else:
        stream = yt.streams.get_highest_resolution()
    out = stream.download(output_path=path)
    print(f'Downloaded: {out}')

def main():
    parser = argparse.ArgumentParser(description='Simple YouTube downloader (pytube)')
    parser.add_argument('url', help='YouTube video URL')
    parser.add_argument('--path', default='.', help='Download destination folder')
    parser.add_argument('--audio', action='store_true', help='Download audio only')
    args = parser.parse_args()
    download(args.url, path=args.path, audio_only=args.audio)

if __name__ == '__main__':
    main()
