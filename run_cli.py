"""
Main module to work with PostgreSQL through CLI.
"""
import click
import json
from utils.conn_cursor_context_manager import ConnectAndCursorManager
from utils.file_manager import FileManager
from utils.sql_queries_collection import query_insert_data_to_rooms_table, query_insert_data_to_students_table,\
    QueryCreator
from utils.logger_util import Logger


@click.command()
@click.option("--rooms-file", "-rf", default=None, help="Path to json file to insert data in rooms table.",
              type=click.Path(exists=True, dir_okay=False))
@click.option("--students-file", "-sf", default=None, help="Path to json file to insert data in students table.",
              type=click.Path(exists=True, dir_okay=False))
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
            Logger().logger().info(f'Trying to insert data into rooms and students tables')
            data_rooms: list = FileManager().read_json_file(rooms_file)
            data_students: list = FileManager().read_json_file(students_file)
            cur.execute(query_insert_data_to_rooms_table, (json.dumps(data_rooms),))
            cur.execute(query_insert_data_to_students_table, (json.dumps(data_students),))

        out_files_names: list = ['students_num', 'top_5_lowest_avg_age', 'top_5_highest_age_diff',
                                 'room_diversity_list']

        if out_files_extension:
            Logger().logger().info('Trying to save results of the queries')
            if out_files_extension == "json":
                result_queries_list = QueryCreator().return_json_query(out_files_names)
            elif out_files_extension == "xml":
                result_queries_list = QueryCreator().return_xml_query(out_files_names)
            else:
                raise Exception('Value of out_files_extension is incorrect')

            for query, file_name in zip(result_queries_list, out_files_names):
                cur.execute(query)
                result: list = cur.fetchall()
                path_to_save: str = f'{out_folder}/{file_name}.{out_files_extension}'
                FileManager().save_to_file(result[0][0], path_to_save)


if __name__ == "__main__":
    work_with_postresql()
