from flask import Flask
from flask import render_template
import time
import collections
import setproctitle

app = Flask(__name__,template_folder='html')

setproctitle.setproctitle("HomeLights API")

#initialized as -1; does not change state until set to 1 or 0
lightsCurrentStatus = -1

@app.route("/lights/off",methods=["GET"])
def lightsOn():
    global lightsCurrentStatus
    lightsCurrentStatus = 0
    return "0"

@app.route("/lights/on",methods=["GET"])
def lightsOff():
    global lightsCurrentStatus
    lightsCurrentStatus = 1
    return "1"

@app.route("/lights/status",methods=["GET"])
def lightsStatus():
    global lightsCurrentStatus
    if (lightsCurrentStatus == 1):
        lightsCurrentStatus = -1
        return "1"
    if (lightsCurrentStatus == 0):
        lightsCurrentStatus = -1
        return "0"
    else:
        return "-1"


@app.route("/lights/",methods=["GET"])
def lightsInterface():
    return render_template("lightsInterface.html")

if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(host="0.0.0.0", port = "8002",threaded=True)


