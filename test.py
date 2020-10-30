from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

myName = "ForALLAH"
ourName = "DIIIIII"

@app.route('/', methods=['POST','GET'])
def index():
    if(request.method == "POST"):
        variableNames = ['eq',"a", "q", "i", "om", "w", "ma" ,"n", "per", "ad", "per_y", "h"]
        inputVals = []
        print(request.form)
        for i in variableNames:
            inputVals.append(request.form[i])
        # enter = request.form['ogTest']
        print(inputVals)
        return render_template("test.html",myName=inputVals[0],ourName=inputVals[1])
    else:
        return render_template("test.html",myName=myName, ourName=ourName)

if __name__ == '__main__':
    app.run(debug=True)
