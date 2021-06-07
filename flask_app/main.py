from app import application 
from app import db
app = application

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
