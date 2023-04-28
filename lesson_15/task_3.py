CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0

    def first_channel(self):
        self.current_channel_index = 0
        return self.channels[self.current_channel_index]

    def last_channel(self):
        self.current_channel_index = len(self.channels) - 1
        return self.channels[self.current_channel_index]

    def turn_channel(self, channel_number):
        if channel_number > 0 and channel_number <= len(self.channels):
            self.current_channel_index = channel_number - 1
            return self.channels[self.current_channel_index]
        else:
            return "Invalid channel number."

    def next_channel(self):
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def previous_channel(self):
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def current_channel(self):
        return self.channels[self.current_channel_index]

    def is_exist(self, channel):
        if isinstance(channel, int):
            if channel > 0 and channel <= len(self.channels):
                return "Yes"
            else:
                return "No"
        elif isinstance(channel, str):
            if channel in self.channels:
                return "Yes"
            else:
                return "No"
        else:
            return "Invalid input."

controller = TVController(CHANNELS)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(4))
print(controller.is_exist("BBC"))
