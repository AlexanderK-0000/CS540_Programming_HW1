#Alexander Kerschen
import subprocess
#subprocess.run() is being used to run the shell commands
#it is condsidered more secure than os.system() (Check README.txt for more information)
#shell=True make it so that whatever is put into the quotations marks is just inputed directly into the shell

#Prints a message to the console if a command returns a non-zero code
def ErrorHandling(output):
    #subprocess.run returns a CompletedProcess Object (output)
    #it has an attribute args, that is the command that was ran
    #it has an attibute returncode, that is the value of the code returned after the command was executed (non-zero generally means an error occured)
    if output.returncode != 0:
        subprocess.run(f'echo Command "{output.args}" returned non-zero code: {output.returncode}', shell=True)

#Loops until it hits the break in option 6
while(True):
    n = " & echo " #used as \n, more or less
    #displays the menu using echo
    subprocess.run(f"echo: & echo:{n}1)List directory contents{n}2)Print working directory{n}3)Create a new directory{n}4)Display a message{n}5)Concatenate and display content of a file{n}6)Exit & echo:", shell=True)

    choice = input("Select an Option: ") #user chooses a menu option

    subprocess.run("echo: ", shell=True)#makes an empty line
     
    #most of the command explanation I was going to make comments for just ended up as part of the explanation I print to the shell when the option is selected
    #so if you want to know what the shell commads do, just read the string after the echo command in each if statement
    if choice == "1": #List directory contents (dir/ls)
        subprocess.run(f'echo Runs the command: "dir"{n}prints the contents of the current working directory{n}Entering a file path to a directory into dir as an argument will print the contents of that directry instead{n}Command Output:', shell=True)
        output = subprocess.run("dir", shell=True) 
        ErrorHandling(output)
    elif choice == "2": #print working directory (cd/pwd)
        subprocess.run(f'echo Runs the command: "cd"{n}This prints the file path to the working directory{n}Entering a file path into cd as an argument will move the working directory to that position{n}Command Output:', shell=True)
        output = subprocess.run("cd", shell=True)
        ErrorHandling(output)
    elif choice == "3": #make a directory (mkdir)
        path = input("Input the name of the new directory: ") 
        subprocess.run(f'echo Runs the command: "mkdir <inputed_name>"{n}This creates a new directory called the previously inputed name in the current working directory{n}A file path can be specified before the name to create the directory in that position, rather than the working directory{n}Command Output:', shell=True)
        output = subprocess.run(f"mkdir {path}", shell=True) 
        ErrorHandling(output)
    elif choice == "4": #display a message (echo)
        message = input("Input the message you would like to display: ") 
        subprocess.run(f'echo Runs the command: "echo <inputed_message>"{n}This prints the previously inputed message to the console{n}Command Output:', shell=True)
        output = subprocess.run(f"echo {message}", shell=True)
        ErrorHandling(output)
    elif choice == "5": #concat/print a file (type/cat)
        subprocess.run(f'echo Runs the command: "type sender.txt >> reciever.txt && type reciever.txt"{n}"type sender.txt >> reciever.txt" adds the contents of sender.txt onto the end of reciever.txt{n}"type reciever.txt" prints the contents of reciever.txt to the console{n}Command Output:', shell=True)
        output = subprocess.run("type sender.txt >> reciever.txt && type reciever.txt", shell=True)
        ErrorHandling(output)
    elif choice == "6": #Exit
        break #Exits the loop, ending the program
    else:#a number not 1-6
        subprocess.run("echo Please choose a number from the menu.", shell=True)
        