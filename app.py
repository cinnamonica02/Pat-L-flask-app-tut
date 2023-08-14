from flask import Flask, render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

#create an obj
app = Flask(__name__)
# routing the path to our db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#decorate the func w route
@app.route('/')
def index():
    return render_template('base.html')

#@app.route('/about')
#def about():
#    return 'About'

if __name__ == '__main__':
    # creating our db
    db.create_all()
    app.run(debug=True)