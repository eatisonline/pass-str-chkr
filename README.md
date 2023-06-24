The goal of this project was to develop a security automation Python script that will prompt the user for an input file path, read the usernames and passwords from the file, and check the overall password strength based on specified criteria. This script will identify the weak passwords and display both the weak passwords and their corresponding usernames.


Scope: 
User input: Prompts the user to enter an input file path.
File handling: Read the input file and extract the usernames and passwords.
Password strength checking: Program checks for password length “> 8, < 50” characters, one special character, one number, and one uppercase letter.
Weak password identification: Identify weak passwords based on previously defined criteria.
Display results: Prints the weak passwords along with their corresponding usernames.

Timeline:
Day 1: Project setup and research
Day 2: Script development for file handling and password strength checking.
Day 3: Testing, fixing bugs, and finalizing the script.
Day 4: Documentation, final review, and project submission.

Deliverables:
Python script: The final script that prompts for an input file, checks password strength, and displays weak passwords along with their corresponding usernames.
Project documentation: Documentation explaining the project scope, timeline, constraints, and other information can be found here: https://github.com/eatisonline/pass-str-chkr

Constraints:
The input file will be in a specific format with each line containing a username and password separated by a colon.
The script will only consider the password portion for password strength checking.
The script will not perform any modifications to the input file or the passwords.
