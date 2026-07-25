note = open("notes.txt" , "a")

n = input("Enter a note: ")

note.write(n)
note.write("\n")
note.close()


# Read and Print all the notes avail in notes.txt
note = open("notes.txt" , "r")
content = note.read()
print(content)
note.close()
