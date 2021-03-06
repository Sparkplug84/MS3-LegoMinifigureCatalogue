import os
from functools import wraps
from flask import Flask, flash, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGODB_NAME"] = os.environ.get("MONGODB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
COLLECTION_NAME = "lego_catalogue"
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route('/')
@app.route('/index_page')
def index_page():
    # displays home page with message if user logged in
    if 'username' in session:
        return render_template('index.html',
                                text='You are logged on as ' + session['username'])
    return render_template('index.html')


@app.route('/login_form')
def login_form():
    # displays the log in form
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    # Checks if user exists and logs user in, errors if wrong password/username
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'),
                        login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index_page'))

    return render_template('login.html',
                            text='* Invalid username/password combination. Please try again...')


@app.route('/register', methods=['POST', 'GET'])
def register():
    # Registers and logs in a new user, errors id username alredady exists
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.form['username'], 'password': hashpass, 'liked_items': []})
            session['username'] = request.form['username']
            return redirect(url_for('index_page'))
        return render_template('register.html',
                                text='* That username already exists, please try another...')

    return render_template('register.html')


def login_required(f):
    # this is a wrap function which wraps around other routes to first check if a user is logged in before continuing with the function.
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'username' in session:
            return f(*args, **kwargs)
        else:
            return render_template('login.html',
                            text='* You need to be logged in to continue!')
    return wrap


@app.route('/log_out')
@login_required
def log_out():
    # this will log a user out of the session
    session.clear()
    return redirect(url_for('index_page'))


@app.route('/get_minifigures')
def get_minifigures():
    # this will retrieve all the minifigure records from Mongo and display them
    minifigures = mongo.db.minifigures.find({"minifig_deleted": False})
    minifigures = list(minifigures)[::-1]
    return render_template(
        "minifigs.html",
        minifigures=minifigures,
        themes=mongo.db.themes.find(),
        age=mongo.db.age.find())


@app.route('/add_minifig')
@login_required
def add_minifig():
    # This will display the page and form for adding a minifigure
    return render_template('addminifig.html',
                           themes=mongo.db.themes.find(),
                           age=mongo.db.age.find(),
                           parts=mongo.db.parts.find(),
                           rarity=mongo.db.rarity.find())


@app.route('/insert_minifig', methods=['POST'])
@login_required
def insert_minifig():
    # This will take the info from the form and save it onto the Monog database
    if 'photo' in request.files:
        photo = request.files['photo']
        mongo.save_file(photo.filename, photo)
        mongo.db.minifigures.insert_one({'photo': photo.filename,
                                         'minifigure_name': request.form.get('minifigure_name').lower(),
                                         'theme_name': request.form.get('theme_name'),
                                         'age_range': request.form.get('age_range'),
                                         'feature': request.form.get('feature').lower(),
                                         'number_of_parts': request.form.get('number_of_parts'),
                                         'rarity_name': request.form.get('rarity_name'),
                                         'uploaded_by': session['username'],
                                         'minifig_deleted': False,
                                         'liked_counter': 0})
    return redirect(url_for('get_minifigures'))


@app.route('/file/<filename>')
def file(filename):
    # This will retrieve and store the images uploaded onto Mongo
    return mongo.send_file(filename)


@app.route('/edit_minifig/<minifigure_id>')
@login_required
def edit_minifig(minifigure_id):
    # This route displays the edit minifigure form with existing info already filled in
    the_minifig = mongo.db.minifigures.find_one(
        {"_id": ObjectId(minifigure_id)})
    all_themes = mongo.db.themes.find()
    all_age = mongo.db.age.find()
    all_parts = mongo.db.parts.find()
    all_rarity = mongo.db.rarity.find()
    return render_template('editminifig.html', minifigure=the_minifig, themes=all_themes, age=all_age, parts=all_parts, rarity=all_rarity)


@app.route('/update_minifig/<minifigure_id>', methods=['POST'])
@login_required
def update_minifig(minifigure_id):
    # this will take the info from the edit form and send it to Mongo to update the record
    mongo.db.minifigures.update_one({'_id': ObjectId(minifigure_id)},
                                    {"$set": {
                                        'minifigure_name': request.form.get('minifigure_name').lower(),
                                        'theme_name': request.form.get('theme_name'),
                                        'age_range': request.form.get('age_range'),
                                        'feature': request.form.get('feature').lower(),
                                        'number_of_parts': request.form.get('number_of_parts'),
                                        'rarity_name': request.form.get('rarity_name')
                                    }})
    return redirect(url_for('get_minifigures'))


@app.route('/delete_minifig/<minifigure_id>')
@login_required
def delete_minifig(minifigure_id):
    # The delete route will hide the record from view of user but not completely delete from database
    mongo.db.minifigures.update_one({'_id': ObjectId(minifigure_id)},
                                    {"$set": {
                                        'minifig_deleted': True}
                                     })
    return redirect(url_for('get_minifigures'))


@app.route('/get_themes')
@login_required
def get_themes():
    # Renders the themes page
    return render_template('themes.html', themes=mongo.db.themes.find())


@app.route('/edit_theme/<theme_id>')
@login_required
def edit_theme(theme_id):
    # Renders the edit theme form
    return render_template('edittheme.html', theme=mongo.db.themes.find_one({'_id': ObjectId(theme_id)}))


@app.route('/update_theme/<theme_id>', methods=['POST'])
@login_required
def update_theme(theme_id):
    # takes the info in the form and updates the theme in the database
    mongo.db.themes.update_one({'_id': ObjectId(theme_id)},
                               {"$set": {
                                   'theme_name': request.form.get('theme_name').lower()}
                                })
    return redirect(url_for('get_themes'))


@app.route('/delete_theme/<theme_id>')
@login_required
def delete_theme(theme_id):
    # deletes a theme from the database completely
    mongo.db.themes.remove({'_id': ObjectId(theme_id)})
    return redirect(url_for('get_themes'))


@app.route('/insert_theme', methods=['POST'])
@login_required
def insert_theme():
    # takes the info from the form and creates a new theme in the database
    mongo.db.themes.insert_one({'theme_name': request.form.get('theme_name').lower()})
    return redirect(url_for('get_themes'))


@app.route('/add_theme')
@login_required
def add_theme():
    # renders the add theme form
    return render_template('addtheme.html')


@app.route('/get_minifigure_theme/<theme_name>')
def get_minifigure_theme(theme_name):
    # filters the records by theme
    minifigures = mongo.db.minifigures.find(
        {'theme_name': theme_name, "minifig_deleted": False})
    return render_template("minifigs.html",
                            minifigures=minifigures,
                            themes=mongo.db.themes.find(),
                            age=mongo.db.age.find(), isFilter=True)


@app.route('/get_minifigure_age/<age_range>')
def get_minifigure_age(age_range):
    # filters the records by age range
    minifigures = mongo.db.minifigures.find(
        {'age_range': age_range, "minifig_deleted": False})
    return render_template("minifigs.html",
                            minifigures=minifigures,
                            themes=mongo.db.themes.find(),
                            age=mongo.db.age.find(), isFilter=True)


@app.route('/get_minifigure_name', methods=['GET', 'POST'])
def get_minifigure_name():
    # filters the records by name
    if request.method == "POST":
        minifigures = mongo.db.minifigures.find(
            {'minifigure_name': request.form['minifigure_name'].lower(), "minifig_deleted": False})
        return render_template("minifigs.html", minifigures=minifigures, 
                themes=mongo.db.themes.find(),
                age=mongo.db.age.find(), isFilter=True)


@app.route('/like_minifig/<minifigure_id>')
def like_minifig(minifigure_id):
    # ** UNFINISHED ROUTE ** likes a minifigure by increasing the count by 1 or decreasing if user doesn't like anymore.  
    user = mongo.db.users.find_one({"name": session['username']})
    print(user)
    user_liked = user.get('liked_items')
    print(user_liked)
    like_counter = mongo.db.minifigures.find_one({'_id': ObjectId(minifigure_id), 'liked_counter': ''})
    print(like_counter)
    if minifigure_id in user_liked:
        user_liked.remove(minifigure_id)
    else:
        user_liked.append(minifigure_id)
    mongo.db.users.update_one
    return redirect(url_for('get_minifigures'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
