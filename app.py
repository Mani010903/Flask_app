from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/v1/users", methods=["GET"])
def get_users():
    users = [
        {
            "id": 1,
            "name": "Mani Gupta",
            "email": "betu90104@gmail.com",
            "role": "Intern Developer"
        },
        {
            "id": 2,
            "name": "Test User",
            "email": "test@example.com",
            "role": "Developer"
        }
    ]
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)
