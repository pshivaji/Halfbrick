import argparse
import os 
import pandas as pd
import json
import matplotlib.pyplot as plt
import csv

inputString = input("Provide the csv file name : ")

p = inputString +".csv"
    
#os.chdir("C:\\Users\\pshiv\\Downloads")

# coverting csv file json file 
def csv_json(d):
    df = pd.read_csv(d)
    result = df.to_json(orient="index")
    parsed = json.loads(result)
    
    # Serializing json  
    json_object = json.dumps(parsed, indent = 4) 
  
    print(json_object)

    
# Data summary
def data_summary(d):
    df = pd.read_csv(d)
    df['device_language'].value_counts()[1:20].plot(kind="bar")
    plt.show()
    df['sku'].value_counts().plot(kind="bar",color="green")
    plt.show()
    df['ua_source'].value_counts().plot(kind="bar",color="red")
    plt.show()

    
    
    # 
def sql_insert(p):
    file = open(p, 'r',encoding="utf8")
    read = csv.reader(file)
    header_list = next(read)
    headers_list = map((lambda q: '"'+q+'"'), header_list)
    insert_list = 'INSERT INTO Table (' + ", ".join(headers_list) + ") VALUES "
    
    for row in read:
        val = map((lambda q: "'"+q+"'"), row)
        print(insert_list +"("+ ", ".join(val) +");")

    file.close()
    print("SQL inserts statements created in a results txt file")
    

if __name__ == '__main__':   
    # user inputs
    i = input("Do you want convert csv to json file(y/n): ")
    if i == "y" :
        csv_json(p)
    
    j = input("Do you want summary of the data(y/n): ")
    if j == "y" :
        data_summary(p)

    k = input("convert to sql statements(y/n): ")
    if k == "y" :
        sql_insert(p)

    