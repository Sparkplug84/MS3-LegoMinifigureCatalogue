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
    minifigures = mongo.db.minifigures.find({"minifig_deleted": False})
    return render_template("minifigs.html", minifigures=minifigures)


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
        mongo.db.minifigures.insert_one({'photo': photo.filename, 
                            'minifigure_name': request.form.get('minifigure_name'),
                            'theme_name': request.form.get('theme_name'),
                            'age_range': request.form.get('age_range'),
                            'feature': request.form.get('feature'),
                            'number_of_parts': request.form.get('number_of_parts'),
                            'rarity_name': request.form.get('rarity_name'),
                            'minifig_deleted': False})
    return redirect(url_for('get_minifigures'))


@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)


@app.route('/edit_minifig/<minifigure_id>')
def edit_minifig(minifigure_id):
    the_minifig = mongo.db.minifigures.find_one({"_id": ObjectId(minifigure_id)})
    all_themes = mongo.db.themes.find()
    all_age = mongo.db.age.find()
    all_parts = mongo.db.parts.find()
    all_rarity = mongo.db.rarity.find()
    return render_template('editminifig.html', minifigure=the_minifig, themes=all_themes, age=all_age, parts=all_parts, rarity=all_rarity)


@app.route('/update_minifig/<minifigure_id>', methods=['POST'])
def update_minifig(minifigure_id):
    mongo.db.minifigures.update_one({'_id': ObjectId(minifigure_id)},
    { "$set": {
        'minifigure_name': request.form.get('minifigure_name'),
        'theme_name': request.form.get('theme_name'),
        'age_range': request.form.get('age_range'),
        'feature': request.form.get('feature'),
        'number_of_parts': request.form.get('number_of_parts'),
        'rarity_name': request.form.get('rarity_name')
    }})
    return redirect(url_for('get_minifigures'))


@app.route('/delete_minifig/<minifigure_id>')
def delete_minifig(minifigure_id):
    mongo.db.minifigures.update_one({'_id': ObjectId(minifigure_id)},
    { "$set": {
        'minifig_deleted': True }
    })
    return redirect(url_for('get_minifigures'))


@app.route('/get_themes')
def get_themes():
    return render_template('themes.html', themes=mongo.db.themes.find())


@app.route('/edit_theme/<theme_id>')
def edit_theme(theme_id):
    return render_template('edittheme.html', theme=mongo.db.themes.find_one({'_id': ObjectId(theme_id)}))


@app.route('/update_theme/<theme_id>', methods=['POST'])
def update_theme(theme_id):
    mongo.db.themes.update_one({'_id': ObjectId(theme_id)},
    { "$set": {
        'theme_name': request.form.get('theme_name') }
    })
    return redirect(url_for('get_themes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)