import os

#Select a directory to list its contents
directory = "/"

#Use the os module to list the contents of the directory 
contents = os.listdir(directory)

#Print the contents of the directory
print(contents)