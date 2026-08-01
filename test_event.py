from core.event_manager import EventManager



events = EventManager()



def plugin_started(data):

    print(
        "Plugin iniciado:",
        data
    )



events.register(
    "PLUGIN_STARTED",
    plugin_started
)



events.emit(
    "PLUGIN_STARTED",
    "Hardware"
)