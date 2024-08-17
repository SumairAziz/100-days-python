# simply for windows ----window voice

# import win32com.client
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# list = ["rana", "sumair", "Aziz"]
# for l in list:
#     speaker.speak(f"hello {l}")




#----------to use multiple voices-----------------#

import pyttsx3
# Initialize the converter
converter = pyttsx3.init()
#speed of voice
converter.setProperty("rate", 200)
#volume
converter.setProperty("volume", 2)
# Get available voices
voices = converter.getProperty('voices')
# Example list
names = ["rana", "sumair", "Aziz"]
# Iterate through voices and names
for i, name in enumerate(names):
    # Set voice (alternating between available voices)
    converter.setProperty('voice', voices[i % len(voices)].id)
    # Speak
    converter.say(f"Hello {name}")
# Wait for the speech to finish
converter.runAndWait()
