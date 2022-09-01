"""
module contains class ConnectAndCursorManager
"""

import psycopg2


class ConnectAndCursorManager:
    """
    Class implements context manager to create and PostgreSQL and its cursor. Returns cursor if everything works
    properly.
    """
    def __init__(self, **kwargs):
        self.ps_connection = psycopg2.connect(**kwargs)
        self.ps_cursor = self.ps_connection.cursor()

    def __enter__(self):
        return self.ps_cursor

    def __exit__(self, err_type, err_value, traceback):
        if err_type and err_value:
            self.ps_connection.rollback()
        self.ps_cursor.close()
        self.ps_connection.close()
        return False
