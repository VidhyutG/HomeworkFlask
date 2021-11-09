from myapp import myobj
from myapp import db
from myapp.forms import TopCites
from myapp.models import City
from flask import render_template, escape, flash, redirect

@myobj.route("/", methods=['GET', 'POST'])
def home():
    title = "Top Cites"
    name = "Vidhyut"
    top_cities = City.query.all()
    form = TopCites()
    if form.validate_on_submit():
        city = City(city_name = form.city_name.data, city_rank = form.city_rank.data, is_visited = form.is_visited.data)
        db.session.add(city)
        db.session.commit()
        flash(f'City {form.city_name.data} added into list!')
        return redirect("/")
    return render_template("home.html", title = title, name = name, top_cities = top_cities, form = form)

