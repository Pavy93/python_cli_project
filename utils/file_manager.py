"""
module contains class  FileManager
"""
import json


class FileManager:
    """
    class contains static methods for reading json files
    and saving json and xml data to corresponding file
    """

    @staticmethod
    def read_json_file(path: str) -> dict:
        """
        static method to read json files
        :param path: path to read json file from
        :type:path: str
        :return: dict of data
        """
        with open(path) as data_file:
            data: dict = json.load(data_file)
            return data

    @staticmethod
    def save_to_json_file(dict_data: dict, path: str):
        """
        static method to save dict to json file
        :param dict_data: input data to save as json file
        :type:dict_data: dict
        :param path: path to save data as json file
        :type:path: str
        """
        with open(path, "w") as outfile:
            json.dump(dict_data, outfile)

    @staticmethod
    def save_to_xml_file(xml_data: str, path: str):
        """
        static method to save xml data to xml file
        :param xml_data: input data to save as xml file
        :type:xml_data: str
        :param path: path to save data as xml file
        :type:path: str
        """
        with open(path, "w") as outfile:
            outfile.write(xml_data)
