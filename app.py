from flask import Flask, render_template,request
import predict
app = Flask(__name__)

user_input = 0
result = 0
lift_type = ""

@app.route("/", methods=['GET','POST'])
def hello_world():
    global user_input
    global result
    global lift_type
    result = 0
    if request.method == 'POST':
        user_input = request.form.get('Weight')
        lift_type = request.form.get('workout')
        benchmark = request.form.get('benchmark')

    # Fran
    if lift_type == "Clean and Jerk" and benchmark == "Fran" and user_input != ' ':
        result = predict.fran_clean(user_input)

    if lift_type == "Deadlift" and benchmark == "Fran" and user_input != ' ':
        result = predict.fran_dead(user_input)
        
    if lift_type == "Snatch" and benchmark == "Fran" and user_input != ' ':
        result = predict.fran_snatch(user_input)

    # Grace
    if lift_type == "Clean and Jerk" and benchmark == "Grace" and user_input != ' ':
        result = predict.grace_clean(user_input)

    if lift_type == "Deadlift" and benchmark == "Grace" and user_input != ' ':
        result = predict.grace_dead(user_input)

    if lift_type == "Snatch" and benchmark == "Grace" and user_input != ' ':
        result = predict.grace_snatch(user_input)

    #Helen
    if lift_type == "Clean and Jerk" and benchmark == "Helen" and user_input != ' ':
        result = predict.helen_clean(user_input)

    if lift_type == "Deadlift" and benchmark == "Helen" and user_input != ' ':
        result = predict.helen_dead(user_input)

    if lift_type == "Snatch" and benchmark == "Helen" and user_input != ' ':
        result = predict.helen_snatch(user_input)
        

    return render_template("index.html", result = result)
    