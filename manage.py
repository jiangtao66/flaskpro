#!./venv/bin/python

from flask_script import Manager, Shell

from app.models import registrations, Student, Class, db
from app import create_app

app = create_app()

manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, Student=Student, Class=Class, registrations=registrations)


manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()