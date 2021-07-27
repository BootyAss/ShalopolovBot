import os

from os import walk

filenames = next(walk('./'), (None, None, []))[2]  # [] if no file
print(filenames)

index = 0
for filename in filenames:
    file, ext = os.path.splitext(filename)
    os.rename(file + ext, 'photo' + '{:03d}'.format(index) + ext)
    index += 1

filenames = next(walk('./'), (None, None, []))[2]  # [] if no file
print(filenames)
