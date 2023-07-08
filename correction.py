from colorama import Fore, init
init(autoreset=True)
from textblob import TextBlob

def correct():
	words = []
	wd = input("Enter the words for correction: ")
	words.append(wd)
	corrected_words = []
	for i in words:
		corrected_words.append(TextBlob(i))
	print()
	print(f"{Fore.RED}Wrong words:", end=" ")
	for w in words:
		print(w, end=" ")
	print(f"{Fore.GREEN}\nCorrected Words are ", end="")
	for i in corrected_words:
		print(str(i.correct()), end=" ")
	print("\n")

if __name__ == "__main__":
	correct()
