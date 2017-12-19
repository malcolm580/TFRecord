import os

path = os.path.join(os.path.sep, 'Users', 'youma', 'Downloads', 'raccoon_dataset-master - test', 'images', 'bottle')
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, 'bottle-' + str(i) + '.jpg'))
    i = i + 1
