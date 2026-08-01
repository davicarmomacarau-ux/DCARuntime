from core.service_manager import ServiceManager


manager = ServiceManager()


print("======================")
print("SERVICE MANAGER")
print("======================")


for service in manager.list_services()[:20]:

    print(service)