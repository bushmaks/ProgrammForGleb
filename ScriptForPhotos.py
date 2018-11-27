import os, sys

path = sys.argv[1] + "\\"

listOfDirs = []

for dirname, dirnames, filenames in os.walk(path):
    for dir in dirnames:
        listOfDirs.append(dir)

for dir in listOfDirs:
    count = 0
    for file in os.listdir(path + dir):
        count += 1
        os.rename(path + dir + "\\" + file, path + dir + "\\" + dir + str(count) + '.jpg')
