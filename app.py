from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import os

app = Flask(__name__)

# Connect to MongoDB (Container)
mongo_host = os.getenv("MONGO_HOST", "mongo")
mongo_port = int(os.getenv("MONGO_PORT", 27017))

client = MongoClient(f"mongodb://{mongo_host}:{mongo_port}/")
db = client["mydatabase"]
collection = db["names"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            collection.insert_one({"name": name})
        return redirect("/")
    return render_template("index.html")

@app.route("/names")
def show_names():
    names = collection.find()
    return render_template("names.html", names=names)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
