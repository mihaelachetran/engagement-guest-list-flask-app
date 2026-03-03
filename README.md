# Engagement Guest List – Flask Web Application

## Overview

A full-stack web application built with **Python and Flask** that allows users to manage an engagement party guest list through a simple web interface.

The application supports guest creation, RSVP status updates, guest removal, and persistent data storage using a structured JSON file.

---

## Features

- Add new guests  
- Remove guests  
- Update RSVP status (Yes / No / Pending)  
- View total invited guests  
- View confirmed guests  
- Server-side validation to prevent duplicate entries  
- Persistent data storage using JSON  

---

## Tech Stack

- Python  
- Flask  
- HTML  
- CSS (Flexbox for layout and responsiveness)  
- JSON (for data persistence)  

---

## How It Works

Flask handles routing and form submissions. The main route processes both:

- **GET requests** – to render the guest list page  
- **POST requests** – to handle form actions (add, remove, update RSVP)  

Each form includes an `action` value, allowing the backend to determine which operation to execute.

Jinja2 templating dynamically renders guest data within the HTML interface, while Python logic validates input, prevents duplicate entries, and calculates confirmed guest totals in real time.

---

## Project Structure


app.py
guest_list.py
templates/
static/
guests.json


---

## How to Run Locally

1. Install Python (3.10+ recommended)
2. Install Flask:


pip install flask


3. Navigate to the project folder  
4. Run:


python app.py


5. Open your browser and visit:


http://127.0.0.1:5000


---

## Challenges & Problem Solving

One challenge involved managing multiple form actions within a single route.  
This was resolved by including an `action` field in each form and applying conditional logic in the Flask route.

Another challenge was preventing duplicate guest entries. This was addressed by implementing input normalization and validation checks to ensure consistent comparisons.

Incremental testing and print-based debugging were used to identify and resolve issues throughout development.

---

## Academic Context

This project was developed as part of the Python & Web Development Skills Bootcamp (2026).