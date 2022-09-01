"""
Module contains required SQL queries
"""
query_insert_data_to_rooms_table: str = """INSERT INTO rooms
                SELECT * FROM JSON_POPULATE_RECORDSET(NULL::rooms, %s);"""

query_insert_data_to_students_table: str = """INSERT INTO students
                SELECT * FROM JSON_POPULATE_RECORDSET(NULL::students, %s);"""


class QueryCreator:
    @staticmethod
    def return_json_query(prefixes: list) -> list:
        query_list: list = []
        for prefix in prefixes:
            query_xml: str = f"""SELECT json_agg({prefix}_view) from {prefix}_view;"""
            query_list.append(query_xml)
        return query_list

    @staticmethod
    def return_xml_query(prefixes: list) -> list:
        query_list: list = []
        for prefix in prefixes:
            query_xml: str = f"""SELECT * FROM query_to_xml( 'SELECT * from {prefix}_view',true,false,'');"""
            query_list.append(query_xml)
        return query_list
