"""
module contains class  FileManager
"""
import json
from typing import Union
from utils.logger_util import Logger


class FileManager:
    """
    class contains static methods for reading json files
    and saving json and xml data to corresponding file
    """

    @staticmethod
    def read_json_file(path: str) -> Union[dict, list]:
        """
        static method to read json files
        :param path: path to read json file from
        :type:path: str
        :return: list of dicts of data
        """
        Logger().logger().info(f'Trying to read json file using path: {path}')
        with open(path) as data_file:
            data: dict = json.load(data_file)
            return data

    @staticmethod
    def save_to_file(input_data: Union[dict, str], path: str):
        """
        static method to save dict to json or xml file
        :param input_data: input data to save as json file
        :type:input_data: dict or str
        :param path: path to save data as json or xml file
        :type:path: str
        """
        if path.endswith('.json'):
            Logger().logger().info(f'Trying to save data as json file to "{path}"')
            with open(path, "w") as outfile:
                json.dump(input_data, outfile)
        elif path.endswith('.xml'):
            Logger().logger().info(f'Trying to save data as xml file to "{path}"')
            with open(path, "w") as outfile:
                outfile.write(input_data)
        else:
            raise Exception("Wrong output file extension")
