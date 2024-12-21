# property-vacancies
Property management vacancy web utility for deploying marketing assets

### Authors
William Vann - Organization

Gregory Michalak - SQLAlchemy

John Torgerson - Concept & Design

### Instructions for using the software in this repository
1. Download a copy of the current availability report from realpage, and save file as `Vacancy.csv`
2. Replace the existing `Vacancy.csv` file in repo directory with the newly downloaded file.
3. Using Jupyter notebook, run `Prop_Cleaner.ipynb` in entirety.
4. In gitbash, run flask app `library_filter.py` and copy displayed local server address ID.
5. In browser paste local server address ID as filepath in the address bar.
6. A webpage will appear showing the list of all current existing properties stored in this library.
7. Enter new data, edit existing data, and view all or only currently available units.
8. After use, shut down flask server and exit gitbash.

### languages and programs used
python, pandas, Sql db pro, SQL, SQLalchemy, flask, html & externally, RealPage

### File Index
* In folder `Instance`
    `All_Properties.db` #this might be the duplicate?
* In folder `sqlite_approach` these went unused, but we did start here
    `index.html`
    `script.js`
    `style.css`
* In folder `static` these are standard formatting tools which were unecessary for this project
    *In folder `css` 
        `reset.css`
        `style.css`
* In folder `templates` these are our working webpages for this database
    `add.html` adds a new property and fields to the management library
    `admin.html` full list of properties in the library
    `all.html` full list of properties expanded to full details
    `listings.html` filtered list of currently available properties and their fields
    `update.html` revises an existing property and fields
    `view.html` full view of single property with full details  
`DS_Store`
`.gitignore`
`All_Properties.db`
`All_Properties.sqbpro`
`Avalable_Properties.xlsx` this is the cleaned ID list we use as our filter
`main_prop.py` this is the python flask we run to manipulate the database locally
`Prop_Cleaner.ipynb` this is the code you'll run to clean the real world avail report
`properties.db`
`properties.sqbpro`
`README.md`
`requirements.txt`
`Vacancy Workflow Design.jpg` concept of idea
`Vacancy.csv` this is the real world working availability report acting as our filter

##### Initially we were looking at using something like Postgres and SQL, and we could potentially return to that, but for now we're going to make a first attempt at this using SQlite in hopes that the project runs smoother and quicker. We'll just have to see if the idea expands if we won't need more data table relations, and we may, as this PMS software contains a lot of other useful contact points we could utilize.

##### We did return to SQL, but did not require Postgres as we were able to accomplish what was required with SQL Alchemy and SQL Database Pro operated with a flask server directly to local html

##### You do not need SQL database pro to run this, but you will need it if you'd like to make data table modifications to fields or datatypes

##### JT - Sometimes I tried expanding the fruit before the branches were stable enough to support them. Example: Renaming field labels from our sample "library & books" converted to "properties and houses" while aslo expanding upon them. The lingo shift at times confused the flask process due to premature or incomplete editing of variable names. I'll try to use more patience when coding with others in the future. its much easier to build out upon completion of function than it is to do in stride with debugging as sometimes those updates were causes of bugs. What feels like attempting efficiency, ultimately created inefficiency of workflow. One. step. at. a. time.


