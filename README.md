# 🚆 RailGo – Railway Reservation System

RailGo is a full-stack web-based Railway Reservation System developed using **Python (Flask)** and **MongoDB**. It allows users to register, log in, book train tickets, manage their accounts, and securely store reservation data.

---

## 📌 Features

- User Registration and Login Authentication  
- Secure Password Management (Change Password feature)  
- Train Ticket Booking System  
- Booking Details Storage in Database  
- User Dashboard Interface  
- Responsive Web Pages using HTML templates  
- MongoDB Database Integration  
- Real-time data handling using Flask routes  

---

## 🛠️ Technologies Used

### Frontend
- HTML  
- CSS  
- JavaScript  
- Jinja2 Templates (Flask)

### Backend
- Python  
- Flask Framework

### Database
- MongoDB

### Tools
- VS Code  
- Git & GitHub  

---


---

## ⚙️ How the System Works

### 1. Frontend
- Users interact with web pages to register, log in, and book tickets.
- Forms collect user data such as name, journey details, and credentials.

### 2. Backend (Flask Server)
- Receives requests from the frontend.
- Validates user input.
- Handles business logic like authentication and ticket booking.
- Communicates with MongoDB for data storage and retrieval.

### 3. Database (MongoDB)
- Stores:
  - User credentials
  - Booking information
  - Ticket details

### 4. Response Handling
- Sends success or error messages back to users.
- Displays booking confirmations or failure alerts.

---

## 🔁 Database Connectivity Flow

1. User enters data in the frontend form  
2. Data is sent to the Flask backend via HTTP request  
3. Flask processes and validates the data  
4. MongoDB stores or retrieves the required information  
5. Flask sends a response back to the frontend  
6. User sees the result on the webpage  

---

## 🧮 Algorithm (High Level)

1. Start  
2. User opens the website  
3. User logs in or registers  
4. User enters booking details  
5. Data sent to Flask backend  
6. Backend validates input  
7. Data stored in MongoDB  
8. Booking confirmation returned  
9. Display result to user  
10. End  

---

## ▶️ How to Run the Project Locally

### Prerequisites
- Python installed  
- MongoDB installed and running  
- pip package manager  

### Steps

```bash
git clone https://github.com/your-username/railgo.git
cd railgo
pip install flask pymongo
python app.py



