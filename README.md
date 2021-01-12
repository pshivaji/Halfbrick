Shivaji parala
===========================================================

## Halfbrick code task

# Essential tasks

First three tasks where in included in data_analysis.py file with three function:

*csv_json

https://raw.githubusercontent.com/pshivaji/Halfbrick/main/results/task1_results.json

*data_summary:

![image info](results/task2_results.png)

*sql_insert:

https://raw.githubusercontent.com/pshivaji/Halfbrick/main/results/task3_results.txt
'''

This python solution acts as cli(command line interface), i also made it user interface.

When you run the code in command prompt, user will be seeing a message to enter csv file name. (just the file name no .csv extension)

Next user will be asked whether they want to convert given csv file to json file

futher, user will be asked whether they want to conduct some analysis on data. Bar and pie plots where impleented to explain the data insights.

Lastly, user will be asked whether they want to convert csv file to SQL insert into statements and when "y" results are generated.

we can simply run the code by following command in console

$ python data_anaysis.py

# Optional tasks:

Docker file was created adding the commands to exicute the python script

Command to create a image 

$ docker build -t my-python-app .

Command to run the image in a container

$ docker run -it --rm --name my-running-app my-python-app

#pip Packaging 

I have Setup tools and twine to generate package and publish it in pip.

You can access the package by 

```bash
pip install halfsolbrick
```
You can find the package in https://pypi.org/project/halfsolbrick/

Using the functions follow the folowing steps

```bash
from halfsolbrick import functions
```

```bash
functions.csv_json("input.csv") 
functions.data_summary ("input.csv") 
functions.sql_insert("input.csv") 
```




