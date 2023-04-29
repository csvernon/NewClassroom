Install instructions:
recommend following this tutorial to set up python in VS Code https://code.visualstudio.com/docs/python/python-tutorial
install python interpreter from https://www.python.org/downloads/
install the Python extension for VS Code from the Visual Studio Marketplace
Open VS code as Admin
install needed dependensies by running powershell commands:
    pip install requests
    pip install flask
    python.exe -m pip install --upgrade pip
open command prompt in NewClass folder
ex: win key + cmd
type cd C:\Users\****\downloads\NewClass
run "python server.py"
open web browser and paste http://localhost:5000/
Install "open in browser" extension by TechER

Alternatively you could just run "python test.ty" in the terminal for a CLI output.

What works:
1. Count by Gender works and reports accurately
2. Count by Country works

Defects:
1: Action type CountPasswordComplexity appears to be returning the password as "name".
2. Action type CountPasswordComplexity is considering numberic characters towards complexity even though instructions state
Complexity will be considered the number of non-alphanumeric characters in the password.
Non-alphanumeric characters should only include ! @ # & ( ) – [ { } ] : ; ', ? / * ` ~ $ ^ + = < > “
3. When "–" is inserted in a password, it converts to "\u2013" in results. I ran across this when I copied non-alphanumeric characters
from a website and it should be noted that "-" is not the same as "–". My keyboards version of "-" does not suffer from this issue.
