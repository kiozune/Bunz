Steps to setup Virtual environment and packages in pycharm
1. File --> Setting
2. Select Project-Bunz -- Python interpreter
3. Add local interpreter --> new interpreter
    a. example of the directory : C:\Users\yeeha\OneDrive\Documents\GitHub\Bunz
    b. just make sure the last directory is Bunz will do and
4.  in the terminal ( 5th on the nav bar at the bottom left of pycharm)
5. paste the following script and run
    a) .venv\Scripts\activate
6. File --> setting --> project --> project structure --> click on the .venv directory
   --> mark as sources (when ur folder become blue which mean you are on the correct path)

7. Use (python --version) in terminal to check if the presence of VE
8. if no then go back to the 1-2 steps, then click on the interpreter dropdown and select the interpreter as such
    a. Python 3.12 (Bunz)
    b. something like this
9. if yes continue to the next step by copy and paste the following command:
    a. pip install -r requirement.txt
 10. once installation success you should be able to run the app.py