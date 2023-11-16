import sqlite3
import sys
from pathlib import Path
from database.studantModel import StudantModel

"""Controls all the database manipulation for the studants table"""


class studantsController:
    def __init__(self) -> None:
        # Sets the database dir as the root
        if getattr(sys, "frozen", False):
            applicationPath = Path(sys._MEIPASS)
        else:
            applicationPath = Path(__file__).parent.parent

        # Sets the database dir as the root
        self.__ROOT_DIR = applicationPath
        # Sets the database name
        self.__DB_NAME = "studants.db"
        # Sets the complete database file path
        self.__DB_FILE = self.__ROOT_DIR / self.__DB_NAME

        # Triggers the function that create the database if needed
        self.__makeDataBase()

    def create(self, studant: StudantModel):
        """Creates a new studant in the database using the StudantModel class"""

        # sql command
        sql = "INSERT INTO studants (username, enrollment_number, password) VALUES (?, ?, ?);"

        # making the connection
        conn = sqlite3.connect(self.__DB_FILE)
        cursor = conn.cursor()

        # executing the command with the parameters
        cursor.execute(
            sql, (studant.username, studant.enrollment_number, studant.password)
        )

        conn.commit()

        # closing everything
        cursor.close()
        conn.close()

    def delete(self, studantid: int):
        """Deletes a studant from the database using the studant id"""

        # sql command
        sql = "DELETE FROM studants WHERE id = ?;"

        # making the connection
        conn = sqlite3.connect(self.__DB_FILE)
        cursor = conn.cursor()

        # executing the command with the parameters
        cursor.execute(sql, (studantid,))

        conn.commit()

        # closing everything
        cursor.close()
        conn.close()

    def getStudants(self) -> list:
        """Returns a list of all the studants in the database"""

        # sql command
        sql = "SELECT * FROM studants;"

        conn = sqlite3.connect(self.__DB_FILE)
        cursor = conn.cursor()

        # executing the command
        cursor.execute(sql)

        # get the list of studants from the quary
        studants = cursor.fetchall()

        # closing everything
        cursor.close()
        conn.close()

        return studants

    def getStudant(self, id: int) -> list:
        """Return a list with the data of one studant from the database"""

        sql = "SELECT * FROM studants WHERE id = ?;"

        conn = sqlite3.connect(self.__DB_FILE)
        cursor = conn.cursor()

        # executing the command
        cursor.execute(sql, (id,))

        # get the studant data from the quary
        studant = cursor.fetchone()

        # closing everything
        cursor.close()
        conn.close()

        return studant

    def __makeDataBase(self):
        """
        This method should be called anywhere else only in the studantController constructor
        creates the database if it doesn't exist"""

        sql = "CREATE TABLE IF NOT EXISTS studants (\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        username TEXT NOT NULL,\
        enrollment_number INTEGER NOT NULL,\
        password TEXT NOT NULL\
        );"

        conn = sqlite3.connect(self.__DB_FILE)
        cursor = conn.cursor()

        cursor.execute(sql)

        cursor.close()
        conn.close()
