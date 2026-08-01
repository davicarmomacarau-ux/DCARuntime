"""
===========================================
DCARuntime Config Manager
Versão 1.0.0
===========================================
"""

import json
import os



class ConfigManager:


    FILE = "dcaruntime.json"



    def __init__(self):

        self.config = {}



    def create_default(self):

        self.config = {

            "name":
            "DCARuntime",

            "version":
            "0.6.0",

            "plugins":
            True,

            "database":
            True,

            "security":
            True

        }


        self.save()



    def load(self):

        if not os.path.exists(self.FILE):

            self.create_default()


        with open(
            self.FILE,
            "r"
        ) as file:

            self.config = json.load(file)


        return self.config



    def save(self):

        with open(
            self.FILE,
            "w"
        ) as file:

            json.dump(

                self.config,

                file,

                indent=4

            )



    def get(self, key):

        return self.config.get(key)



    def set(self, key, value):

        self.config[key] = value

        self.save()