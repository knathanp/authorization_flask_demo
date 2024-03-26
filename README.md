
# Flask RBAC Demo Application

This demo Flask application illustrates a simple implementation of Role-Based Access Control (RBAC). The application supports three types of roles: Admin, Editor, and Viewer, each with different levels of access permissions.

## Features

- **User Authentication:** Simple authentication system using Flask sessions.
- **Role-Based Access Control:** Different access permissions based on user roles:
  - **Admin:** Can create, read, update, and delete content.
  - **Editor:** Can read and update content.
  - **Viewer:** Can only read content.
- **Secure Password Handling:** (Note: This demo uses plaintext passwords for simplicity, but in a real-world application, you should hash passwords using a library like `bcrypt` or `argon2`.)

## Getting Started

### Prerequisites

- Python 3.6 or later.
- Flask

### Installation

1. Clone the repository:

   ```
   git clone https://your-repository-url-here.git
   cd your-repository-folder
   ```

2. Install the required Python packages:

   ```
   pip install Flask
   ```

### Running the Application

1. Start the Flask application:

   ```
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to view the application.

### Usage

- Visit `http://127.0.0.1:5000/login` to log in as different users. Here are the credentials you can use:
  - Admin: Username `admin`, Password `adminpass`
  - Editor: Username `editor`, Password `editorpass`
  - Viewer: Username `viewer`, Password `viewerpass`
- Once logged in, you will see your role and available permissions.
- Try accessing the `/create`, `/edit`, and `/delete` routes to see access control in action.

## Important Notes

- This application is a demo and is not intended for production use.
- Passwords are stored and checked in plaintext for simplicity in this demo. For any real-world application, use hashed passwords and a more secure authentication method.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
