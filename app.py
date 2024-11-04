# app.py
from controllers.mutant_controller import app
from database.db_connection import initialize_database

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)
