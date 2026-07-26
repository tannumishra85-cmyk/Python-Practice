note = open("notes.txt" , "a")

yes = True

while(yes):
    msg = input("Enter note(0 to exit): ")
    if(msg == "0"):
        break;
    else:
        note.write(msg)
        note.write("\n")

note.close()


note = open("notes.txt" , "r")
content = note.read()
print(content)
note.close()

