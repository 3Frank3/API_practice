# database_sqlite3
This is a simple SQLite3 database for storing user information.
It is designed to be used with a Python application that requires user authentication and data storage.
## Features
- User registration and login
- Password hashing for security
- Basic user profile management
- SQLite3 database for lightweight storage 
## Requirements
- Python 3.x
- SQLite3 library
- Flask (for web application)
- Flask-SQLAlchemy (for database management)
## Installation     
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd database_sqlite3
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```  
4. Set up the database:
   ```bash
   python setup.py
   ```
5. Run the application:
   ```bash
   python app.py
   ```
## Usage
- Register a new user by accessing `/register` endpoint.
- Log in using the `/login` endpoint.
- Access user profile at `/profile`.
- Modify user information through `/profile/edit`.
## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.