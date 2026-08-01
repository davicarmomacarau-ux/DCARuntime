"""
===========================================
DCARuntime
database.py
Versão 0.2.0
===========================================
"""

import sqlite3
from pathlib import Path
from datetime import datetime


class Database:

    def __init__(self, db_name="dcaruntime.db"):

        self.base_path = Path(__file__).parent

        self.db_path = self.base_path / db_name

        self.connection = sqlite3.connect(self.db_path)

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

        self.create_tables()

    # ==========================================
    # CREATE TABLES
    # ==========================================

    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS settings(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            key TEXT UNIQUE,

            value TEXT

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS logs(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            level TEXT,

            message TEXT,

            created_at TEXT

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS plugins(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT UNIQUE,

            version TEXT,

            enabled INTEGER

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS runtime_history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            started_at TEXT,

            finished_at TEXT,

            status TEXT

        )

        """)

        self.connection.commit()

    # ==========================================
    # SETTINGS
    # ==========================================

    def set_setting(self, key, value):

        self.cursor.execute("""

        INSERT INTO settings(key,value)

        VALUES(?,?)

        ON CONFLICT(key)

        DO UPDATE SET

        value=excluded.value

        """, (key, value))

        self.connection.commit()

    def get_setting(self, key):

        self.cursor.execute(

            "SELECT value FROM settings WHERE key=?",

            (key,)

        )

        row = self.cursor.fetchone()

        if row:

            return row["value"]

        return None

    # ==========================================
    # LOGS
    # ==========================================

    def add_log(self, level, message):

        self.cursor.execute("""

        INSERT INTO logs(

            level,

            message,

            created_at

        )

        VALUES(?,?,?)

        """,

        (

            level,

            message,

            datetime.now().isoformat()

        )

        )

        self.connection.commit()

    def get_logs(self):

        self.cursor.execute("""

        SELECT *

        FROM logs

        ORDER BY id DESC

        """)

        return self.cursor.fetchall()
        # ==========================================
    # PLUGINS
    # ==========================================

    def install_plugin(self, name, version="1.0.0"):

        self.cursor.execute("""

        INSERT OR REPLACE INTO plugins(

            name,

            version,

            enabled

        )

        VALUES(?,?,1)

        """,

        (

            name,

            version

        )

        )

        self.connection.commit()

    def uninstall_plugin(self, name):

        self.cursor.execute(

            "DELETE FROM plugins WHERE name=?",

            (name,)

        )

        self.connection.commit()

    def enable_plugin(self, name):

        self.cursor.execute(

            "UPDATE plugins SET enabled=1 WHERE name=?",

            (name,)

        )

        self.connection.commit()

    def disable_plugin(self, name):

        self.cursor.execute(

            "UPDATE plugins SET enabled=0 WHERE name=?",

            (name,)

        )

        self.connection.commit()

    def plugins(self):

        self.cursor.execute("""

        SELECT *

        FROM plugins

        ORDER BY name

        """)

        return self.cursor.fetchall()


    # ==========================================
    # RUNTIME HISTORY
    # ==========================================

    def runtime_start(self):

        now = datetime.now().isoformat()

        self.cursor.execute("""

        INSERT INTO runtime_history(

            started_at,

            finished_at,

            status

        )

        VALUES(?,?,?)

        """,

        (

            now,

            "",

            "RUNNING"

        )

        )

        self.connection.commit()

        return self.cursor.lastrowid


    def runtime_stop(self, runtime_id):

        now = datetime.now().isoformat()

        self.cursor.execute(
            """
            UPDATE runtime_history
            SET
                finished_at = ?,
                status = ?
            WHERE
                id = ?
            """,
            (
                now,
                "STOPPED",
                runtime_id
            )
        )

        self.connection.commit()


    def history(self):

        self.cursor.execute(
            """
            SELECT *
            FROM runtime_history
            ORDER BY id DESC
            """
        )

        return self.cursor.fetchall()
        # ==========================================
    # DATABASE MANAGEMENT
    # ==========================================

    def database_size(self):

        """
        Retorna o tamanho do banco em bytes.
        """

        return self.db_path.stat().st_size


    def vacuum(self):

        """
        Otimiza o banco SQLite.
        """

        self.cursor.execute(
            "VACUUM"
        )

        self.connection.commit()


    def clear_logs(self):

        """
        Remove todos os registros de logs.
        """

        self.cursor.execute(
            "DELETE FROM logs"
        )

        self.connection.commit()


    def clear_history(self):

        """
        Remove histórico de execução.
        """

        self.cursor.execute(
            "DELETE FROM runtime_history"
        )

        self.connection.commit()


    def backup(self, filename="dcaruntime_backup.db"):

        """
        Cria uma cópia de segurança do banco.
        """

        backup_path = self.base_path / filename

        backup_connection = sqlite3.connect(
            backup_path
        )

        with backup_connection:

            self.connection.backup(
                backup_connection
            )

        backup_connection.close()

        return backup_path


    def close(self):

        """
        Fecha conexão com banco.
        """

        if self.connection:

            self.connection.close()


# ==========================================
# TESTE DO BANCO
# ==========================================

if __name__ == "__main__":

    db = Database()


    print("\n=== DCARuntime Database Test ===\n")


    # Configurações

    db.set_setting(
        "version",
        "0.2.0"
    )

    db.set_setting(
        "developer",
        "DCA"
    )


    # Logs

    db.add_log(
        "INFO",
        "Database iniciado"
    )


    # Plugins

    db.install_plugin(
        "hardware",
        "1.0.0"
    )

    db.install_plugin(
        "network",
        "1.0.0"
    )


    # Histórico

    runtime_id = db.runtime_start()


    print("Configurações:")

    print(
        db.get_setting("version")
    )


    print("\nPlugins:")

    for plugin in db.plugins():

        print(
            dict(plugin)
        )


    print("\nLogs:")

    for log in db.get_logs():

        print(
            dict(log)
        )


    db.runtime_stop(
        runtime_id
    )


    print("\nHistórico:")

    for item in db.history():

        print(
            dict(item)
        )


    print(
        "\nTamanho do banco:",
        db.database_size(),
        "bytes"
    )


    # Backup

    backup = db.backup()

    print(
        "\nBackup criado:",
        backup
    )


    db.close()


    print(
        "\nBanco fechado."
    )