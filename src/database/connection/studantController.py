import sqlite3
from pathlib import Path
from database.studantModel import StudantModel


class studantsController:
    def __init__(self) -> None:
        self.__ROOT_DIR = Path(__file__).parent.parent
        self.__DB_NAME = "studants.db"
        self.__DB_FILE = self.__ROOT_DIR / self.__DB_NAME
        self.__makeDataBase()
        self.__feedStudantsList()

    def create(self, studant: StudantModel):
        sql = "INSERT INTO studants (username, enrollment_number, password) VALUES (?, ?, ?);"

        conn = sqlite3.connect(self.__DB_FILE)
        cursor = conn.cursor()

        cursor.execute(
            sql, (studant.username, studant.enrollment_number, studant.password)
        )

        studantID = cursor.lastrowid

        studant.id = studantID
        studant.studantsList.append(studant)

        conn.commit()

        cursor.close()
        conn.close()

    def __feedStudantsList(self):
        sql = "SELECT * FROM studants;"

        conn = sqlite3.connect(self.__DB_FILE)
        cursor = conn.cursor()

        cursor.execute(sql)

        for studant in cursor.fetchall():
            self.studantsList.append(
                StudantModel(studant[1], studant[2], studant[3], studant[0])
            )

    def delete(self, studant: StudantModel):
        sql = "DELETE FROM products WHERE id = ?;"

        conn = sqlite3.connect(self.__DB_FILE)
        cursor = conn.cursor()

        cursor.execute(sql, (studant.id,))

        conn.commit()

        cursor.close()
        conn.close()

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
