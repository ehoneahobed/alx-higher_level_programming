#!/usr/bin/python3
"""This module contains a class to serve as base for other classes"""


import csv
import json
import os


class Base:
    """Represents base of all classes created """

    __nb_objects = 0

    def __init__(self, id=None):
        """ """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(i) == dict for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON representation to file"""
        if list_objs is None or list_objs == []:
            jstr = "[]"
        else:
            json_string = cls.to_json_string([i.to_dictionary() for i in
                                              list_objs])
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representations"""
        json_string_list = []

        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            json_string_list = json.loads(json_string)

        return json_string_list

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        # create an instance of an existing class
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        file_name = cls.__name__ + ".json"
        list_of_instances = []
        list_dictionaries = []

        if os.path.exists(file_name):
            with open(file_name, 'r') as my_file:
                my_str = my_file.read()
                list_dictionaries = cls.from_json_string(my_str)
                for dictionary in list_dictionaries:
                    list_of_instances.append(cls.create(**dictionary))
        return list_of_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs and saves to file"""

        if (type(list_objs) != list and list_objs is not None
           or not all(isinstance(i, cls) for i in list_objs)):

            raise TypeError("list_objs must be a list of instances")

        # file_name = cls.__name__ + ".csv"
        # with open(file_name, 'w') as my_file:
        #     if list_objs is not None:
        #         list_objs = [i.todictionary for i in list_objs]
        #         if cls.__name__ == 'Rectangle':
        #             records = ['id', 'width', 'height', 'x', 'y']
        #         elif cls.__name__ == 'Square':
        #             records = ['id', 'size', 'x', 'y']
        #         script = csv.DictWriter(my_file, fieldnames=records)
        #         script.writeheader()
        #         script.writerows(list_objs)

        name_of_file = cls.__name__ + ".csv"
        with open(name_of_file, "w", newline="") as nof:
            if list_objs is None or list_objs == []:
                nof.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    records = ["id", "width", "height", "x", "y"]
                else:
                    records = ["id", "size", "x", "y"]
                creator = csv.DictWriter(nof, records)
                for obj in list_objs:
                    creator.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file"""

        # file_name = cls.__name__ + ".csv"
        # list_of_instances = []
        # if os.path.exists(file_name):
        #     with open(file_name, 'r') as my_file:
        #         reader = csv.reader(my_file, delimiter=',')
        #         if cls.__name__ == 'Rectangle':
        #             records = ['id', 'width', 'height', 'x', 'y']
        #         elif cls.__name__ == 'Square':
        #             records = ['id', 'size', 'x', 'y']
        #         for i, row in enumerate(reader):
        #             if i > 0:
        #                 x = cls(1, 1)
        #                 for j, y in enumerate(row):
        #                     if y:
        #                         setattr(x, records[j], int(y))
        #                 list_of_instances.append(x)
        # return list_of_instances

        name_of_file = cls.__name__ + ".csv"
        try:
            with open(name_of_file, "r", newline="") as nof:
                if cls.__name__ == "Rectangle":
                    rec_instances = ["id", "width", "height", "x", "y"]
                else:
                    sq_instances = ["id", "size", "x", "y"]
                    list_of_dicts = csv.DictReader(nof,
                                                   rec_instances=sq_instances)
                    list_of_dicts = [dict([key, int(value)]
                                     for key, value in d.items())
                                     for d in list_of_dicts]
                    return [cls.create(**d) for d in list_of_dicts]
        except IOError:
            return []