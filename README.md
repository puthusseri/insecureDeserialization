# insecureDeserialization
Code for explaining the concept of insecure deserialization and remote code execution


After running the exploit.py, you will get the serialized code for the class you defined,  Inside the reduce function, you can write your payload as the return value.
Here I had just used ls command to list the directory. ( If you are looking for reverse shell , do the logic here.)

Copy the serialized code which is the output of this program.


Run the file app.py to start the flask application. 
Type any name to register into the application. Which will take you to the second page. When you click the button to "LOAD YOUR HOME PAGE" you will get the third page, which tells that your are having user privilages.

So go back to the second page, edit the cookie named "serialized" and set its value as the serialized string you got as the output of the python program "exploit.py" 
then click the button again to load the home page. this time  the logic you write in the return function of exploit.py will gets executed. you can look at the terminal or logs to see that ls(ls is a command in linux os to list the directories) has executed.