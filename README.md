# Hostel Pass Application

## Description

The Hostel Pass Application is a web-based system designed to streamline the process of applying for and managing hostel passes. The application allows users to submit pass requests online and provides an interface for administrators to review and manage these requests.

### Features

- **User Login:** Users can log in to the system to apply for hostel passes.
- **Pass Application Form:** Users can fill out a form to apply for a pass, providing their name and the reason for the request.
- **Pass Management:** The application lists all submitted pass requests, allowing administrators to approve or reject them.
- **Admin Actions:** Administrators have special privileges to manage and update the status of pass requests.

### Technologies Used

- **HTML/CSS:** For structuring and styling the web pages.
- **JavaScript:** For handling user interactions and AJAX requests.
- **Python (Flask):** For backend logic and routing.
- **Jinja:** For rendering templates dynamically based on user roles.

### File Structure

- **index.html:** The main page where users can apply for passes and view existing requests【10†source】.
- **login.html:** The login page where users authenticate themselves before accessing the system【8†source】.
- **style.css:** The stylesheet that defines the visual layout of the application, ensuring a clean and user-friendly interface【9†source】.
- **script.js:** Contains client-side JavaScript code to handle form submissions, pass retrieval, and admin actions like approving or rejecting passes【11†source】.
- **app.py:** Backend Python script that handles routing, user authentication, and database interactions.

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/hostel-pass-application.git
   cd hostel-pass-application
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   python app.py
   ```
4. **Access the application:**
   Open your web browser and go to `http://localhost:5000`.

### Usage

1. **Login:** Enter your username and password on the login page.
2. **Apply for a Pass:** Fill out the form on the main page to submit a pass request.
3. **Admin Actions:** If you are an admin, you can approve or reject pass requests from the list.
