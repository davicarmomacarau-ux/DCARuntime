"""
===========================================
DCARuntime Security Plugin
Versão 1.0.0
===========================================
"""

import platform
import getpass
import os
import socket


class SecurityPlugin:

    NAME = "Security"

    VERSION = "1.0.0"


    # ======================================
    # USUÁRIO ATUAL
    # ======================================

    def username(self):

        return getpass.getuser()



    # ======================================
    # COMPUTADOR
    # ======================================

    def hostname(self):

        return socket.gethostname()



    # ======================================
    # SISTEMA
    # ======================================

    def system(self):

        return {

            "Sistema":
            platform.system(),

            "Versão":
            platform.version(),

            "Arquitetura":
            platform.machine()

        }



    # ======================================
    # AMBIENTE
    # ======================================

    def environment(self):

        return {

            "Usuário":
            self.username(),

            "Computador":
            self.hostname(),

            "Diretório":
            os.getcwd()

        }



    # ======================================
    # INFORMAÇÕES DE SEGURANÇA
    # ======================================

    def info(self):

        data = {}

        data.update(
            self.system()
        )

        data.update(
            self.environment()
        )


        return data



    # ======================================
    # START
    # ======================================

    def start(self):

        return {

            "plugin":
            self.NAME,

            "status":
            "online"

        }



    # ======================================
    # STOP
    # ======================================

    def stop(self):

        return {

            "plugin":
            self.NAME,

            "status":
            "offline"

        }