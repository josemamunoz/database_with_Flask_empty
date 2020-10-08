from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Test(db.Model):
    __tablename__ = 'tests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)

    def save(self):
        db.session_add(self)
        db.session.commmit()

    def update():
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }