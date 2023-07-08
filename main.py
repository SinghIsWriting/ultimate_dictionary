from colorama import Fore, init
init(autoreset=True)
import correction
import english_dictionary
import translator

def ultimate_dictionary():
    print("\n\t\t******************", f"{Fore.BLUE}Ultimate Dictionary", "******************\n")
    while(True):
        print("[1]      Translate English to Hindi\n[2]      Translate from and to any language\n[3]      Word Correction\n[4]      Define a Word\n[5]      Exit\n\n")
        try:
            usr = input("Enter your option: ")
            if usr == "1":
                translator.en_to_hi()
            elif usr == "2":
                translator.any_to_any()
            elif usr == "3":
                correction.correct()
            elif usr == "4":
                english_dictionary.means()
            elif usr == "5":
                print("\nThanks for using this script :)")
                break
            else:
                print(f"{Fore.RED}WARNING: Invalid Input!\n")
        except:
            print(f"{Fore.RED}WARNING: Invalid Input!\n")

if __name__ == "__main__":
    ultimate_dictionary()
