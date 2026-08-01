"""
===========================================
DCARuntime Hardware Plugin
Versão 0.4.0
===========================================
"""

import platform
import psutil


class HardwarePlugin:

    NAME = "Hardware"

    VERSION = "1.0.0"


    def info(self):

        return {

            "Sistema": platform.system(),

            "Versão": platform.version(),

            "Arquitetura": platform.machine(),

            "CPU": platform.processor(),

            "Núcleos": psutil.cpu_count(logical=False),

            "Threads": psutil.cpu_count(),

            "RAM GB": round(
                psutil.virtual_memory().total / 1024**3,
                2
            ),

            "Disco GB": round(
                psutil.disk_usage("/").total / 1024**3,
                2
            )
        }


    def start(self):

        return {

            "plugin": self.NAME,

            "status": "online"

        }


    def stop(self):

        return {

            "plugin": self.NAME,

            "status": "offline"

        } 