"""
Main module to work with PostgreSQL through CLI.
"""
import click
import json
from utils.conn_cursor_context_manager import ConnectAndCursorManager
from utils.file_manager import FileManager
from utils.sql_queries_collection import query_insert_data_to_rooms_table, query_insert_data_to_students_table,\
    result_queries_list


@click.command()
@click.option("--rooms-file", "-rf", default=None, help="Path to json file to insert data in rooms table.")
@click.option("--students-file", "-sf", default=None, help="Path to json file to insert data in students table.")
@click.option("--out-folder", "-outf", default='D:/docker/python_project/data',
              help="Folder where the results will be saved to.")
@click.option("--out-files-extension", "-ofe", default=None, help="Extension of files where results of the queries will"
                                                                  " be saved. Only JSON and XML.")
def work_with_postresql(rooms_file: str, students_file: str, out_folder: str, out_files_extension: str):
    """
    function "work_with_postresql" help to work with PostgreSQL through CLI
    :param rooms_file: Path to json file to insert data in rooms table.
    :type:rooms_file: str
    :param students_file: Path to json file to insert data in students table.
    :type:students_file: str
    :param out_folder: Folder where the results will be saved to.
    :type:out_folder: str
    :param out_files_extension: Extension of files where results of the queries will be saved. Only JSON and XML.
    :type:out_files_extension: str
    """
    __config_path: str = 'config/db_config.json'
    db_config: dict = FileManager().read_json_file(__config_path)

    with ConnectAndCursorManager(**db_config) as cur:
        if rooms_file and students_file:
            data_rooms = FileManager().read_json_file(rooms_file)
            data_students = FileManager().read_json_file(students_file)
            cur.execute(query_insert_data_to_rooms_table, (json.dumps(data_rooms),))
            cur.execute(query_insert_data_to_students_table, (json.dumps(data_students),))

        out_files_names: list = ['students_by_rooms_num', 'top_5_lowest_avg_age', 'top_5_highest_age_diff',
                                 'room_diversity_list']

        if out_files_extension:
            for query, file_name in zip(result_queries_list, out_files_names):
                cur.execute(query)
                result: list = cur.fetchall()
                path_to_save: str = f'{out_folder}/{file_name}.{out_files_extension}'
                FileManager().save_to_file(result[0][0], path_to_save)


if __name__ == "__main__":
    work_with_postresql()
