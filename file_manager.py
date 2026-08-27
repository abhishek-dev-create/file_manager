#file manager version 1
#later i add more

from colorama import Fore, Back, Style, init
from pathlib import Path

init(autoreset=True)

print(Fore.GREEN + "-----========   File Manager   ========-----")
print(Fore.GREEN + "1. Rearrange different file types in different folder")
print(Fore.GREEN + "2. Exit")
print("")
run = True

while run:
    choice = int(input(Fore.YELLOW + "Enter your choice : "))

    if choice == 1:
        path = input(Fore.YELLOW + "----- Enter the path : ")
        target_path = Path(path)
        folders = [f.name for f in target_path.iterdir() if f.is_dir()]
        files = [f.name for f in target_path.iterdir() if f.is_file()]
        image = target_path / "Image"
        video = target_path / "Video"
        audio = target_path / "Audio"
        executables = target_path / "Executables"
        python = target_path / "Python"
        others = target_path / "Others"
        image.mkdir(parents=True, exist_ok=True)
        video.mkdir(parents=True, exist_ok=True)
        audio.mkdir(parents=True, exist_ok=True)
        executables.mkdir(parents=True, exist_ok=True)
        python.mkdir(parents=True, exist_ok=True)
        others.mkdir(parents=True, exist_ok=True)
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                _file = Path(target_path / file)
                _file.rename(image / file)
            elif file.lower().endswith((".mp4", ".mkv")):
                _file1 = Path(target_path / file)
                _file1.rename(video / file)
            elif file.lower().endswith(".mp3"):
                _file2 = Path(target_path / file)
                _file2.rename(audio / file)
            elif file.lower().endswith(".exe"):
                _file3 = Path(target_path / file)
                _file3.rename(executables / file)
            elif file.lower().endswith(".py"):
                _file4 = Path(target_path / file)
                _file4.rename(python / file)
            else:
                _file5 = Path(target_path / file)
                _file5.rename(others / file)
    elif choice == 2:
        print("")
        print(Fore.MAGENTA + "Bye ! ... Have a nice day")
        run = False
    else:
        print(Fore.RED + "Warning : Not a Valid Choice")
