#set up server
#import packages
from flask import Flask, request, render_template, jsonify
from flask_pymongo import PyMongo
from flask import redirect, session, flash

#initialize
#this function initializes any application
app = Flask(__name__)
app.debug = True

app.secret_key = "sri"

#config
app.config["MONGO_URI"] = "mongodb://sridhar:asdf@cluster0-shard-00-00-aou9c.mongodb.net:27017,cluster0-shard-00-01-aou9c.mongodb.net:27017,cluster0-shard-00-02-aou9c.mongodb.net:27017/pat_reg?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority"
# app.config["MONGO_URI"] = "mongodb://sridhar:asdf@cluster0-aou9c.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route("/<a>/home", methods = ['GET', 'POST'])
def ajax(a):
    print(a)
    if a == "sridhar":
        return "Hello"
    else:
        return "This is a different org"

@app.route("/another", methods = ['GET', 'POST'])
def another():
    books = {"a":"b"}
    return jsonify(books)


#run
if __name__ == "__main__":
    app.run()