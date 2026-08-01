"""
===========================================
DCARuntime Network Plugin
Versão 1.0.0
===========================================
"""

import socket
import platform


class NetworkPlugin:

    NAME = "Network"

    VERSION = "1.0.0"


    def hostname(self):

        return socket.gethostname()


    def local_ip(self):

        try:

            hostname = socket.gethostname()

            ip = socket.gethostbyname(
                hostname
            )

            return ip

        except Exception:

            return "Indisponível"



    def system(self):

        return platform.system()



    def info(self):

        return {

            "Hostname":
            self.hostname(),

            "IP Local":
            self.local_ip(),

            "Sistema":
            self.system()

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