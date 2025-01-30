from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, text
import pandas as pd

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///All_Properties.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# initialise the app with the extension
db.init_app(app)


# CREATE TABLE - the class name must match the name of the table in the SQL database
class house(db.Model):
    id: Mapped[str] = mapped_column(String(20), primary_key=True)
    SQFT: Mapped[str] = mapped_column(String(20), nullable=True)
    # Desc: Mapped[str] = mapped_column(String(20), nullable=True)
    # B: Mapped[str] = mapped_column(String(20), nullable=True)
    # Ba: Mapped[str] = mapped_column(String(20), nullable=True)
    Address: Mapped[str] = mapped_column(String(20), nullable=True)
    Pic1: Mapped[str] = mapped_column(String(20), nullable=True)
    Pic2: Mapped[str] = mapped_column(String(20), nullable=True)
    Pic3: Mapped[str] = mapped_column(String(20), nullable=True)
    Pic4: Mapped[str] = mapped_column(String(20), nullable=True)
    Pic5: Mapped[str] = mapped_column(String(20), nullable=True)
    Floorplan: Mapped[str] = mapped_column(String(20), nullable=True)
    Tour: Mapped[str] = mapped_column(String(20), nullable=True)

class Prop(db.Model):
    id: Mapped[str] = mapped_column(String(20), primary_key=True)
    SQFT: Mapped[str] = mapped_column(String(20), nullable=True)
    Desc: Mapped[str] = mapped_column(String(20), nullable=True)
    B: Mapped[str] = mapped_column(String(20), nullable=True)
    Ba: Mapped[str] = mapped_column(String(20), nullable=True)
    Address: Mapped[str] = mapped_column(String(20), nullable=True)
    Pic1: Mapped[str] = mapped_column(String(20), nullable=True)
    Pic2: Mapped[str] = mapped_column(String(20), nullable=True)
    Pic3: Mapped[str] = mapped_column(String(20), nullable=True)
    Pic4: Mapped[str] = mapped_column(String(20), nullable=True)
    Pic5: Mapped[str] = mapped_column(String(20), nullable=True)
    Floorplan: Mapped[str] = mapped_column(String(20), nullable=True)
    Tour: Mapped[str] = mapped_column(String(20), nullable=True)


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

df = pd.read_excel('Available_Properties.xlsx')

prop_list = df['id'].tolist()


@app.route('/')
def home():

    # READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(house).order_by(house.id))

    # Use .scalars() to get the elements rather than entire rows from the database
    all_houses = result.scalars().all()
    
    return render_template("admin.html", houses=all_houses)

@app.route('/all')
def all():

    # READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(house).order_by(house.id))

    # Use .scalars() to get the elements rather than entire rows from the database
    all_houses = result.scalars().all()
    
    return render_template("all.html", houses=all_houses)

@app.route('/avail')
def avail():

    # READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the filtered database
    result = db.session.execute(db.select(house).filter(house.id.in_(prop_list)).order_by(house.id))

    # Use .scalars() to get the elements rather than entire rows from the database
    all_houses = result.scalars().all()

    return render_template("listings.html", houses=all_houses) #This is the Admin page - where you can view and edit/add all properties
    

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # CREATE RECORD for new house and specify the attributes
        
        new_house = house(
            id=request.form["id"],
            Address=request.form["Address"],
            SQFT=request.form["SQFT"],
            Desc=request.form["Desc"],
            B=request.form["B"],
            Ba=request.form["Ba"],
            Pic1=request.form["Pic1"],
            Pic2=request.form["Pic2"],
            Pic3=request.form["Pic3"],
            Pic4=request.form["Pic4"],
            Pic5=request.form["Pic5"],
            Floorplan=request.form["Floorplan"],
            Tour=request.form["Tour"]
        )
        db.session.add(new_house)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html") #This is where we add a new property - inputs with edit boxes

@app.route("/delete")
def delete():
    house_id = request.args.get('id')

    # DELETE A RECORD BY ID
    house_to_delete = db.get_or_404(house, house_id)
    # Alternative way to select the book to delete.
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(house_to_delete)
    db.session.commit()
    return redirect(url_for('home')) #Go back to homepage after deleting an item

@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        # UPDATE RECORD
        house_id = request.form["id"]
        house_to_update = db.get_or_404(house, house_id) #This house already exists, so we can do nothing to the field if it is blank
        
        if request.form['SQFT'] != '':
            house_to_update.SQFT = request.form["SQFT"]

        if request.form['Desc'] != '':
            house_to_update.Desc = request.form["Desc"]

        if request.form['B'] != '':
            house_to_update.B = request.form["B"]

        if request.form['Ba'] != '':
            house_to_update.Ba = request.form["Ba"]
        
        if request.form['Address'] != '':
            house_to_update.Address = request.form["Address"]

        if request.form['Pic1'] != '':
            house_to_update.Pic1 = request.form["Pic1"]
        
        if request.form['Pic2'] != '':
            house_to_update.Pic2 = request.form["Pic2"]
    
        if request.form['Pic3'] != '':
            house_to_update.Pic3 = request.form["Pic3"]
        
        if request.form['Pic4'] != '':
            house_to_update.Pic4 = request.form["Pic4"]
        
        if request.form['Pic5'] != '':
            house_to_update.Pic5 = request.form["Pic5"]

        if request.form['Floorplan'] != '':
            house_to_update.Floorplan = request.form["Floorplan"]

        if request.form['Tour'] != '':
            house_to_update.Tour = request.form["Tour"]
        
        db.session.commit()
        return redirect(url_for('home'))
    
    house_id = request.args.get('id')
    house_selected = db.get_or_404(house, house_id)
    return render_template("update.html", house=house_selected) #This is where you would edit the property details

@app.route("/view", methods=["GET", "POST"])
def view():
    if request.method == "POST":
        # UPDATE RECORD
        house_id = request.form["id"]
        house_to_update = db.get_or_404(house, house_id) #This house already exists, so we can do nothing to the field if it is blank
        
        if request.form['SQFT'] != '':
            house_to_update.SQFT = request.form["SQFT"]

        if request.form['Desc'] != '':
            house_to_update.Desc = request.form["Desc"]

        if request.form['B'] != '':
            house_to_update.B = request.form["B"]

        if request.form['Ba'] != '':
            house_to_update.Ba = request.form["Ba"]
        
        if request.form['Address'] != '':
            house_to_update.Address = request.form["Address"]

        if request.form['Pic1'] != '':
            house_to_update.Pic1 = request.form["Pic1"]
        
        if request.form['Pic2'] != '':
            house_to_update.Pic2 = request.form["Pic2"]
    
        if request.form['Pic3'] != '':
            house_to_update.Pic3 = request.form["Pic3"]
        
        if request.form['Pic4'] != '':
            house_to_update.Pic4 = request.form["Pic4"]
        
        if request.form['Pic5'] != '':
            house_to_update.Pic5 = request.form["Pic5"]

        if request.form['Floorplan'] != '':
            house_to_update.Floorplan = request.form["Floorplan"]

        if request.form['Tour'] != '':
            house_to_update.Tour = request.form["Tour"]
        
        db.session.commit()
        return redirect(url_for('home'))
    
    house_id = request.args.get('id')
    house_selected = db.get_or_404(house, house_id)
    return render_template("view.html", house=house_selected) #This is where you would examine individual property details

if __name__ == "__main__":
    app.run(debug=True)