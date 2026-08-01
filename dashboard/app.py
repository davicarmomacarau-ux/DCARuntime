from flask import Flask, render_template

import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

sys.path.append(str(ROOT))


from plugin_manager import PluginManager
from plugin_loader import PluginLoader
from core.process_manager import ProcessManager
from core.service_manager import ServiceManager


app = Flask(__name__)


# ===============================
# DCARUNTIME DATA
# ===============================


def get_data():

    loader = PluginLoader()

    loader.load()


    plugins = []


    for plugin in loader.manager.list():

        plugins.append({

            "name": plugin.NAME,

            "version": plugin.VERSION,

            "status": "ONLINE"

        })


    processes = ProcessManager().list_processes()


    services = ServiceManager().list_services()


    return {

        "plugins": plugins,

        "processes": processes[:10],

        "services": services[:10]

    }



# ===============================
# HOME
# ===============================


@app.route("/")

def index():

    data = get_data()


    return render_template(

        "index.html",

        data=data

    )



if __name__ == "__main__":

    app.run(

        host="127.0.0.1",

        port=8000,

        debug=True

    )