Engagement Party Guest List – Full-Stack Flask Application
===========================================================

Project Overview
----------------
This project is a full-stack web application developed using Python and Flask. 
The application allows users to manage an engagement party guest list through 
a web interface.

Users can:
- Add guests
- Remove guests
- Update RSVP status (Yes / No / Pending)
- View total invited guests
- View confirmed guests

Guest data is stored in a structured JSON file (guests.json), enabling 
persistent data storage between sessions without requiring a database.

Technologies Used
-----------------
- Python
- Flask
- HTML
- CSS
- JSON (for data storage)

How the Application Works
--------------------------
Flask is used to create the backend server and define application routes. 
The main route handles both GET requests (to display the page) and POST 
requests (to process form submissions).

Each form includes an action value, allowing the application to determine 
whether to add, remove, or update a guest entry. Jinja2 templating is used 
to dynamically render guest data within the HTML interface.

Python logic is applied to validate user input, prevent duplicate entries, 
handle potential errors, and calculate the number of confirmed guests in real time.

Project Structure
-----------------
- app.py (main Flask application)
- guest_list.py (data handling functions)
- templates/index.html (HTML template)
- static/style.css (styling)
- guests.json (data storage)

Features Demonstrated
---------------------
- Backend development using Flask
- Handling GET and POST requests
- JSON data storage and retrieval
- Implementation of basic CRUD functionality
- Server-side validation and error handling
- Clear separation of front-end and back-end logic
- Responsive UI design using CSS and Flexbox

How to Run the Application
--------------------------
1. Install Python (version 3.10+ recommended)
2. Install Flask:
   pip install flask
3. Navigate to the project folder
4. Run:
   python app.py
5. Open a browser and visit:
   http://127.0.0.1:5000

Challenges and Debugging
------------------------
Managing multiple form actions within a single route was initially challenging. 
This was resolved by including an action field in each form and using conditional 
logic in the Flask route to process the correct operation.

Preventing duplicate guest entries required careful input handling. I implemented 
normalization techniques and validation checks to ensure consistent comparisons. 
Throughout development, I used incremental testing and print-based debugging 
to identify and resolve issues efficiently.

Author:
Mihaela Chetran
Python & Web Development Skills Bootcamp - 2026