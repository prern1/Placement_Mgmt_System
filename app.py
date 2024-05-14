import json 
from flask import Flask, jsonify,request
from csv import DictReader, DictWriter
from tempfile import NamedTemporaryFile
from flask_cors import CORS
import shutil
import os

data=[]
temp_data=[]



app= Flask(__name__)
CORS(app)

def read_csv():
   with open('./student.csv','r') as file:
    csv_reader = DictReader(file,
    fieldnames=('RollNumber','FirstName', 'LastName', 'Age','Course'),
    lineterminator='\n'
        )
    next(csv_reader)
    #data=csv_reader.reader
    data = list(csv_reader)
    print(data)
    return(data)
   
def read_csv1(Roll):
   with open('./student.csv','r') as file:
    csv_reader = DictReader(file,
    fieldnames=('RollNumber','FirstName', 'LastName', 'Age','Course'),
    lineterminator='\n'
        )
    next(csv_reader)
    #data=csv_reader.reader
    data = list(csv_reader)
    for row in data:  
        if int(row['RollNumber'])==int(Roll):
            temp_data1=[]

    
            temp_data1.append(row)
    return(temp_data1)
   
   
def write_csv(data):
    with open('./student.csv', 'a') as file:
        csv_writer = DictWriter(file,
        fieldnames=('RollNumber','FirstName', 'LastName', 'Age','Course'),
        lineterminator='\n'
            )
        
        csv_writer.writerow(data)

    
def delete_csv(Roll):
    with open('./student.csv') as file:
        csv_reader = DictReader(file,
    fieldnames=('RollNumber','FirstName', 'LastName', 'Age','Course'),
    lineterminator='\n'
        )
        next(csv_reader)
        data = list(csv_reader)
        
        for row in data:  
         if int(row['RollNumber'])==Roll:
            continue
         temp_data.append(row)
            
    with open('./student.csv','w') as file:
        csv_writer = DictWriter(file,
        fieldnames=('RollNumber','FirstName', 'LastName', 'Age','Course'),
        lineterminator='\n'
            )
        print(data)
        csv_writer.writeheader()
        csv_writer.writerows(temp_data)

def update_csv(Roll , new_data):
    with open('./student.csv') as file:
        csv_reader = DictReader(file,
    fieldnames=('RollNumber','FirstName', 'LastName', 'Age','Course'),
    lineterminator='\n'
        )
        next(csv_reader)
        data = list(csv_reader)
        for row in data:  
         if int(row['RollNumber'])==Roll:
            print(row['RollNumber'])
            print(Roll) 
            row['RollNumber']=new_data['RollNumber']
            row['FirstName']=new_data['FirstName']
            row['LastName']=new_data['LastName']
            row['Age']=new_data['Age']
            row['Course']=new_data['Course']
            print(new_data)
    with open('./student.csv','w') as file:
        csv_writer = DictWriter(file,
        fieldnames=('RollNumber','FirstName', 'LastName', 'Age','Course'),
        lineterminator='\n'
            )
        print(data)
        csv_writer.writeheader()
        csv_writer.writerows(data)
        
        
    

    

@app.route('/student', methods=['GET'])
def get_students():
    print(json.dumps(read_csv()))
    return json.dumps(read_csv())

@app.route('/student/<int:Roll>', methods=['GET'])
def get_students1(Roll:int):
    #print(json.dumps(read_csv1(Roll)))
    return json.dumps(read_csv1(Roll))



@app.route('/student', methods =['POST'])
def create_student():
    
    write_csv(request.form.to_dict())
    return jsonify([{'status':1},{'msg':'record inserted successfully'}]),201
        


@app.route('/student/<int:Roll>', methods=['PUT'])
def update_student(Roll:int):
    print(request.form.to_dict())
    update_csv(Roll,request.form.to_dict())
   
   
    return jsonify([{'status':1},{'msg':'record updated successfully'}]),201




@app.route('/student/<int:roll>', methods=['DELETE'])
def delete_student(roll:int):
    delete_csv(roll)
    return jsonify([{'status':1},{'msg':'record deleted successfully'}]),201


@app.route('/studentu/<int:Roll>', methods=['PUT'])
def update_student1(Roll:int):
    print(request.form.to_dict())
    update_csv(Roll,request.form.to_dict())
   
   
    return jsonify([{'status':1},{'msg':'record updated successfully'}]),201

app.run()