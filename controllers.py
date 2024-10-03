from flask import Flask, render_template, request, redirect

from config import APP_NAME, SECRET_KEY

from models import Animal

from forms import AnimalForm, EditAnimalForm, DeleteAnimalForm

animal_controller = Flask(__name__)
animal_controller.config["SECRET_KEY"] = SECRET_KEY

@animal_controller.route("/add")
def add():
    form = AnimalForm(meta = {"csrf": True})

    return render_template(
        "add-animal.html.j2",
        site_title = APP_NAME,
        page_title = APP_NAME + " - Add Animal",
        args = request.args,
        form = form
    )

@animal_controller.route("/create", methods = ["POST"])
def create():
    form = AnimalForm(request.form, meta = {"csrf": True})
    if form.validate_on_submit():
        animal = Animal(form)
        animal.save()

        return redirect("/?add = success")
    else:
        return redirect("/add?add=error")
    
@animal_controller.route("/")
def read():
    animals = Animal().get_all()        #why not write animals = Animal.get_all() .. why are we writing Animal class as a function?
    form = DeleteAnimalForm(meta = {"csrf" : True})

    return render_template(
        "view-animals.html.j2",
        site_title  = APP_NAME,
        page_title = APP_NAME + " - View Animals",
        args = request.args,
        animals = animals, 
        form = form
    )

@animal_controller.route("/animal/<int:animal_id>")
def show(animal_id):
    animal = Animal().get(animal_id)        #why not write animals = Animal.get_all() .. why are we writing Animal class as a function?
    form = DeleteAnimalForm(meta = {"csrf" : True})

    return render_template(
        "show-animal.html.j2",
        site_title  = APP_NAME,
        page_title = APP_NAME + " - View Animal",
        args = request.args,
        animal = animal, 
        form = form
    )

@animal_controller.route("/edit/<int:animal_id>")
def edit(animal_id):
    animal = Animal().get(animal_id)

    form = EditAnimalForm(meta = {"csrf": True})
    form.name.data = animal["name"]
    form.image.data = animal["image"]
    form.region.data = animal["region"]
    form.predator.data = animal["predator"]
    form.row_id.data = animal_id

    return render_template(
        "edit-animal.html.j2",
        site_title = APP_NAME,
        page_title = APP_NAME + " - Edit Animal",
        args = request.args,
        animal = animal,
        form = form
    )

@animal_controller.route("/update", methods = ["POST"])
def update():
    form = EditAnimalForm(request.form, meta = {"csrf": True})
    animal_id = form.row_id.data

    if form.validate_on_submit():
        animal = Animal(form)
        animal.save(animal_id)
        return redirect("/?edit=success")
    else:
        return redirect(f"/edit/{animal_id}?edit=error")

@animal_controller.route("/delete", methods=["POST"])
def delete():
    form = DeleteAnimalForm( request.form, meta = {"csrf": True})
    animal_id = form.row_id.data

    if form.validate_on_submit():
        Animal().delete(animal_id)
        return redirect("/?delete=success")
    else:    
        return redirect("/?delete=error")
    