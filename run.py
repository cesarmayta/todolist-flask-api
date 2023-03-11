from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/db_dotolist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

### crear una tabla con el ORM ###
class Tarea(db.Model):
    id = db.Column(db.Integer,primary_key=True) # id INT NOT NULL PRIMARY KEY
    descripcion = db.Column(db.String(200),nullable=False) # descripcion VARCHAR(200) NOT NULL
    estado = db.Column(db.String(100),nullable=False)
    
    def __init__(self,descripcion,estado):
        self.descripcion = descripcion
        self.estado = estado
        
db.create_all()
print("se creo la tabla tarea en la base de datos")
    
@app.route('/')
def index():
    context = {
        'status':True,
        'content':'servidor activo'
    }
    
    return jsonify(context)

app.run(debug=True)