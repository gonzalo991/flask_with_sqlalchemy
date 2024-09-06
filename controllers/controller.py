# from database.database import connection as db
from flask import request, jsonify, render_template, url_for, redirect
from sqlalchemy import select
from config import db
from database.models.Person import Person

def get_home():
    try:
        stmt = select(Person)
        persons = db.session.execute(stmt).scalars().all()
    except Exception as e:
        print(f'Couldnt find the persons: {e}')
        persons = []
    finally:
        db.session.close()
    return render_template("index.html", data = persons)

def add_person():
    try:
        name = request.form['name']
        surname = request.form['surname']
        age = request.form['age']
        gender = request.form['gender']

        new_person = Person(name, surname, age, gender)
        db.session.add(new_person)
        db.session.commit()
    except Exception as e:
        print(f'An error occurred: {e}')
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for("get_home"))