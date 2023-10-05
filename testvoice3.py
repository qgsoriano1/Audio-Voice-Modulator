import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set the voice to the toad from Super Mario
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

# Say something
text = 'Hey, Barbara! Maybe I can get you some wine My Sylvia! How can I say that you are mine? Hey, Beverly! Eyes are blue from what I can see Hey, Stephanie! So you wanna dance with me?'
engine.say(text)

# Save the audio to a file
engine.save_to_file(text, 'C:\\Users\\GSori\\OneDrive\\Documents\\4thYear\\DSPA\\AI_output2.wav')

# Wait for the speech to be generated and saved to the file
engine.runAndWait()
