class EventHandler:
    def __init__(self):
        self.events = {}
        self.fired_events = []

    def add_event(self, event):
        self.events[event.name] = event

    def contains(self, event_name):
        if event_name in self.events:
            return True
        return False

    def fire(self, event_name, args):
        self.events[event_name].fire(args)
        self.fired_events.append(self.events[event_name])


class Event:
    def __init__(self, name, callback):
        self.name = name
        self.callback = callback
        self.args = None

    def fire(self, args):
        self.args = args
        self.callback(args)


event_handler = EventHandler()
