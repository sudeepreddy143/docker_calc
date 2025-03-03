import sqlite3
import os

DB_PATH = os.getenv("DB_PATH", "commands.db")

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self._create_table()

    def _create_table(self):
        """Create the history table if it doesn't exist."""
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS command_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    command TEXT NOT NULL,
                    arguments TEXT NOT NULL,
                    result TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def log_command(self, command, arguments, result):
        """Log a command execution in the database."""
        with self.conn:
            self.conn.execute("""
                INSERT INTO command_history (command, arguments, result)
                VALUES (?, ?, ?)
            """, (command, arguments, result))

    def get_history(self, limit=10):
        """Retrieve the last `limit` commands from history."""
        with self.conn:
            return self.conn.execute("""
                SELECT command, arguments, result, timestamp
                FROM command_history
                ORDER BY timestamp DESC
                LIMIT ?
            """, (limit,)).fetchall()
