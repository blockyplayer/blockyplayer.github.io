import pyaudio # Soundcard audio I/O access library
import wave # Python 3 module for reading / writing simple .wav files
import speech_recognition as sr
import requests
import time
from googlesearch import search

def speech_search():
    # Setup channel info
    FORMAT = pyaudio.paInt16 # data type formate
    CHANNELS = 1 # Adjust to your number of channels
    RATE = 44100 # Sample Rate
    CHUNK = 1024 # Block Size
    RECORD_SECONDS = 5 # Record time
    WAVE_OUTPUT_FILENAME = "temp.wav"
    # Startup pyaudio instance
    audio = pyaudio.PyAudio()
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    # for x in range(10):
    #     if x <= 3:
    #         print(f'\r Recording{'.'*x}', end="\r")
    #     elif x % 2 and not x % 4 and x > 3:
    #         print(f'\r Recording..', end='\r')
    #     elif x > 3 and x % 4 and x % 2:
    #         print(f'\r Recording.', end='\r')
    #     else:
    #         print('\r Recording...', end='\r')
    print('Recording...')
    frames = []

    # Record for RECORD_SECONDS
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Finished recording")


    # Stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Write your new .wav file with built in Python 3 Wave module
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    r = sr.Recognizer()


    base_url = "https://api.assemblyai.com"
    headers = {
        "authorization": "63426fbd53af430d911df5373d0455c3"
    }
    # You can upload a local file using the following code
    with open("temp.wav", "rb") as f:
        response = requests.post(base_url + "/v2/upload",
                                headers=headers,
                                data=f)
    audio_url = response.json()["upload_url"]
    data = {
        "audio_url": audio_url,
        "speech_model": "universal"
    }

    url = base_url + "/v2/transcript"
    response = requests.post(url, json=data, headers=headers)
    transcript_id = response.json()['id']
    polling_endpoint = base_url + "/v2/transcript/" + transcript_id
    while True:
        transcription_result = requests.get(polling_endpoint, headers=headers).json()
        transcript_text = transcription_result['text']
        if transcription_result['status'] == 'completed':
            print(f"Transcript Text:", transcript_text)
            break
        elif transcription_result['status'] == 'error':
            raise RuntimeError(f"Transcription failed: {transcription_result['error']}")
        else:
            time.sleep(3)
    query = transcript_text
    for j in search(query, num_results=10):
        print(j)
while True:
    speech_search()