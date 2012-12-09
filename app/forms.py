from flask.ext.wtf import Form, TextField, Required, PasswordField

class LoginForm(Form):
    username = TextField('username', validators = [Required()])
    password = PasswordField('password', validators = [Required()])

class RegisterForm(Form):
    username = TextField('username', validators = [Required()])
    password = PasswordField('password', validators=[Required()])
    email = TextField('email', validators=[Required()])

