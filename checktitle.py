#Check if a string is formatted as a title. A title string is when every word of the string start with a upper case letter.

def checktitle(s):
    l=s.split()
    for i in l:
        if i[0].isupper() and len(i)==1:
            continue
        elif i[0].isupper() and i[1:].islower() and len(i)>1:
            continue
        else:
            print("Not a title string")
            break

    else:  
        print("Title string")

s=input("Enter a string: ")
checktitle(s)
