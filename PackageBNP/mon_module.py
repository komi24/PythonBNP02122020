import sys
import os


def dire_bonjour():
    print("Bonjour tout le monde !")


print(__name__)
if __name__ == "__main__":
    print(os.listdir())
    print(f"Bonjour {sys.argv[1]}")
    dire_bonjour()
