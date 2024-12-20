# property-vacancies
Property management vacancy web utility

### Authors
William Vann

Gregory Michalak

John Torgerson

### Instructions
1. Download a copy of the current availability report in realpage, and save file as `Avail.csv`
2. Replace the existing file in repo directory.
3. Using Jupyter notebook, run `Prop_Cleaner.ipynb`in entirety.
4. In gitbash, run flask `main_prop.py` and copy displayedweb address for your local server
5. In browser paste local server address in filepath
6. Enter new data, edit existing data, and view currently available units with easy to read fields

### File Index
* In folder `Instance`
    `All_Properties.db`
* In folder sqlite_approach
    `index.html`
    `script.js`
    `style.css`
* In folder `static`
    *In folder `css`
        `reset.css`
        `style.css`
* In folder `templates` these are our working webpages for this database
    `add.html` adds a new property and fields to the management library
    `admin.html` full list of properties in the library
    `listings.html` filtered list of currently available properties and their fields
    `update.html` revises an existing property and fields  
`DS_Store`
`.gitignore`
`All_Properties.db`
`All_Properties.sqbpro`
`Avail_8.19.csv` this is the real world working availability report for beta testing our filter
`Avalable_Properties.xlsx` this is the cleaned ID list we use as our filter
`main_prop.py` this is the python flask we run to manipulate the database locally
`Prop_Cleaner.ipynb` this is the code you'll run to clean the real world avail report
`properties.db`
`properties.sqbpro`
`README.md`
`requirements.txt`
`Vacancy Workflow Design.jpg` concept of idea

##### Initially we were looking at using something like Postgres and SQL, and we could potentially return to that, but for now we're going to make a first attempt at this using SQlite in hopes that the project runs smoother and quicker. We'll just have to see if the idea expands if we won't need more data table relations, and we may, as this PMS software contains a lot of other useful contact points we could utilize. 


