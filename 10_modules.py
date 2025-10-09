import os
import os.path
import sys
"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""
print("Task 1:")
directory = os.getcwd#create a variable for directory

print("Current working directory:", directory)#print the working directory

"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""
print("Task 2:")
print()
print()

# Create a new directory called 'test_folder' if it doesn't already exist
os.makedirs('test_folder', exist_ok=True)

# List all files and directories in the current directory
items = os.listdir('.')

# Print the list
print("Files and directories in current directory:")
for item in items:
    print(item)

print()
print()
print()


"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current 
working directory. If it doesn't exist, create it. If it does exist, print 
"Directory already exists."
"""
print("Task 3:")
print()
print()
# Define the directory name
dir_name = "data"

# Check if the directory exists
if os.path.isdir(dir_name):
    print("Directory already exists.")
else:
    os.makedirs(dir_name)
    print(f"Directory '{dir_name}' created.")
"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""
print("Task 4:")
filename = "config.txt"#creates a varibale for the filename

file_path = os.path.join(os.getcwd(), filename)#create file path by joining the current working directory and filename

if not os.path.isfile(file_path):#checks if the file is found
    print(f"File found at: {file_path}")
else:
    print("File not found.")

"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""
print("Task 5:")
print("Python version:", sys.version)#prints the python version

"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""
print("Task 6:")
platform_ID = sys.platform#creates a vairable for the platform IF
platform = {#creats a dictionary for the platform names
    'linux': 'linux',
    'win32': 'Windows',
    'darwin': 'MacOS',
    'e.g.,': 'e.g.,'
}
print("Platform:", platform.get(platform_ID, f"Unknown ({platform_ID})"))#prints the platform name or unknown