#readfile
#open function-->Open the file
#read method --->Read the file
#seek method ---> change the cursor position
#tell method --->this method use for knowing the cursor position
#readline method-->Print 1 line in a file.
#readlines method --> Create a list all lines
#close method

#f=open('Files/text.txt')
#print(f"Cursor position: {f.tell()}")
#print(f.read())
#print(f"Cursor position: {f.tell()}")
#print("Before seek method")
#f.seek(0)
#
#print("after seek method")
#print(f"Cursor position: {f.tell()}")
#print(f.read())
#print(f"Cursor position: {f.tell()}")
#f.close()
f=open('Files/text.txt')
print(f.readlines())