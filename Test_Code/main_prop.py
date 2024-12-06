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
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:/Users/gmich/property-vacancies/Greg_Code/All_Properties.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# initialise the app with the extension
db.init_app(app)


# CREATE TABLE - the class name must match the name of the table in the SQL database
class house(db.Model):
    id: Mapped[str] = mapped_column(String(20), primary_key=True)
    address: Mapped[float] = mapped_column(Float, nullable=True)
    SQFT: Mapped[float] = mapped_column(Float, nullable=True)
    pic: Mapped[float] = mapped_column(Float, nullable=True)
    tour: Mapped[float] = mapped_column(Float, nullable=True)
    floorplan: Mapped[float] = mapped_column(Float, nullable=True)

class Prop(db.Model):
    id: Mapped[str] = mapped_column(String(20), primary_key=True)
    address: Mapped[float] = mapped_column(Float, nullable=True)
    SQFT: Mapped[float] = mapped_column(Float, nullable=True)
    pic: Mapped[float] = mapped_column(Float, nullable=True)
    tour: Mapped[float] = mapped_column(Float, nullable=True)
    floorplan: Mapped[float] = mapped_column(Float, nullable=True)

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

df = pd.read_excel('Available_Properties.xlsx')

prop_list = df['id'].tolist()


@app.route('/')
def home():

    # READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    # result = db.session.execute(db.select(house).order_by(house.id))
    result = db.session.execute(db.select(house).filter(house.id.in_(prop_list)).order_by(house.id))
    
    # Use .scalars() to get the elements rather than entire rows from the database
    
    all_houses = result.scalars().all()
    
    return render_template("avail_prop_index.html", houses=all_houses)

@app.route('/avail')
def admin():

    # READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(house).order_by(house.id))
    # result = db.session.execute(db.select(house).filter(house.id.in_(prop_list)).order_by(house.id))
    # results = db.session.execute(db.select(Prop).order_by(Prop.id))
    # Use .scalars() to get the elements rather than entire rows from the database
    
    all_houses = result.scalars().all()

    return render_template("full_prop_index.html", houses=all_houses) #This is the Admin page - where you can view and edit/add all properties
    

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # CREATE RECORD for new house and specify the attributes
        
        new_house = house(
            id=request.form["id"],
            address=request.form["address"],
            SQFT=request.form["SQFT"],
            pic=request.form["pic"],
            tour=request.form["tour"],
            floorplan=request.form["floorplan"]
            
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

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # UPDATE RECORD
        house_id = request.form["id"]
        house_to_update = db.get_or_404(house, house_id) #This house already exists, so we can do nothing to the field if it is blank
        
        if request.form['address'] != '':
            house_to_update.address = request.form["address"]
        
        if request.form['SQFT'] != '':
            house_to_update.SQFT = request.form["SQFT"]

        if request.form['pic'] != '':
            house_to_update.pic = request.form["pic"]

        if request.form['tour'] != '':
            house_to_update.tour = request.form["tour"]

        if request.form['floorplan'] != '':
            house_to_update.floorplan = request.form["floorplan"]
        
        db.session.commit()
        return redirect(url_for('home'))
    
    house_id = request.args.get('id')
    house_selected = db.get_or_404(house, house_id)
    return render_template("update.html", house=house_selected) #This is where you would edit the property details

if __name__ == "__main__":
    app.run(debug=True)
