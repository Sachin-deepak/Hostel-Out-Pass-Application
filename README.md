#Description:

The Hostel Pass Application is a web-based system designed to streamline the process of applying for and managing hostel passes. The application allows users to submit pass requests online and provides an interface for administrators to review and manage these requests.

#Features:

User Login: Users can log in to the system to apply for hostel passes.
Pass Application Form: Users can fill out a form to apply for a pass, providing their name and the reason for the request.
Pass Management: The application lists all submitted pass requests, allowing administrators to approve or reject them.
Admin Actions: Administrators have special privileges to manage and update the status of pass requests.
#Technologies Used:

HTML/CSS: For structuring and styling the web pages.
JavaScript: For handling user interactions and AJAX requests.
Python (Flask): For backend logic and routing.
Jinja: For rendering templates dynamically based on user roles.

#File Structure:

index.html: The main page where users can apply for passes and view existing requests​(index).
login.html: The login page where users authenticate themselves before accessing the system​(login).
style.css: The stylesheet that defines the visual layout of the application, ensuring a clean and user-friendly interface​(style).
script.js: Contains client-side JavaScript code to handle form submissions, pass retrieval, and admin actions like approving or rejecting passes​(script).
app.py: Backend Python script that handles routing, user authentication, and database interactions.
