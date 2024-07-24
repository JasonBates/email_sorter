from elevenlabs import play, stream
from elevenlabs.client import ElevenLabs

class VoiceService:
    def __init__(self, API_key):
        self.voice = ElevenLabs(
            api_key = API_key
        )

    def set_voice(self, voice_id):
        self.voice_id = (voice_id)

    def generate_audio(self, text, voice_id):
        return self.voice.generate(
            text = text,
            voice = voice_id,
            model = "eleven_multilingual_v2"
        )
        

    def generate_audio_stream(self, text, voice_id):
        return self.voice.generate(
            text = text,
            voice = voice_id,
            model = "eleven_multilingual_v2",
            stream = True
        )

    def play_audio(self, audio_file):
        play(audio_file)

    def stream_audio(self, audio_stream):
        stream(audio_stream)
