"""
===========================================
DCARuntime Process Manager
Versão 1.0.0
===========================================
"""

import psutil


class ProcessManager:


    def list_processes(self):

        processes = []


        for process in psutil.process_iter(
            [
                "pid",
                "name",
                "status"
            ]
        ):

            try:

                processes.append(

                    process.info

                )


            except:

                pass


        return processes



    def find(self, name):

        result = []


        for process in self.list_processes():

            if process["name"]:

                if name.lower() in process["name"].lower():

                    result.append(process)


        return result