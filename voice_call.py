from gtts import gTTS
import os


def call_isp(download, upload):
    script = "I'm getting bandwidth throttled. Send a technician ASAP!"
    tts = gTTS(text=script, lang="en")
    tts.save("call.mp3")
    # Send to voice call service (e.g., Twilio)
    print("[Call] ISP has been 'prayer-called'.")

