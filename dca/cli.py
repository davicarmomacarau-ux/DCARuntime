import sys
from pathlib import Path


# ==========================================
# LOCALIZA A RAIZ DO PROJETO
# ==========================================

ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(ROOT))


# ==========================================
# IMPORTS DO PROJETO
# ==========================================

from database import Database
from app import Runtime



# ==========================================
# INFORMAÇÕES
# ==========================================

def show_info():

    print("""
=========================
 DCARuntime 0.3.0
=========================
""")

    runtime = Runtime()

    print("Sistema:")
    print(runtime.hardware.system())

    print("\nCPU:")
    print(runtime.hardware.cpu())

    print("\nRAM:")
    print(runtime.hardware.ram(), "GB")



# ==========================================
# LOGS
# ==========================================

def show_logs():

    db = Database()

    print("\n=== LOGS ===\n")


    for log in db.get_logs():

        print(
            f"[{log['level']}] {log['message']}"
        )


    db.close()



# ==========================================
# PLUGINS
# ==========================================

def show_plugins():

    db = Database()

    print("\n=== PLUGINS ===\n")


    for plugin in db.plugins():

        status = (
            "ATIVO"
            if plugin["enabled"]
            else "DESATIVADO"
        )


        print(
            plugin["name"],
            "-",
            status
        )


    db.close()



# ==========================================
# START RUNTIME
# ==========================================

def start_runtime():

    runtime = Runtime()

    runtime.start()

    runtime.stop()



# ==========================================
# MENU
# ==========================================

def menu():

    while True:

        print("""
=====================
 DCARuntime CLI
=====================

1 - Info
2 - Logs
3 - Plugins
4 - Iniciar Runtime
5 - Sair

""")


        option = input("Escolha: ")



        if option == "1":

            show_info()


        elif option == "2":

            show_logs()


        elif option == "3":

            show_plugins()


        elif option == "4":

            start_runtime()


        elif option == "5":

            print("Encerrando DCARuntime...")

            break


        else:

            print("Opção inválida")



# ==========================================
# EXECUÇÃO
# ==========================================

if __name__ == "__main__":

    menu()