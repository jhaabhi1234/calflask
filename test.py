from flask import Flask,request,url_for,render_template, jsonify
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the app"

@app.route('/calc', methods=["Get"])
def math_operator():
    operator= request.json()
    number1= request.json()
    number2=request.json()
    if operator=="add":
         result= number1+number2
    elif operator=="multiply":
        result = number1*number2
    elif operator=="division":
        if number2 == 0:
            return "Error: Division by zero"
        result=number1/number2
    elif operator=="subtract":
        result=number1-number2
    else:
        return "invalid request"    
    return result            
    
    

if __name__=='__main__':
    app.run()
