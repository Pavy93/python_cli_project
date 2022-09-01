"""
Main module
"""
import click
import json
from utils.conn_cursor_context_manager import ConnectAndCursorManager
from utils.file_manager import FileManager
from utils.sql_queries_collection import query_insert_data_to_rooms_table, query_insert_data_to_students_table,\
    result_queries_list


def work_with_postresql(rooms_file: str, students_file: str, out_folder: str, out_files_extension: str):
    __config_path = 'config/db_config.json'
    db_config: dict = FileManager().read_json_file(__config_path)

    with ConnectAndCursorManager(**db_config) as cur:
        data_rooms = FileManager().read_json_file(rooms_file)
        data_students = FileManager().read_json_file(students_file)
        cur.execute(query_insert_data_to_rooms_table, (json.dumps(data_rooms),))
        cur.execute(query_insert_data_to_students_table, (json.dumps(data_students),))

        out_files_names = ['students_by_rooms_num', 'top_5_lowest_avg_age', 'top_5_highest_age_diff',
                           'room_diversity_list']

        if out_files_extension:
            for query, file_name in zip(result_queries_list, out_files_names):
                cur.execute(query)
                result = cur.fetchall()
                path_to_save = f'{out_folder}/{file_name}.{out_files_extension}'
                FileManager().save_to_file(result[0][0], path_to_save)
