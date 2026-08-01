"""
===========================================
DCARuntime Event Manager
Versão 1.0.0
===========================================
"""


from datetime import datetime



class EventManager:


    def __init__(self):

        self.listeners = {}



    def register(self, event, callback):

        if event not in self.listeners:

            self.listeners[event] = []


        self.listeners[event].append(
            callback
        )



    def emit(self, event, data=None):

        print(
            f"[EVENT] {event}"
        )


        if event in self.listeners:


            for callback in self.listeners[event]:

                callback(
                    data
                )



    def log_event(self, event):

        return {

            "event":
            event,

            "time":
            datetime.now().isoformat()

        }