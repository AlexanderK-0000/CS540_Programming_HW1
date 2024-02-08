Alexander Kerschen

Instructions for Running:
	download and install python from: https://www.python.org/downloads/
	Use cd to navigate into the directory containing HW1.py
	enter "python HW1.py"
	(Note: Using "python <file_path>/HW1.py" to run the script from outside the directory containing HW1.py, will cause option 5 (type/cat) to break)
	Once the script is running
		Option 1) Uses dir to print the contents of the working directory
		Option 2) Uses cd to print the file path of the working directory
		Option 3) Uses mkdir to create a new directory (will ask the user to input a name/path for the directory)
		Option 4) Uses echo to print a message to the console (will ask the user for the message)
		Option 5) Uses type to concatanating the contents of one file into another, and then print the contents of that file to the console
		Option 6) Exits the program
		
subprocess.run() vs os.system()
	subprocess.run() takes in the command you want to run as a list of strings
		EX: subprocess.run(['dir','/d'])
	os.system() takes a single string that it inputs directly to the shell as a command
		EX: os.system('dir /d')
	subprocess also has some additional functionality, like being able to save the output of the command
	Security:
		subprocess.run() is also condsidered more secure than os.system()
		As far as I understand, this is because subprocess.run() is more resiliant to shell injection
		For example:
			arg = input("argument")
			subprocess.run(['dir',arg])
			os.system(f'dir {arg}')
		Subprocess will only allow arg to be one argument because two or more arguments would have to be split into different list items
		OS, on the otherhand, will just run whatever string arg ends up making f"dir {arg}"
		So the user could input any number of things (like maybe a " & <entirely different command>") and os would just run it
		Something to note, I use subprocess's shell=True parameter in the homework
		This essentially makes it work like os
			EX: subprocess.run("dir /d", shell=True)
		Therefore, I'm really not getting the security benefit
		(I used shell=True for simplicity)
		(also, without shell=True, subprocess has some very annoying issues with running correctly on Windows, so I just avoided them)