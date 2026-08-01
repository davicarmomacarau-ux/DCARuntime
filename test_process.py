from core.process_manager import ProcessManager


manager = ProcessManager()


print("======================")
print("PROCESS MANAGER")
print("======================")


for process in manager.list_processes()[:10]:

    print(
        process
    )