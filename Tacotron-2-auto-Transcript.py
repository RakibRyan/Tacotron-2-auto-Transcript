# Batch file for Tacotron 2
from youtube_transcript_api import YouTubeTranscriptApi


# Get transcript.

def write_transcript():
    id = str(input('Enter the video id to download transcript: '))
    default_id = 'DY0ekRZKtm4'

    if id == '':
        id = default_id

    transcript_txt = YouTubeTranscriptApi.get_transcript(id)

    with open('transcript.txt', 'a+') as transcript_object:
        transcript_object.seek(0)
        subtitles = transcript_object.read(100)
        if len(subtitles) > 0:
            transcript_object.write('\n')
        for i in transcript_txt:
            i = i['text']
            print(i)
            transcript_object.write(i + '\n')
    transcript_object.close()


# format extras.


def append_new_line(file_name):
    a = 'wavs/'
    b = '.wav|'
    c = 1
    with open(file_name, 'a+') as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write('\n')
        file_object.seek(0)
        lines = file_object.readlines()
        for i in lines:
            if not len(data) <= 0:
                line = str(a + str(c) + b + i)
                c = c + 1
                file_object.write(line)
                print(line)
    file_object.close()


loop = True

while loop:
    print('''Select option:
    1. Download Transcript
    2. Add reformat text
    
    ''')
    user_input = str(input())
    if user_input == '1':
        write_transcript()
    elif user_input == '2':
        append_new_line('transcript.txt')
    elif user_input == 'Exit' or 'exit' or 'exit()':
        loop = False
