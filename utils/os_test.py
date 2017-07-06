from os import path

current_dir = path.dirname(__file__) #mamy dostep do sciezki pliku niezalezenie od tego gdzie jestesmy

print(current_dir)

print(path.join(current_dir, 'subfolder', 'module.py'))