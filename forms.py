from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, HiddenField
from wtforms.validators import DataRequired

class AnimalForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    image = SelectField("Image: ", validators=[DataRequired()],
        choices=[
            ("bear.jpg", "Bear"),
            ("cheetah.jpg", "Cheetah"),
            ("deer.jpg", "Deer"),
            ("elephant.jpg", "Elephant"),
            ("fox.jpg", "Fox"),
            ("gibbon.jpg", "Gibbon"),
            ("giraffe.jpg", "Giraffe"),
            ("lion.jpg", "Lion"),
            ("owl.jpg", "Owl"),
            ("zebra.jpg", "Zebra"),
            ("animals.jpg", "Other Animals")
        ]
    )
    region = StringField("Region: ")
    predator = BooleanField("Is this a predator?")

class EditAnimalForm(AnimalForm):
    row_id = HiddenField()

class DeleteAnimalForm(FlaskForm):
    row_id = HiddenField()