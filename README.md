# Streaming

- ffmpeg -i input.mp4 -profile:v baseline -level 3.0 -s 640x360 -start_number 0 -hls_time 10 -hls_list_size 0 -f hls index.m3u8
- ffmpeg -i input.mp4 -vf scale=w=1280:h=720:force_original_aspect_ratio=decrease -c:a aac -ar 48000 -c:v h264 -profile:v main -crf 20 -sc_threshold 0 -g 48 -keyint_min 48 -hls_playlist_type vod -b:v 2800k -maxrate 2996k -bufsize 4200k -b:a 128k -hls_time 10 -hls_list_size 0 -f hls index.m3u8

# Filename

- ffmpeg -i input.mp4 -vf scale=w=1280:h=720:force_original_aspect_ratio=decrease -c:a aac -ar 48000 -c:v h264 -profile:v main -crf 20 -sc_threshold 0 -g 48 -keyint_min 48 -hls_playlist_type vod -b:v 2800k -maxrate 2996k -bufsize 4200k -b:a 128k -segment_list index.m3u8 -segment_time 10 -f ssegment -strftime 1 uuid-%Y*%m*%d-%H\*%M\_%S.ts

**Filename**

- -segment_list index.m3u8
- -segment_time 10
- -f ssegment
- -strftime 1 uuid-%Y*%m*%d-%H*%M*%S.ts

# Webcam

- ffmpeg -f dshow -i video="DroidCam Source 3" -profile:v high -pix_fmt yuvj420p -level:v 4.1 -preset veryfast -tune zerolatency -c:v h264 -r 60 -b:v 2800k -s 1280x720 -c:a aac -ac 2 -ab 32k -ar 48000 -hls_time 20 -hls_list_size 0 -f hls index.m3u8

**1080p**:

- scale=w=1920:h=1080:force_original_aspect_ratio=decrease
- -b:v 5000k
- -maxrate 5350k
- -bufsize 7500k
- -b:a 192k

**720p**:

- scale=w=1280:h=720:force_original_aspect_ratio=decrease
- -b:v 2800k
- -maxrate 2996k
- -bufsize 4200k
- -b:a 128k

**480p**:

- scale=w=842:h=480:force_original_aspect_ratio=decrease
- -b:v 1400k
- -maxrate 1498k
- -bufsize 2100k
- -b:a 128k

**360p**:

- scale=w=640:h=360:force_original_aspect_ratio=decrease
- -b:v 800k
- -maxrate 856k
- -bufsize 1200k
- -b:a 96k

**Args**:

- -r fps
- -an disables audio stream selection
- -re by default ffmpeg attempts to read the input(s) as fast as possible. This option will slow down the reading of the input(s) to the native frame rate of the input(s). It is useful for real-time output (e.g. live streaming).
- -i in file
- -vf video filter
- -c codec name
- -b:v especifica uma taxa de bits de vídeo
- -b:a especifica uma taxa de bits do audio
- -crf quality for constant quality mode
- -sc_threshold scene change threshold
- -g set the group of picture (GOP) size
- -keyint_min minimum interval between IDR-frames
- -hls_list_size set maximum number of playlist entries
- -hls_time set maximum number of playlist entries
- -f fmt force format

[Twitch transcoder](https://blog.twitch.tv/live-video-transmuxing-transcoding-ffmpeg-vs-twitchtranscoder-part-i-489c1c125f28)
[Seleção de dispositivos](http://4youngpadawans.com/stream-camera-video-and-audio-with-ffmpeg/)

# Listando os dispositivos

```bash
ffmpeg -list_devices true -f dshow -i dummy
```
