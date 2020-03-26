# Patient-Registration-System
This is a Python3-PyQt5 based project.

The system comprised of various tabs/windows, starting with a login page ("Main.py") where the user has to fill valid credentials to it to unlock it. The credentials are stored in a database (sqlite3), named "Login_details.db". The code for the login-credentials creation is not available to the user, rather an one of registration file is sent to the user for the registration. Then, the master user and every user with valid login credentials can allow new employees to register through a new tab/window activated by a "Add User" button on main window.

Following successful login, the next tab allows the user to search for a patient and its medical records. If the patient is not registered and no medical records exist, registration is available. For the clinician to access the medical records of the patient a new tab opens, where the data can be accessed either as a database(.db) or as text (.txt) files. Printing is allowed only with successful verification of the users identity. 

In the case where the clinicians would want to add new medical notes (medical record), then by clicking the available notes addition button will pop a new window. This new window is a text editor. 

When the clinical personnel  will finish its report, the data will be saved in the prviously mentioned database (one for each patient).

Note: The structure of the scripts can be seen in the Code_Structure.pdf file.

