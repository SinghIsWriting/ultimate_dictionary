from colorama import Fore, init
init(autoreset=True)
import requests

def means():
    try:
        text = input("Enter your word: ")
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{text}"
        meaning = requests.get(url).json()

        txtMeaning = str(meaning[0]['meanings'][0]['definitions'][0]['definition'])

        print("\n"+text.title() + ":", f"{Fore.GREEN}"+txtMeaning)
        print()
    except:
        print(f"{Fore.YELLOW}WARNING: Opps, something went wrong!\n")
if __name__ == "__main__":
    means()
