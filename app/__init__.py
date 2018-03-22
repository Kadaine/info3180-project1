from flask import Flask
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = 'Sup3r$3cretkey'
UPLOAD_FOLDER = "./app/static/uploads"

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://iuqvewujlrzqrw:292b72464af40add8d49404cc4fc56f3941e370f8245d16e38cc55d4531ec408@ec2-54-243-210-70.compute-1.amazonaws.com:5432/de69424rhl6am2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
db = SQLAlchemy(app)

app.config.from_object(__name__)

upload_f = app.config['UPLOAD_FOLDER']
Allowed_Uploads = ['jpg','png','jpeg']
app.debug= True
from app import views
