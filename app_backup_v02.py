# ============================================
# DCARuntime
# app.py
# Versão: 0.2.0
# ============================================

from rich.console import Console
from rich.panel import Panel
from datetime import datetime
import platform
import psutil
import time

from database import Database


console = Console()


# ============================================
# LOG
# ============================================

class Logger:

    def __init__(self, database=None):
        self.database = database

    def info(self, msg):

        console.print(f"[cyan][INFO][/cyan] {msg}")

        if self.database:
            self.database.add_log(
                "INFO",
                str(msg)
            )


    def success(self, msg):

        console.print(f"[green][ OK ][/green] {msg}")

        if self.database:
            self.database.add_log(
                "SUCCESS",
                str(msg)
            )


    def warning(self, msg):

        console.print(f"[yellow][WARN][/yellow] {msg}")

        if self.database:
            self.database.add_log(
                "WARNING",
                str(msg)
            )


    def error(self, msg):

        console.print(f"[red][ERRO][/red] {msg}")

        if self.database:
            self.database.add_log(
                "ERROR",
                str(msg)
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
# HARDWARE
# ============================================

class Hardware:

    def cpu(self):

        return platform.processor()


    def system(self):

        return platform.system()


    def version(self):

        return platform.version()


    def architecture(self):

        return platform.machine()


    def ram(self):

        return round(
            psutil.virtual_memory().total / 1024 ** 3,
            2
        )


    def cores(self):

        return psutil.cpu_count(
            logical=False
        )


    def threads(self):

        return psutil.cpu_count()


    def disk(self):

        return round(
            psutil.disk_usage("/").total / 1024 ** 3,
            2
        )


# ============================================
# MODULE
# ============================================

class Module:

    def __init__(self, name, logger):

        self.name = name
        self.loaded = False
        self.logger = logger


    def load(self):

        self.loaded = True

        self.logger.success(
            f"Módulo carregado -> {self.name}"
        )


    def unload(self):

        self.loaded = False

        self.logger.warning(
            f"Módulo descarregado -> {self.name}"
        )


# ============================================
# MODULE MANAGER
# ============================================

class ModuleManager:

    def __init__(self, logger):

        self.modules = []
        self.logger = logger


    def register(self, module):

        self.modules.append(module)


    def load_all(self):

        for module in self.modules:

            module.load()


    def unload_all(self):

        for module in self.modules:

            module.unload()


# ============================================
# RUNTIME
# ============================================

class Runtime:

    VERSION = "0.2.0"

    NAME = "DCARuntime"


    def __init__(self):

        # Banco
        self.database = Database()

        # Logger
        self.logger = Logger(
            self.database
        )

        # Componentes
        self.kernel = Kernel(
            self.logger
        )

        self.hardware = Hardware()

        self.modules = ModuleManager(
            self.logger
        )

        self.session_id = None



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



    def load_modules(self):

        plugins = [

            "Hardware",

            "System",

            "Runtime API",

            "Plugin Manager"

        ]


        for plugin in plugins:

            self.modules.register(

                Module(
                    plugin,
                    self.logger
                )

            )


        self.modules.load_all()



    def hardware_info(self):

        console.print()

        console.print(
            "[bold cyan]Hardware[/bold cyan]"
        )

        print("-------------------------------")

        print(
            "Sistema :",
            self.hardware.system()
        )

        print(
            "Versão :",
            self.hardware.version()
        )

        print(
            "CPU :",
            self.hardware.cpu()
        )

        print(
            "Arquitetura :",
            self.hardware.architecture()
        )

        print(
            "RAM :",
            self.hardware.ram(),
            "GB"
        )

        print(
            "Núcleos :",
            self.hardware.cores()
        )

        print(
            "Threads :",
            self.hardware.threads()
        )

        print(
            "Disco :",
            self.hardware.disk(),
            "GB"
        )

        print("-------------------------------")



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



    def start(self):

        self.banner()


        self.session_id = (

            self.database.runtime_start()

        )


        self.logger.info(
            datetime.now()
        )


        self.kernel.start()

        self.load_modules()

        self.hardware_info()

        self.loop()



    def stop(self):

        self.modules.unload_all()


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