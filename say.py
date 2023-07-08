from gtts import gTTS
from playsound import playsound

def say_it(text, lang, file_name):
	sound = gTTS(text, lang=lang)
	sound.save(file_name)
	playsound(file_name)

if __name__ == "__main__":
	say_it("some text", "hi")

