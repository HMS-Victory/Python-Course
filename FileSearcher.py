import os

print('Where do you want to search? (enter the complete path)')
rootFolder=input()
print('What type of file would you like to find? (if none press enter)')
fileType=input()
print('What Filename would you like to discover?')
filename=input()

for folderName, subfolders, filenames in os.walk(rootFolder):
    print('folder: '+folderName)
    print('subfolders: '+ str(subfolders))
    print('Files: '+ str(filenames))
    print()

    #Need to fix error os.join something or other.
    if filename != False:
        for subfolder in subfolders:
             if filename in subfolder:
                 print(os.join(folderName, filename))
    if fileType != False:
        for file in filenames:
            if file.endswith(fileType):
                print(os.join(folderName, file))

