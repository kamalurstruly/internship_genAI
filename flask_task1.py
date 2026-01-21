from flask import Flask, request

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return "Welcome to Flask App"

# MAIN TASK: Convert name to UPPERCASE
@app.route("/uppercase")
def uppercase_name():
    name = request.args.get("name", "Guest")
    return f"""
    <h1 style="color:blue;">🔥 HELLO {name.upper()} 🔥</h1>
    """


if __name__ == "__main__":
    app.run(debug=True)
