# ============================================
# DCARuntime
# app.py
# Versão: 0.5.0
# ============================================

from rich.console import Console
from rich.panel import Panel
from datetime import datetime
import time

from database import Database
from plugin_loader import PluginLoader


console = Console()


# ============================================
# LOG
# ============================================

class Logger:

    def __init__(self, database=None):

        self.database = database


    def write(self, level, msg):

        console.print(
            f"[{level}] {msg}"
        )

        if self.database:

            self.database.add_log(
                level,
                str(msg)
            )


    def info(self, msg):

        self.write(
            "INFO",
            msg
        )


    def success(self, msg):

        self.write(
            "SUCCESS",
            msg
        )


    def warning(self, msg):

        self.write(
            "WARNING",
            msg
        )


    def error(self, msg):

        self.write(
            "ERROR",
            msg
        )



# ============================================
# KERNEL
# ============================================

class Kernel:


    def __init__(self, logger):

        self.running = False
        self.logger = logger



    def start(self):

        self.running = True

        self.logger.success(
            "Kernel iniciado"
        )



    def stop(self):

        self.running = False

        self.logger.warning(
            "Kernel finalizado"
        )



# ============================================
# RUNTIME
# ============================================

class Runtime:


    NAME = "DCARuntime"

    VERSION = "0.5.0"



    def __init__(self):


        # Banco

        self.database = Database()



        # Logger

        self.logger = Logger(
            self.database
        )



        # Kernel

        self.kernel = Kernel(
            self.logger
        )



        # Plugin System

        self.plugins = PluginLoader()



        self.session_id = None




    # ========================================
    # BANNER
    # ========================================

    def banner(self):

        console.print()


        console.print(

            Panel.fit(

                f"""
{self.NAME}

Versão {self.VERSION}

Inicializando plataforma...
""",

                border_style="cyan"

            )

        )



    # ========================================
    # PLUGINS
    # ========================================

    def load_plugins(self):

        self.logger.info(
            "Carregando plugins..."
        )


        self.plugins.load()



        self.plugins.start()




    # ========================================
    # LOOP
    # ========================================

    def loop(self):

        self.logger.info(
            "Entrando no loop principal"
        )


        for i in range(5):

            self.logger.info(
                f"Ciclo {i+1}"
            )

            time.sleep(1)



        self.logger.success(
            "Loop encerrado"
        )



    # ========================================
    # START
    # ========================================

    def start(self):


        self.banner()



        self.session_id = (

            self.database.runtime_start()

        )



        self.logger.info(
            datetime.now()
        )



        self.kernel.start()



        self.load_plugins()



        self.loop()




    # ========================================
    # STOP
    # ========================================

    def stop(self):


        self.plugins.stop()



        self.kernel.stop()



        if self.session_id:


            self.database.runtime_stop(

                self.session_id

            )



        self.database.close()



# ============================================
# MAIN
# ============================================


if __name__ == "__main__":


    runtime = Runtime()



    try:

        runtime.start()



    except KeyboardInterrupt:


        runtime.logger.warning(

            "Interrompido pelo usuário"

        )



    finally:


        runtime.stop()