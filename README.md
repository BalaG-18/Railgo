🚆 RailGo – Railway Reservation System

RailGo is a full-stack web-based Railway Reservation System developed using Python (Flask) and MongoDB. It allows users to register, log in, book train tickets, manage their accounts, and securely store reservation data. The system is designed to provide a simple, efficient, and user-friendly experience for railway ticket booking.

📌 Features

User Registration and Login Authentication

Secure Password Management (Change Password feature)

Train Ticket Booking System

Booking Details Storage in Database

User Dashboard Interface

Responsive Web Pages using HTML templates

MongoDB Database Integration

Real-time data handling using Flask routes

🛠️ Technologies Used
Frontend

HTML

CSS

JavaScript

Jinja2 Templates (Flask)

Backend

Python

Flask Framework

Database

MongoDB

Tools

VS Code

Git & GitHub

🗂️ Project Structure
Railgo/
│
├── app.py
├── templates/
│   ├── index.html
│   ├── book_ticket.html
│   ├── change_password.html
│   └── other HTML files
│
├── static/
│   ├── images
│   ├── videos
│   └── css / js files
│
└── README.md

⚙️ How the System Works
1. Frontend

Users interact with web pages to register, log in, and book tickets.

Forms collect user data such as name, journey details, and credentials.

2. Backend (Flask Server)

Receives requests from the frontend.

Validates user input.

Handles business logic like authentication and ticket booking.

Communicates with MongoDB for data storage and retrieval.

3. Database (MongoDB)

Stores:

User credentials

Booking information

Ticket details

Ensures data persistence and security.

4. Response Handling

Sends success or error messages back to users.

Displays booking confirmations or failure alerts.

🔁 Database Connectivity Flow

User enters data in the frontend form.

Data is sent to the Flask backend via HTTP request.

Flask processes and validates the data.

MongoDB stores or retrieves the required information.

Flask sends a response back to the frontend.

User sees the result on the webpage.

🧮 Algorithm (High Level)

Start

User opens the website

User logs in or registers

User enters booking details

Data sent to Flask backend

Backend validates input

Data stored in MongoDB

Booking confirmation returned

Display result to user

End

▶️ How to Run the Project Locally
Prerequisites

Python installed

MongoDB installed and running

pip package manager

Steps

Clone the repository:

git clone https://github.com/your-username/railgo.git


Navigate to project folder:

cd railgo


Install required packages:

pip install flask pymongo


Start MongoDB server

Run the application:

python app.py


Open browser and go to:

http://127.0.0.1:5000/

🔐 Security Features

Password validation

Session handling

Input validation

Controlled database access

📈 Future Enhancements

Online payment gateway integration

Seat selection system

Admin dashboard

Ticket cancellation module

Email/SMS notifications

Train schedule management
