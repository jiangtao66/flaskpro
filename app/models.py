from . import db

registrations = db.Table('registrations', db.Column('student_id', db.Integer, db.ForeignKey('students.id')),
                         db.Column('class_id', db.Integer, db.ForeignKey('classes.id')))


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=True, unique=True)
    classes = db.relationship('Class', secondary=registrations,
                              backref=db.backref('students', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return '<Student %r>' % self.username


class Class(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __repr__(self):
        return "<Class %r>" % self.name