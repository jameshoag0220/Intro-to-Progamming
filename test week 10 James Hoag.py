#testweek10
#James Hoag
import os
#program would not work without def main function
def main():
    directory = input("Enter the directory that you want to save the file : ") #need to enter 'os'
    filename = input("Enter the filename : ")
    name = input("Enter your name : ")
    address = input("Enter your address : ")
    phone_number = input("Enter your phone number : ") 
    if os.path.isdir(directory):
        writeFile = open(os.path.join(directory,filename),'w') #writing the data 
        writeFile.close() #close the file after writing is done
        print("File contents:")
        readFile = open(os.path.join(directory,filename),'r') #read the data the user entered into the file
    for line in readFile:  #looping through the data entered
        print(line)
        readFile.close()

    else:
        print("Sorry that directory is not exists...")

main()

#what does the user enter as a filename?
