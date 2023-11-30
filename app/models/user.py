from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    mail = db.Column(db.Text)

    def __repr__(self):
        return f'<User "{self.name}">'