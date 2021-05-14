from flask import Flask,jsonify,request
app = Flask(__name__)
data = [
    {
        'id': 1,
        'Name': u'abc',
        'Contact': u'1234567890', 
        
    },
    {
        'id': 2,
        'Name': u'xyz',
        'Contact': u'1234567891',  
        
    }
]
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    task={
        'id': data[-1]['id']+1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact',""), 
       
    }
    data.append(task)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":data
    })
if (__name__=="__main__"):
    app.run(debug=True)