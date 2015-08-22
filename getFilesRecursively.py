from os import listdir
from os.path import isfile, join
def getFileListRecursively(rootFolderPath):
	folders = []
	files = []
	folders.append(rootFolderPath)
	while(len(folders)>0):
		curPath = folders.pop()
		folderContents = listdir(curPath)
		for f in folderContents:
			if isfile(join(curPath,f)):
				files.append(join(curPath,f))
			else:
				folders.append(join(curPath,f))
	return files

print (getFileListRecursively("/media/abhinav/Multimedia/users/Movies"))
