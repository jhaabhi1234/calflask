from flask import Flask,request,url_for,render_template, jsonify
import json
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the app"

@app.route('/calc', methods=["Get"])
def math_operator():
    operator= request.json['operator']
    number1= request.json['number1']
    number2=request.json['number2']
    if operator=="add":
         result= int(number1)+int(number2)
    elif operator=="multiply":
        result = int(number1)*int(number2)
    elif operator=="division":
        if number2 == 0:
            return "Error: Division by zero"
        result=int(number1)/int(number2)
    elif operator=="subtract":
        result=int(number1)-int(number2)
    else:
        return "invalid request"    
    return jsonify({"result": result})           
    
    

if __name__=='__main__':
    app.run()
