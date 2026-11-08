import math
from flask import Flask

app = Flask(__name__)

def onko_alkuluku(luku):
    if luku <= 1:
        return False

    for i in range(2, int(math.sqrt(luku)) + 1):
        if luku % i == 0:
            return False

    return True

@app.route("/alkuluku/<int:luku>")
def alkuluku(luku):
    vastaus = {
        "Number": luku,
        "isPrime": onko_alkuluku(luku)
    }
    return vastaus

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)