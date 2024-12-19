import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def crate_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS survey_results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    genre TEXT
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    price FLOAT,
                    genre TEXT
                )
            """)
            conn.commit()

    def save_survey(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
            """
                INSERT INTO survey_results (name, age, genre)
                VALUES (?, ?, ?)
            """,
            (data["name"], data["age"], data["genre"])
            )

    def save_book(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
            """
                INSERT INTO books (name, price, genre)
                VALUES (?, ?, ?)
            """,
            (data["name"], data["price"], data["genre"])
            )

    def get_all_books(self):
        with sqlite3.connect(self.path) as conn:
            result = conn.execute("SELECT * from books")
            result.row_factory = sqlite3.Row
            data = result.fetchall()
            # data = result.fetchmany(10)

            return [dict(row) for row in data]


