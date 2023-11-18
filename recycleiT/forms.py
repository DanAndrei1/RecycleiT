from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

from database import get_user_by_username, get_user_by_email, get_recycle_by_barcode


class LoginForm(FlaskForm):
    username = StringField(validators=[Length(min=4)])
    email = EmailField(validators=[Email(), DataRequired()])
    submit = SubmitField(label='Login')


class RegisterForm(FlaskForm):
    first_name = StringField(validators=[Length(min=3, max=50), DataRequired()])
    last_name = StringField(validators=[Length(min=3, max=50), DataRequired()])
    username = StringField(validators=[Length(min=4)])
    email = EmailField(validators=[Email(), DataRequired()])
    password1 = PasswordField(validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(validators=[EqualTo(password1), DataRequired()])
    submit = SubmitField(label='Creeaza cont')

    @staticmethod
    def validate_username(username_to_check):
        user = get_user_by_username(username_to_check)
        if user:
            raise ValidationError("Username already exists")

    @staticmethod
    def validate_email(email_to_check):
        user = get_user_by_email(email_to_check)
        if user:
            raise ValidationError("Email already exists")

        class BarcodeForm(FlaskForm):
            barcode = StringField(validators=[DataRequired()])

            @staticmethod
            def validate_barcode(barcode_to_check):
                user = get_recycle_by_barcode(barcode_to_check)
                if user:
                    raise ValidationError("Barcode already exists")