from config import app, db
from controllers.controller import get_home, add_person
from controllers.route_controller import form, login

app.route('/')(get_home)
app.route('/add_person', methods=['POST'])(add_person)
app.route("/form")(form)
app.route("/login")(login)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)