from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def start():
    return render_template('start.html')


@app.route("/calculated", methods=["POST"])
def calculate():
    first_number = float(request.form['first_number'])
    operator = request.form['operator']
    second_number = float(request.form['second_number'])
    if second_number != 0 and (operator != "/" or operator != "%"):
        if operator == "+":
            response = (first_number) + (second_number)
        elif operator == "-":
            response = (first_number) - (second_number)
        elif operator == "x":
            response = (first_number) * (second_number)
        elif operator == "/":
            response = (first_number) / (second_number)
        elif operator == "%":
            response = (first_number) % (second_number)
        elif operator == "^":
            response = (first_number) ** (second_number)
        given_number = response
        return render_template("calculated.html", number_three=given_number)
    else:
        return render_template("error_page.html")

if __name__ == "__main__":
    app.run(debug=True)
