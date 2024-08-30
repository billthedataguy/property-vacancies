# property-vacancies
Property management vacancy web utility

### Authors
William Vann

Gregory Michalak

John Torgerson

### File Index
`Cleaning.ipynb` this file contains pandas code to filter a PMS report to a list of upcoming and available residential units by their unique property id<br>
`Avail_8.19.csv` this file is a real PMS software download we'll use to filter available residential units<br>
`DUMMY_SHEET.xlsx` this file is a practice list of residential units and data files<br>
`index.html` this is a blank landing page to display results of our subquery filter<br>
`market_table_fake` this file is a practice list of residential units and data files<br>
`README.md` you are here<br> 
`Vacancy Workflow Design.jpg` this file is an image of the workflow schematic to layout what we're designing<br>
`Vacant xml raw text.rtf` this is a raw text file I figured we could use as the format is similar to json, which I believe we can now delete as well 
    

### Notes
    

##### Initially we were looking at using something like Postgres and SQL, and we could potentially return to that, but for now we're going to make a first attempt at this using SQlite in hopes that the project runs smoother and quicker. We'll just have to see if the idea expands if we won't need more data table relations, and we may, as this PMS software contains a lot of other useful contact points we could utilize. 


