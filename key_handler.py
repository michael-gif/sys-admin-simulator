import pygame
import string

from event_system import event_handler

class KeyHandler:
    def __init__(self, CD, history, command_history):
        self.CD = CD
        self.history = history
        self.command_history = command_history
        self.command_input = ""
        self.temp_input = ""
        self.left_shift = False
        self.right_shift = False
        self.left_ctrl = False
        self.history_index = 0

    def tick(self, key):
        key_ascii = pygame.key.name(key)

        # sticky keys
        if not pygame.key.get_pressed()[pygame.K_LSHIFT] and self.left_shift:
            self.left_shift = False
        if not pygame.key.get_pressed()[pygame.K_RSHIFT] and self.right_shift:
            self.left_shift = False
        if not pygame.key.get_pressed()[pygame.K_LCTRL] and self.left_ctrl:
            self.left_ctrl = False
        if key_ascii == "left shift":
            if not self.left_shift:
                self.left_shift = True
        if key_ascii == "right shift":
            if not self.right_shift:
                self.right_shift = True
        if key_ascii == "left ctrl":
            if not self.left_ctrl:
                self.left_ctrl = True

        # alpha numerical keys
        if key_ascii in string.ascii_lowercase:
            if self.left_shift or self.right_shift:
                self.command_input += key_ascii.upper()
                return
            self.command_input += key_ascii
        if key_ascii in string.digits:
            self.command_input += key_ascii

        # other keys
        if key_ascii == "return":
            self.history.append(f"{self.CD}> {self.command_input}")
            self.command_history.append(self.command_input)
            self.command_input = ""
            event_handler.fire("process input", (self.command_history[-1]))
        if key_ascii == "space":
            self.command_input += " "
        if key_ascii == "backspace":
            if self.left_ctrl:
                split_command = self.command_input.split(" ")
                split_command.pop(-1)
                self.command_input = " ".join(split_command)
                return
            self.command_input = self.command_input[:-1]

        # cycle through previous commands
        if key_ascii == "up" or key_ascii == "down":
            if self.history_index == 0:
                self.temp_input = self.command_input
        if key_ascii == "up" and self.history:
            if abs(self.history_index) < len(self.command_history):
                self.history_index -= 1
            self.command_input = self.command_history[self.history_index]
        if key_ascii == "down" and self.history:
            self.history_index += 1
            if self.history_index < 0:
                self.command_input = self.command_history[self.history_index]
            else:
                self.command_input = self.temp_input
                self.history_index = 0
