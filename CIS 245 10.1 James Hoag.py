#CIS 245 10.2
#James Hoag

import os.path
#program would not work without def main function
def main():
    directory = raw_input("Enter the directory that you want to save the file : ") #need to enter 'os'
    filename = raw_input("Enter the filename : ")
    name = raw_input("Enter your name : ")
    address = raw_input("Enter your address : ")
    phone_number = raw_input("Enter your phone number : ")
    if os.path.isdir(directory):
        writeFile = open(os.path.join(directory,filename+".txt"),'w') #writing the data 
        writeFile.close() #close the file after writing is done
        print("File contents:")
        readFile = open(os.path.join(directory,filename),'r') #read the data the user entered into the file
    for line in readFile:  #looping through the data entered
        print(line)
        readFile.close()

    else:
        print("Sorry that directory is not exists...")

main()

