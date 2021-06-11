from app import application 
from app import db
app = application

if __name__ == '__main__':
    db.create_all()
    from app.create_admin import create_admin
    create_admin()
    app.run(host='0.0.0.0')
