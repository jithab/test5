- https://rss.dw.com/xml/DKpodcast_topthemamitvokabeln_de
- All Scrips are inside scripts folder.

- Download Audio
```
yt-dlp -x --audio-format mp3  <url>
```
- Cut Audio
```
bash cut_audio.sh x.mp3 8.500 11.680
```
- Convert mp3 to vtt
```
bash audio2vtt.sh x.mp3 
```

- Convert vtt to json
```
python vtt2json.py x.vtt 
```