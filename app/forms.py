from flask.ext.wtf import Form, TextField, Required, PasswordField, SelectField, FileField, TextAreaField

class LoginForm(Form):
    username = TextField('username')
    password = PasswordField('password')

class RegisterForm(Form):
    username = TextField('username', validators = [Required()])
    password = PasswordField('password', validators=[Required()])
    email = TextField('email', validators=[Required()])

class AchievementForm(Form):
    name = TextField('name', validators = [Required()])
    category = SelectField('category', coerce=int)
    description = TextAreaField('description', validators = [Required()])
    image = FileField('image')
    

