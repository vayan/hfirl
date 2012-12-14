from app import app, db, models
from flask import render_template, flash, redirect, request, session, url_for, g
from forms import AchievementForm
import re
from datetime import datetime

def category_exists(name):
    category = models.Category.query.filter_by(name = name).first()
    if category != None:
            return True
    flash('Category %r already exists.' % name)
    return False

def achievement_exists(name):
    achievement = models.Achievement.query.filter_by(name = name).first()
    if achievement != None:
        flash('Achievement %s already exists.' % name)
        return True
    return False

def add_category(name, upper_cat):
    categ = models.Category(name = name, upper_cat = upper_cat)
    db.session.add(categ)
    db.session.commit()
    flash('Category %s successfully added.' % name)

def valid_categ(cat_id):
    if models.Category.query.get(cat_id) == None:
        flash('Invalid category.')
        return False
    return True

def add_achievement(name, category, description):
    if not valid_categ(category):
        return False
    if achievement_exists(name):
        return False
    date_now = datetime.now().date()
    achievement = models.Achievement(name = name, category = category, description = description, date_created = date_now)
    db.session.add(achievement)
    db.session.commit()
    flash('Achievement %s added !' % achievement.name)
    return True

@app.route('/create-achievement', methods = ['GET', 'POST'])
def create_achievement():
    if not g.user.is_authenticated():
        return redirect(url_for('login'))
    title = "Create an Achievement"
    form = AchievementForm()
    form.category.choices = [(cat.id, cat.name) for cat in models.Category.query.all()]
    if form.validate_on_submit():
        name = form.name.data
        category = form.category.data
        description = form.description.data
        if add_achievement(name, category, description):
            return redirect(url_for('index'))
        else:
            return redirect(url_for('create_achievement'))
    return render_template(
        'create_achievement.html',
        title = title,
        form = form)
