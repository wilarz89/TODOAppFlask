from wtforms import Form,StringField, PasswordField, BooleanField, SubmitField, validators


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])


class LoginForm(Form):
    username = StringField('Username',[validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.Length(min=6, max=35)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')