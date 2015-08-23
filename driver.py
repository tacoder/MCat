from mcatcore import *
from guessit import *
files = getFileListRecursively("/media/abhinav/Multimedia/users/Movies")
filteredFiles= filterFilesByFormat(files)
for f in  filteredFiles:
    print f
    print guess_file_info(os.path.basename(f))
