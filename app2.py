@app.route('/get_minifigures')
def get_minifigures():
    return render_template("minifigures.html", minifigures=mongo.db.minifigures.find())