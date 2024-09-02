from flask_wtf import FlaskForm
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from wtforms import StringField, PasswordField, SubmitField
from market.models import User


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Username already exists! Please try a different username")

    def validate_email_address(self, email_address_to_check):
        email = User.query.filter_by(email=email_address_to_check.data).first()

        if email:
            raise ValidationError("Email already exists! Please try a new email")

    username = StringField(label="username", validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label="email", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password 1", validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label="Password 2", validators=[EqualTo("password1"), DataRequired()])

    submit = SubmitField(label="Create Account")


class LoginForm(FlaskForm):

    username = StringField(label="username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Login")
