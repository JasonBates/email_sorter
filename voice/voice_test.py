
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
#     print('=='*50)

# print(len(response.voices))


# audio = client.generate(
#      text=f"Hi I'm Adam Stone. this is a test of the Eleven labs API service called by the pythonAPI.  ",
#     voice='NFG5qt843uXKj4pFvR7C',
#     model="eleven_multilingual_v2"
# )
# play(audio)


audio = client.generate(
     text=f"Good morning Jason, today we're going to go through your emails and see what's happened in the world.",
    voice='vlEySMCLRrxQ1iLkJQsm',
    model="eleven_multilingual_v2"
)
play(audio)


# for voice in islice(response.voices, 14, 20):
#     audio_stream = client.generate(
#         text=f"Hi I'm {voice.name}, I'm {voice.labels['age']}, and {voice.labels['accent']} ",
#         voice=voice,
#         model="eleven_multilingual_v2",
#         stream=True
#     )
#     stream(audio_stream)

