"""
Module contains required SQL queries
"""
query_insert_data_to_rooms_table: str = """INSERT INTO rooms
                SELECT * FROM JSON_POPULATE_RECORDSET(NULL::rooms, %s);"""

query_insert_data_to_students_table: str = """INSERT INTO students
                SELECT * FROM JSON_POPULATE_RECORDSET(NULL::students, %s);"""

query_students_by_rooms_num: str = """SELECT * FROM students_num_view;"""

query_top_5_lowest_avg_age: str = """SELECT * FROM top_5_lowest_avg_age_view;"""

query_top_5_highest_age_diff: str = """SELECT * FROM top_5_highest_age_diff_view;"""

query_room_diversity_list: str = """SELECT * FROM room_diversity_list_view;"""

result_queries_list: list = [query_students_by_rooms_num, query_top_5_lowest_avg_age, query_top_5_highest_age_diff,
                             query_room_diversity_list]
