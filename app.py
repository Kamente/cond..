from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    messages = [
        "Incorrect",
        "Really?",
        "Wait, How Don't you Know?"
    ]

    message_index = 0

    if request.method == "POST":
        user_input = request.form["user_input"].lower()
        
        if user_input == "basketball":
            result = "How did you know?"
        else:
            result = messages[message_index]
            message_index = (message_index + 1) % len(messages)
        
        return render_template("index.html", result=result)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
