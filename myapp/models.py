from myapp import db

class City(db.Model):
    city_name = db.Column(db.String(32), primary_key=True)
    city_rank = db.Column(db.Integer)
    is_visited = db.Column(db.Boolean)

    def __repr__(self):
        return f'<City  {self.city_name}>'

