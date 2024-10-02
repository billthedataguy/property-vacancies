# property-vacancies
Property management vacancy web utility

### Authors
William Vann

Gregory Michalak

John Torgerson

### File Index
* In folder, `Greg_Code`:
    * In folder, `templates`:
        `add.html` webpage for inputing data to the library
        `edit_rating.html` webpage for editing a book in the library
        `index.html` webpage to display the library
        `prop_index.html` webpage for ... I'm not sure**
`Untitled.ipynb`
`All_Properties.db`
`books-collection.db`
`main.py`
`mani_prop.py`
`requirements.txt`
* In folder, `sqlite_approach`
    `index.html`
    `script.js`
    `style.css`
* In folder, `static`
    * In folder, `css`
* In folder, `templates`
    `add.html` webpage for inputing data to the library
    `edit_rating.html` webpage for editing a book in the library
    `index.html` webpage to display the library
    `prop_index.html` webpage for ... I'm not sure**
`Cleaning.ipynb` this file contains pandas code to filter a PMS report to a list of upcoming and available residential units by their unique property id<br>
`Avail_8.19.csv` this file is a real PMS software download we'll use to filter available residential units<br>
`DUMMY_SHEET.csv` this file is a practice list of residential units and data files<br>
`DUMMY_SHEET.xlsx` this file is a practice list of residential units and data files<br>
`market_table_fake` this file is a practice list of residential units and data files<br>
`properties.db`
`properties.sqbpro`
`public_site_test.html` empty webpage for testing a 2 part display combining data table and vacancy filter.
`README.md` you are here<br> 
`Vacancy Workflow Design.jpg` this file is an image of the workflow schematic to layout what we're designing<br>
`Vacant xml raw text.rtf` this is a raw text file I figured we could use as the format is similar to json, which I believe we can now delete as well 

### Notes

JT 9/29/2024: The directory 'Templates' are updated html code derived from Greg's flask api code reorganized as well as additinal input lines added to prepare for possible product demos. We may want to use multiples for "photos" and there's probably more than one way to do that. for example if these are under a keyed column in a table we may need to number them with a limited number of columns, but if we're using something organized more like a json, the inputs could be limitless with no numbering system. Both have their pros and cons I think. Input from the team would be valuable. 

GJM 9/25/2024: The directory 'Greg_Code' was added and contains source code for creating a SQLite database of properties and CRUD operations via Flask API. The HTML files associated with the webpage design are located in the 'templates' subdirectory, with the current version being 'prop_index'. Run main.py to deploy the API on a web browser.

##### Initially we were looking at using something like Postgres and SQL, and we could potentially return to that, but for now we're going to make a first attempt at this using SQlite in hopes that the project runs smoother and quicker. We'll just have to see if the idea expands if we won't need more data table relations, and we may, as this PMS software contains a lot of other useful contact points we could utilize. 


