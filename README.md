## Halfbrick code taks

# Essential tasks

First three tasks where in included in data_analysis.py file with three function:

*csv_json

*data_summary 

*sql_insert

This python solution acts as cli(command line interface), i also made it user interface.

First user will be seeing a message to enter csv file name. (just the file name no .csv extension)

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


