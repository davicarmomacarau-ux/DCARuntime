from plugin_manager import PluginManager


class PluginLoader:


    def __init__(self):

        self.manager = PluginManager()



    def load(self):

        print(
            "[PLUGIN] Procurando plugins..."
        )


        self.manager.discover()


        print(
            f"[PLUGIN] {len(self.manager.plugins)} plugins encontrados"
        )



    def start(self):

        self.manager.start_all()



    def stop(self):

        self.manager.stop_all()