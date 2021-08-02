# Tacotron-2-auto-Transcript
While using Tacotron 2 I found myself spending a long time to set up the transcript file. So, I made a simple python script to download transcript &amp; add those extra markers in every line. 

How to use:
- Open command prompt by typing cmd in windows search
- type: cd Download_location
- type: python Tacotron-2-auto-Transcript.py
- use 1 to download transcript
- use 2 to reformat file.

python packages to install:
- youtube-transcript-api (pip install youtube-transcript-api)
- 

What it does:
- It can download transcript from provided youtube video id & save it into a txt file.
- It adds /wav[number].wavs| {some txt} to every line.
- By default it downloads 'DY0ekRZKtm4' video transcript if you don't give an address. 

What it doesn't do:
- If transcription lines aren't organized or not separated by full sentences it doesn't separate it. 
- Doesn't add missing punctuationmarks.
  I tried to do it but it requires machine learning & I'm fairly new to coding.
  Infact this is my first original code. 
  
 What you can help with:
 - You can help with automatic punctuation marks.
 - Create a GUI & make it user friendly.
