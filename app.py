from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('iri.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def main():
    return render_template('frontpage.html')

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == "POST":
        data1 = request.form['gender']
        if(data1=='male'):
            data1=1
        else:
            data1=0
        data2 = request.form['married']
        if(data2=='Yes'):
            data2=1
        else:
            data2=0
        data3 = request.form['education']
        if(data3=='Graduate'):
            data3=1
        else:
            data3=0
        data4 = request.form['employeed']
        if(data4=='Yes'):
            data4=1
        else:
            data4=0
        data5 = int(request.form['dependents'])
        data6 = int(request.form['credit_hist'])
        # #data7 = request.form['prop']
        # if(data7=='Urban'):
        #     data7=1
        # else:
        #     data7=0
        data8 = request.form['app_inc']
        data9 = request.form['coapp_inc']
        data10 = request.form['term']
        data11= request.form['amount']
        # print(data1)
        # print(data2)
        # print(data2)
        # print(data2)
        # print(data2)
        # print(data2)
        # print(data2)
        # print(data2)
        # print(data2)

    arr = np.array([[data1, data2, data5, data3, data4, data8, data9, data11, data10, data6]])
    print(arr)
    #arr = np.array([[1,0,0,1,0,5849,0,0,360,1]])
    pred = model.predict(arr)
    output = pred
    print(output)
    #return render_template('after.html', prediction_text=output)
    #render form again and add prediction
    return render_template('after.html',result=output)


if __name__ == "__main__":
    app.run(debug=True)
