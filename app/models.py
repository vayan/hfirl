from app import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), index = True, unique = True)
    upper_cat = db.Column(db.Integer)

    def __repr__(self):
        return '<Category %r>' % (self.name)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pseudo = db.Column(db.String(128), index = True, unique = True)
    email = db.Column(db.String(128), unique = True)
    password = db.Column(db.String(128))
    avatar = db.Column(db.String(128))
    name = db.Column(db.String(128))
    first_name = db.Column(db.String(128))
    rank = db.Column(db.Integer)
    date_sigin = db.Column(db.Date)
    date_online = db.Column(db.Date)
    created_achievements = db.relationship('Achievement', backref = 'creator', lazy = 'dynamic')
    achievements = db.relationship('UserAchieved', backref = 'user', lazy = 'dynamic')

    def __repr__(self):
        return '<User %r # %r>' % (self.pseudo, self.email)

class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128), index = True, unique = True)
    category = db.Column(db.Integer)
    image = db.Column(db.String(128))
    description = db.Column(db.String(512))
    creator = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_created = db.Column(db.Date)
    point_worth = db.Column(db.Integer)
    score_vote = db.Column(db.Integer)
    users = db.relationship('UserAchieved', backref = 'achievements', lazy = 'dynamic')

    def __repr__(self):
        return '<Achievement %r>' % (self.name)

class UserAchieved(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    achievement = db.Column(db.Integer, db.ForeignKey('achievement.id'))
    user = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<UserAchieved %r > %r>' % (user, achievement)
    
    
