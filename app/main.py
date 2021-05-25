#from flask import Flask
#app = Flask(__name__)

#@app.route("/")
#def hello():
 #   return "Our first Kubernetes app"

#if __name__ == "__main__":
 #   app.run(host='0.0.0.0', port=5000, debug=True)


from flask import Flask
APP = Flask(__name__)


@APP.route('/')
def hello_world():
    return 'Our first Kubernetes app'



if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)