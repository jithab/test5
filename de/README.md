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

```
Perform a pedagogical translation from German to English. Target language: English. Source language: German. Translation style: Calque (loan translation). Priority: Faithful to source structure. Priority: Faithful to source words. Priority: Pedagogical value for German learners. Avoid: Idiomatic English. Avoid: Natural-sounding English. Avoid: Changing word meanings. Explanation: The user is learning German and needs to see the direct correspondence between words and sentence structure. Output: Only the completed JSON object.
```