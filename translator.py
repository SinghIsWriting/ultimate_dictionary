from colorama import Fore, init
init(autoreset=True)
from googletrans import Translator, LANGUAGES
from gtts import gTTS
from playsound import playsound
from say import say_it

translator = Translator()

def show(text, origin, pronunciation):
	meaning = "Translated text"
	org = "Original word"
	pronun = "Pronunciation"
	print(f"{Fore.GREEN}\n{meaning:>20} :",text)
	print(f"{Fore.YELLOW}{org:>20} :",origin)
	print(f"{Fore.CYAN}{pronun:>20} :",pronunciation)

def any_to_any():
	ln = LANGUAGES
	count = 0
	for item in ln.keys():
		if count%2 == 0:
			print(f"{Fore.GREEN}{ln[item]:>22}",":",f"{Fore.YELLOW}"+item, end="\t")
		else:
			print(f"{Fore.GREEN}{ln[item]:>22}",":",f"{Fore.YELLOW}"+item)
		count += 1
	dlang = input("\n\nChoose a language in which you want to translate(e.g. fr): ")
	word = input("Enter your text(any language): ")
	try:
		translation = translator.translate(word, dest=dlang)
		show(translation.text, translation.origin, translation.pronunciation)
		say_it(translation.text, dlang, "anyToAny.mp3")
	except:
		print(f"{Fore.RED}\nOpps, something went wrong!")
	print()

def en_to_hi():
	try:
		text = input("Enter your text in English: ")
		translation = translator.translate(text,src='en',dest='hi')
		show(translation.text, translation.origin, translation.pronunciation)
		say_it(translation.text, "hi", "enToHi.mp3")
	except:
		print(f"{Fore.RED}Opps, something went wrong!")
	print()

if __name__ == "__main__":
	any_to_any()
	en_to_hi()
