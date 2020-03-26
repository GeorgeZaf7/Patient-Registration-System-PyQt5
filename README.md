# Patient-Registration-System
This is a Python3-PyQt5 based project.

The system comprised of various tabs/windows, starting with a login page ("Main.py") where the user has to fill-in valid credentials to it to unlock it. The credentials are stored in a database (sqlite3-based), titled "Login_Details_Database.db". A new user can only be added by the Admin of the system and/or by some other predefined already user. The registar's username is also recorded, as a safety measure. 

Following successful login, the next window allows the user to search/register a patient's details. These details are stored in a database titled "Patients_DB.db". If the patient is new, the Registration window opens and the patient's details are recorded together with the registar's username. If the patient exist, his/hers details are displayed and the user can check the medical records existing for the specific patient.    

After the search, a new window opens (contains two major buttons), where the user can either retrieve the existing records (Button no.1) or add new notes (Button no.2). If the Button 1 is pressed, a new window opens, which asks the user to define the starting date from which onwards the records wishes to see. The date submission returns a new window where all the notes from the defined date onwards are displayed (in a table format - the notes can be double-clicked ans are printed in a text editor without edit permission). If Button 2 is pressed, a new window opens with a text editor where the user can add a new medical note. The Medical Records/Notes are stored individually for each patient in an database with the patient's Registration ID.   


Note: The structure of the scripts can be seen in the Code_Structure.pdf file.

