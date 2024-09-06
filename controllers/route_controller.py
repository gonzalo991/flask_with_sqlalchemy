from flask import render_template

def form():
    return render_template("form.html")

def login():
    return render_template("login.html")