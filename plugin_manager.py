import os
import importlib


class PluginManager:


    def __init__(self):

        self.plugins = []



    def discover(self):

        folder = "plugins"


        for name in os.listdir(folder):

            path = os.path.join(
                folder,
                name
            )


            if os.path.isdir(path):

                if name.startswith("__"):
                    continue


                try:

                    module = importlib.import_module(
                        f"plugins.{name}.plugin"
                    )


                    for item in dir(module):

                        obj = getattr(
                            module,
                            item
                        )


                        if isinstance(obj, type):

                            if item.endswith("Plugin"):

                                self.plugins.append(
                                    obj()
                                )


                except Exception as error:

                    print(
                        "Erro carregando plugin:",
                        name,
                        error
                    )



    def start_all(self):

        for plugin in self.plugins:

            print(
                plugin.start()
            )



    def stop_all(self):

        for plugin in self.plugins:

            print(
                plugin.stop()
            )



    def list(self):

        return self.plugins
        def details(self):
            details = []


            for plugin in self.plugins:

                details.append(
                    plugin.info()
                )


            return details
            def details(self):
                data = []

        for plugin in self.plugins:

            item = {

                "name":
                plugin.NAME,

                "version":
                plugin.VERSION

            }

            if hasattr(plugin, "info"):

                item["info"] = plugin.info()


            data.append(item)


        return data