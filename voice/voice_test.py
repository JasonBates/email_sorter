
from config.config import ELEVENLABS_API_KEY
from elevenlabs import play, stream
from elevenlabs.client import ElevenLabs
from itertools import islice
import json

client = ElevenLabs(
    api_key = ELEVENLABS_API_KEY
)    

# response = client.voices.get_all()
# for voice_pick in response.voices:
#     print(voice_pick.name)
# print(len(response.voices))


# audio = client.generate(
#      text=f"Hi I'm Adam Stone. this is a test of the Eleven labs API service called by the pythonAPI.  ",
#     voice='NFG5qt843uXKj4pFvR7C',
#     model="eleven_multilingual_v2"
# )
# play(audio)


# audio = client.generate(
#      text="Good morning Jason... what can I do for you today?",
#     voice='vlEySMCLRrxQ1iLkJQsm',
#     model="eleven_multilingual_v2"
# )
# play(audio)


# for voice in islice(response.voices, 22):
#     audio_stream = client.generate(
#         text=f"Hi I'm {voice.name}, I'm {voice.labels['age']}, and {voice.labels['accent']}.... what do you think? ",
#         voice=voice,
#         model="eleven_multilingual_v2",
#         stream=True
#     )
#     stream(audio_stream)


audio_stream = client.generate(
        text=f"Good morning! It's time to look at your emails for the day... starting out with personal requests, you have a lunch appointment with Charlie that you have to get back to him on, and a dinner reservation tonight at 8pm that you have to confirm ",
        voice='JBFqnCBsd6RMkjVDRZzb', # george
        model="eleven_multilingual_v2",
        stream=True
    )
stream(audio_stream)