from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    celsius = request.args.get("celsius", "")
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""
    return (
        """<form action="" method="get">
                <div style="background-color: red; color: purple; font-size: 2.6em">
                Celsius temperature: <input type="text" name="celsius" value=""" + celsius + """>
                <input type="submit" value="Convert to Fahrenheit">
            </div>
            </form>"""
        + "Fahrenheit: "
        + fahrenheit
    )

def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
