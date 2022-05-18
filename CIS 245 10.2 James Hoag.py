#week 10 James Hoag
import os

directory = input("Enter the directory that you want to save the file : ")
filename = str(input("Enter the filename : "))
name = str(input("Enter your name : "))
address = str(input("Enter your address : "))
phone_number = input("Enter your phone number : ") #checking if the directory exists
if os.path.isdir(directory):
    with open(os.path.join(directory,filename),'w') #writing the data by comma seperated writeFile.write(name+','+address+','+phone_number+'\n') #close the file after writing is done
    writeFile.close()
    print("File contents:")
    with open(os.path.join(directory,filename),'r')
    for line in readFile:
        print(line)
        readFile.close()

    else:
        print("Sorry that directory is not exists...")



#what does the user enter as a directory? filename?
