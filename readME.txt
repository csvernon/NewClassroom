Install instructions:
1. Recommend following this tutorial to set up python in VS Code https://code.visualstudio.com/docs/python/python-tutorial
2. Install python interpreter from https://www.python.org/downloads/
3. Install the Python extension for VS Code from the Visual Studio Marketplace
4. Open VS code as Admin
5. Install needed dependensies by running terminal/powershell commands:
        pip install requests
        pip install flask
        python.exe -m pip install --upgrade pip
4. Open command prompt in NewClass folder
    ex: win key + cmd
    type cd C:\Users\****\downloads\NewClass
5. Run "python server.py"
6. Open web browser and paste http://localhost:5000/


Alternatively you could just run "python test.ty" in the terminal for a CLI output.

What works:
1. Count by Gender works and reports accurately
2. Count by Country works and reports accurately
3. CountPasswordComplexity does give a response but they are inaccurate, I have expanded on this in the defects mentioned below.

Defects:
1: Action type CountPasswordComplexity appears to be returning the password as "name".
Severity: Low

2. Action type CountPasswordComplexity is considering numberic characters towards complexity even though instructions state
Complexity will be considered the number of non-alphanumeric characters in the password.
Non-alphanumeric characters should only include ! @ # & ( ) – [ { } ] : ; ', ? / * ` ~ $ ^ + = < > “
Severity: High

3. When "–" is inserted in a password, it converts to "\u2013" in results. I ran across this when I copied non-alphanumeric characters
from a website and it should be noted that "-" is not the same as "–". My keyboards version of "-" does not suffer from this issue.
Severity: Very low
