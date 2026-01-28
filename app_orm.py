from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create ORM object
db = SQLAlchemy(app)

# ORM model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"

# Create tables in DB
with app.app_context():
    db.create_all()

# Home route
@app.route("/")
def home():
    return "ORM practice app is running"

# Test route to add a user
@app.route("/add_user")
def add_user():
    existing_user = User.query.filter_by(email="mani@test.com").first() ## if the user is already exist
    if existing_user:
        return "User already exists!"
    user = User(first_name="Mani", last_name="Gupta", email="mani@test.com",
                phone="1234567890", password="hashedpassword")
    db.session.add(user)
    db.session.commit()
    return "User added!"

# Endpoint to fetch all users
@app.route("/v1/users", methods=["GET"])
def get_users():
    users = User.query.all()  # Fetch all users from the DB
    # Convert ORM objects to dictionary
    users_list = [
        {
            "id": u.id,
            "first_name": u.first_name,
            "last_name": u.last_name,
            "email": u.email,
            "phone": u.phone
        } for u in users
    ]
    return {"users": users_list}, 200


if __name__ == "__main__":
    app.run(debug=True)
