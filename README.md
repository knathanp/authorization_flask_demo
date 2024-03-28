
# Flask Authorization Demo Application

This demo Flask application illustrates a simple implementation of Role-Based Access Control (RBAC) and Attribute-Based Access Control (ABAC). The application supports three types of roles: Admin, Editor, and Viewer, each with different levels of access permissions.

This demo is intended to be a starting point for understanding how to implement access control in Flask applications. It is not intended for production use and lacks many features that would be necessary for a real-world application.

This demo is based on the tutorial by [Real Python](https://realpython.com/flask-authorization/).

## Features

- **User Authentication:** Simple authentication system using Flask sessions.
- **Role-Based Access Control:** Different access permissions based on user roles:
  - **Admin:** Can create, read, update, and delete content.
  - **Editor:** Can read and update content.
  - **Viewer:** Can only read content.
- **Attribute-Based Access Control:** Access decisions are made based on user attributes.
   - **Dynamic Policy Enforcement:** Demonstrates how policies can be applied based on various attributes of users and resources.
- **Secure Password Handling:** (Note: This demo uses plaintext passwords for simplicity, but in a real-world application, you should hash passwords using a library like `bcrypt` or `argon2`.)





## Getting Started

### Prerequisites

- Python 3.6 or later.
- Flask

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/knathanp/flask_demo.git
   cd flask_demo
   ```

2. Install the required Python packages:

   ```
   pip install Flask
   ```

### Running the Application

1. Start the Flask application using RBAC:

   ```
   python app_rbac.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to view the application.

### Usage

- Visit `http://127.0.0.1:5000/login` to log in as different users. Here are the credentials you can use:
  - Admin: Username `admin`, Password `adminpass`
  - Editor: Username `editor`, Password `editorpass`
  - Viewer: Username `viewer`, Password `viewerpass`
- Once logged in, you will see your role and available permissions.
- Try accessing the `/create`, `/edit`, and `/delete` routes to see access control in action.

### Switching Between RBAC and ABAC

- Stop the Flask application and switch from RBAC to ABAC by starting the other script:

   ```
   python app_abac.py
   ```

- Visit `http://127.0.0.1:5000/login` to log in as different users. Here are the credentials you can use:
  - Admin: Username `alice`, Password `alicepass`
  - Editor: Username `bob`, Password `bobpass`
  - Viewer: Username `carol`, Password `carolpass`
- Once logged in, you will see your role and available permissions.
- Visit the `/edit_marketing_material` route with different user roles to see how the access permissions change based on user attributes.
- Visit the `logout` route to log out and switch users.
- The ABAC implementation demonstrates dynamic policy enforcement based on user attributes. You can see the different access permissions based on the user's role and department.

### Tasks for Students

- Implement additional resources by adding additional routes and define complex ABAC policies considering user, resource, and environmental attributes.
- Reflect on the differences between ABAC and RBAC, discussing the benefits and challenges of each.


## Important Notes

- This project is provided for educational purposes and is not intended for use in production environments.
- Passwords are stored and checked in plaintext for simplicity in this demo. For any real-world application, use hashed passwords and a more secure authentication method.
- This demo uses a simple in-memory user database. In a real-world application, you would use a proper database like PostgreSQL or SQLite.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
