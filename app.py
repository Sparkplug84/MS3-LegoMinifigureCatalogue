import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGODB_NAME"] = os.environ.get("MONGODB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
COLLECTION_NAME = "lego_catalogue"


mongo = PyMongo(app)

@app.route('/')
@app.route('/get_minifigures')
def get_minifigures():
    return render_template("minifigs.html", minifigures=mongo.db.minifigures.find())


@app.route('/add_minifig')
def add_minifig():
    return render_template('addminifig.html',
    themes=mongo.db.themes.find(),
    age=mongo.db.age.find(),
    parts=mongo.db.parts.find(),
    rarity=mongo.db.rarity.find())


@app.route('/insert_minifig', methods=['POST'])
def insert_minifig():
    if 'photo' in request.files:
        photo = request.files['photo']
        mongo.save_file(photo.filename, photo)
        mongo.db.minifigures.insert({'photo': photo.filename, 
                            'minifigure_name': request.form.get('minifigure_name'),
                            'theme_name': request.form.get('theme_name'),
                            'age_range': request.form.get('age_range'),
                            'feature': request.form.get('feature'),
                            'number_of_parts': request.form.get('number_of_parts'),
                            'rarity_name': request.form.get('rarity_name')})
    return redirect(url_for('get_minifigures'))


@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)