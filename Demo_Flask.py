from flask import Flask
top = Flask(__name__)
@top.route("/")
def Index():
    return "hi everyone, i am aastha"
@top.route("/BVP")
def Msg():
    return"<h1>Good Morning</h1>"
if __name__=="__main__":
     top.run()