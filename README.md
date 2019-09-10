# Streaming

- ffmpeg -i input.mp4 -profile:v baseline -level 3.0 -s 640x360 -start_number 0 -hls_time 10 -hls_list_size 0 -f hls index.m3u8
- ffmpeg -i input.mp4 -vf scale=w=1280:h=720:force_original_aspect_ratio=decrease -c:a aac -ar 48000 -c:v h264 -profile:v main -crf 20 -sc_threshold 0 -g 48 -keyint_min 48 -hls_playlist_type vod -b:v 2800k -maxrate 2996k -bufsize 4200k -b:a 128k -hls_time 10 -hls_list_size 0 -f hls index.m3u8

**1080p**:

- scale=w=1920:h=1080:force_original_aspect_ratio=decrease
- -b:v 5000k
- -maxrate 5350k
- -bufsize 7500k
- -b:a 192k

**720p**:

- -scale=w=1280:h=720:force_original_aspect_ratio=decrease
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

- -i in file
- -vf video filter
- -c codec name
- -crf quality for constant quality mode[
- -sc_threshold scene change threshold (from INT_MIN to INT_MAX) (default 0)
- -g set the group of picture (GOP) size (from INT_MIN to INT_MAX) (default 12)
- -keyint_min minimum interval between IDR-frames
- -hls_list_size set maximum number of playlist entries (from 0 to INT_MAX) (default 5)
- -hls_time set maximum number of playlist entries (from 0 to INT_MAX) (default 5)
- -f fmt force format
