import os

translate = {"cane": "dog", "cavallo": "horse", "elefante": "elephant", "farfalla": "butterfly", "gallina": "chicken", "gatto": "cat", "mucca": "cow", "pecora": "sheep", "scoiattolo": "squirrel", "dog": "cane", "cavallo": "horse", "elephant" : "elefante", "butterfly": "farfalla", "chicken": "gallina", "cat": "gatto", "cow": "mucca", "spider": "ragno", "squirrel": "scoiattolo"}

dir_path = 'raw-img'
for entry in os.listdir(dir_path):
    #print(entry)

    entry_path = os.path.join(dir_path, entry)
    if not os.path.isdir(entry_path):
        continue
    print(entry)
    if entry in translate:
        new_name = translate[entry]
        new_path = os.path.join(dir_path, new_name)
        os.rename(entry_path, new_path)
