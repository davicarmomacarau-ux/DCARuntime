from plugin_manager import PluginManager


manager = PluginManager()


manager.discover()


print("\nPLUGINS ENCONTRADOS:")


for plugin in manager.list():

    print(
        plugin.NAME,
        plugin.VERSION
    )


print("\nINICIANDO:")

manager.start_all()


print("\nPARANDO:")

manager.stop_all()