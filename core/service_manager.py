"""
===========================================
DCARuntime Service Manager
Versão 1.0.0
===========================================
"""

import subprocess



class ServiceManager:


    def list_services(self):

        services = []


        command = [
            "powershell",
            "-Command",
            "Get-Service | Select Name,Status"
        ]


        result = subprocess.run(

            command,

            capture_output=True,

            text=True

        )


        lines = result.stdout.splitlines()


        for line in lines[3:]:

            parts = line.split()


            if len(parts) >= 2:

                services.append({

                    "name": parts[0],

                    "status": parts[-1]

                })


        return services



    def find(self, name):

        result = []


        for service in self.list_services():

            if name.lower() in service["name"].lower():

                result.append(service)


        return result