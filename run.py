from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        'status':True,
        'content':'servidor activo'
    }
    
    return jsonify(context)

app.run(debug=True)