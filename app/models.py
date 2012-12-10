from app import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), index = True, unique = True)
    upper_cat = db.Column(db.Integer)

    def __repr__(self):
        return '<Category %r>' % (self.name)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(128), index = True, unique = True)
    email = db.Column(db.String(128), unique = True)
    password = db.Column(db.String(128))
    avatar = db.Column(db.String(128))
    name = db.Column(db.String(128))
    first_name = db.Column(db.String(128))
    rank = db.Column(db.Integer)
    date_signup = db.Column(db.Date)
    date_online = db.Column(db.Date)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r # %r>' % (self.username, self.email)

class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128), index = True, unique = True)
    category = db.Column(db.Integer)
    image = db.Column(db.String(128))
    description = db.Column(db.String(512))
    creator = db.Column(db.Integer)
    date_created = db.Column(db.Date)
    point_worth = db.Column(db.Integer)
    score_vote = db.Column(db.Integer)

    def __repr__(self):
        return '<Achievement %r>' % (self.name)

class UserAchieved(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    achievement = db.Column(db.Integer)
    user = db.Column(db.Integer)

    def __repr__(self):
        return '<UserAchieved %r > %r>' % (user, achievement)
    
    
