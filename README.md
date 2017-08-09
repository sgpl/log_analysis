# Project Name: Log Analysis 


## How to run the program: 
	Please download the "log_analysis.py" file 
	in the same folder as your database. 
	
	The program assumes that you have a database called
	"news" in the folder where you're downloading 
	"log_analysis.py". 
	
	This program also assumes that you have postgreSQL 
	installed on your machine and have a basic 
	understanding of running python programs using 
	the terminal.
	
**Step 1.** Using terminal navigate to the directory where you've downloaded the program "log_analysis.py".
	
**Step 2.** Run the program using the following command: 
	
	python log_analysis.py
	
**Step 3:** The results should be displayed for you to view in your terminal window momentarily. 
			 

## Program's design (description):
The program uses python to access a PostgreSQL database that's stored locally in the same folder as the program. 

Using functions, it opens a connection to the database, runs a query to answer questions *(the parameters of which are specified in the project submission guidelines)* leveraging the data stored in the database. And then closes the connection to the database. 

Finally all the defined functions are called so that the program can output the results when it is run!
 

## Statements to create views:

No views were created for this project. 