from .models import Role, User
from app import db

def create_admin():
    if User.query.filter(User.username=='admin').first() is None:
        admin_role = Role()
        admin_role.name='admin'
        admin_role.description='admin role'

        admin = User()
        admin.username = 'admin'
        admin.password = 'admin123'
        admin.email = 'admin.123@gmail.com'
        admin.roles = [
            admin_role
        ]
        admin.status = 'BOSS'
        admin.active = True

        db.session.add(admin)
        db.session.commit()


