from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
import bcrypt
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL connection setup
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="W7301@jqir#",  # Ensure your password is correct
    database="Railway"
)
cursor = db.cursor()

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validate user credentials
        cursor.execute("SELECT * FROM users WHERE email=%s", (username,))
        user = cursor.fetchone()
        
        if user and bcrypt.checkpw(password.encode('utf-8'), user[2].encode('utf-8')):  # Assuming user[2] is the hashed password
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('menu_page'))  # Redirect to menu_page after login
        else:
            flash('Invalid username or password.', 'danger')
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Hashing the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Check if the user already exists
        cursor.execute("SELECT * FROM users WHERE email=%s", (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            flash('Username already exists. Please choose another one.', 'danger')
        else:
            # Insert new user into the database with only username and password
            cursor.execute("""
                INSERT INTO users (email, password)
                VALUES (%s, %s)
            """, (username, hashed_password.decode('utf-8')))
            db.commit()  # Save changes to the database
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('welcome'))

@app.route('/book_ticket', methods=['GET', 'POST'])
def book_ticket():
    if 'username' not in session:
        flash('You need to be logged in to book a ticket.', 'danger')
        return redirect(url_for('login'))

    if request.method == 'POST':
        try:
            # Capture all user details from the form
            name = request.form['name']
            age = request.form['age']
            gender = request.form['gender']
            address = request.form['address']
            mobile_number = request.form['mobile_number']
            travel_date = request.form['travel_date']
            starting_station = request.form['starting_station']
            destination_station = request.form['destination_station']
            coach_type = request.form['coach_type']
            
            # Generate random distance between 300 and 1000 km
            distance = random.randint(300, 1000)

            # Update user details in the database
            cursor.execute("""
                UPDATE users 
                SET name=%s, age=%s, gender=%s, address=%s, mobile_number=%s 
                WHERE email=%s
            """, (name, age, gender, address, mobile_number, session['username']))
            db.commit()

            # Insert ticket details into the database
            user_id = get_user_id(session['username'])
            pnr_number = generate_pnr_number()
            cursor.execute("""
                INSERT INTO ticket_details (user_id, pnr_number, travel_date, starting_station, destination_station, coach_type, distance)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (user_id, pnr_number, travel_date, starting_station, destination_station, coach_type, distance))
            db.commit()

            # Store ticket details in session to display after booking
            session['ticket_info'] = {
                'pnr_number': pnr_number,
                'travel_date': travel_date,
                'starting_station': starting_station,
                'destination_station': destination_station,
                'coach_type': coach_type,
                'distance': distance,
                'name': name,
                'age': age,
                'gender': gender,
                'address': address,
                'mobile_number': mobile_number
            }

            flash('Ticket booked successfully!', 'success')
            return redirect(url_for('book_ticket'))  # Refresh the page to show ticket details

        except Exception as e:
            db.rollback()  # Rollback if there's an error
            flash(f'An error occurred: {str(e)}', 'danger')

    return render_template('book_ticket.html')

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if 'username' not in session:
        flash('You need to be logged in to change your password.', 'danger')
        return redirect(url_for('login'))

    if request.method == 'POST':
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        # Check if the new password and confirmation match
        if new_password != confirm_password:
            flash('New passwords do not match.', 'danger')
            return redirect(url_for('change_password'))

        # Retrieve user information
        cursor.execute("SELECT * FROM users WHERE email=%s", (session['username'],))
        user = cursor.fetchone()

        # Verify old password
        if user and bcrypt.checkpw(old_password.encode('utf-8'), user[2].encode('utf-8')):
            # Update password in the database
            hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            cursor.execute("UPDATE users SET password=%s WHERE email=%s", (hashed_new_password.decode('utf-8'), session['username']))
            db.commit()
            flash('Password changed successfully!', 'success')
            return redirect(url_for('menu_page'))
        else:
            flash('Old password is incorrect.', 'danger')

    return render_template('change_password.html')

# Menu page (dashboard after login)
@app.route('/menu_page')
def menu_page():
    if 'username' not in session:
        flash('You need to be logged in to access this page.', 'danger')
        return redirect(url_for('login'))
    
    return render_template('menu_page.html')  # Create this HTML template for your menu/dashboard

def get_user_id(email):
    cursor.execute("SELECT user_id FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()
    return user[0] if user else None

def generate_pnr_number():
    return str(random.randint(1000000000, 9999999999))

@app.route('/personal_info', methods=['GET', 'POST'])
def personal_info():
    if 'username' not in session:
        flash('You need to be logged in to update personal information.', 'danger')
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        address = request.form['address']
        mobile_number = request.form['mobile_number']
        date_of_birth = request.form['date_of_birth']

        # Update the user's information in the database
        cursor.execute(""" 
            UPDATE users 
            SET name=%s, age=%s, gender=%s, address=%s, mobile_number=%s, date_of_birth=%s 
            WHERE email=%s
        """, (name, age, gender, address, mobile_number, date_of_birth, session['username']))
        db.commit()

        flash('Personal information updated successfully!', 'success')
        return redirect(url_for('menu_page'))

    # Fetch the user's current personal information to pre-fill the form
    cursor.execute("SELECT name, age, gender, address, mobile_number, date_of_birth FROM users WHERE email=%s", (session['username'],))
    user_info = cursor.fetchone()

    return render_template('personal_info.html', user_info=user_info)

if __name__ == '__main__':
    app.run(debug=True)
