from flask import Flask, render_template, url_for, request, redirect
import tensorflow as tf
from tensorflow import keras
import numpy as np

def machineLearn(array):
    inp = [array]

    model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape = (12,)),
            tf.keras.layers.Dense(30, activation = 'relu'),
            tf.keras.layers.Dense(30, activation = 'relu'),
            tf.keras.layers.Dense(30, activation = 'relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(3, activation = 'softmax')

    ])

    opt = keras.optimizers.Adam(learning_rate=0.9e-5)


    model.compile(optimizer = opt,
                    loss = 'categorical_crossentropy',
                    metrics = ['accuracy'])

    model.load_weights('final_checkpoint')

    #spit out output

    out = model.predict(inp)
    out = out[:1,:]
    if out[0][0] < 0.5:
        out[0][0] = 0.0
    else:
        out[0][0] = 1.0
    if out[0][1] < 0.5:
        out[0][1] = 0.0
    else:
        out[0][1] = 1.0
    return(out)



app = Flask(__name__)


a = 2.76916515450648
eq = .07600902910070946
inc = 10.59406704424526
om = 80.30553156826473
w = 73.597694115971
q = 2.558683599692926
ad = 2.979646709320033
per_y = 4.60820180153985

ma = 0
n =  0
per = 0
q2 = 0
h = 0

NEO = -1
PHA = -1
MOID = -1

@app.route('/', methods=['POST','GET'])
def index():
    if(request.method == "POST"):
        variableNames = ['eq','a', 'q', 'inc', 'om', 'w' , 'ma', 'n', 'per', 'ad', "per_y"]
        defaultVals = [ .07600902910070946, 2.76916515450648, 2.558683599692926, 10.59406704424526, 80.30553156826473, 73.597694115971, 0, 0, 0, 2.979646709320033, 4.60820180153985, 0]
        inputVals = []
        print(request.form)
        for i in variableNames:
            myInput = request.form[i]
            if(myInput == ""):
                inputVals.append(defaultVals[variableNames.index(i)])
            else:
                inputVals.append(float(myInput))
        if(request.form['q'] == ""):
            inputVals.insert(9,defaultVals[variableNames.index('q')])
        else:
           inputVals.insert(9,float(request.form['q']))        
        output = machineLearn(inputVals)
        newNEO = bool(output[0][0])
        newPHA = bool(output[0][1])

        return render_template("index.html",eq=inputVals[0], a=inputVals[1],q=inputVals[2], inc=inputVals[3],om=inputVals[4],w=inputVals[5],ma=inputVals[6],n=inputVals[7],per=inputVals[8],ad=inputVals[10], per_y=inputVals[11],NEO=newNEO,PHA=newPHA,MOID=output[0][2])
    else:
        return render_template("index.html",eq=eq, a=a, inc=inc,om=om, w=w, q=q,ad=ad,per_y=per_y,ma=ma,n=n,per=per,h=h,NEO=NEO,PHA=PHA,MOID=MOID)

if __name__ == '__main__':
    app.run(debug=True)
