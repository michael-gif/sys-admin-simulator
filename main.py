import os
import pygame
import time

from key_handler import KeyHandler
from event_system import event_handler, Event

pygame.init()
screen = pygame.display.set_mode((400, 400))  # , pygame.FULLSCREEN)
clock = pygame.time.Clock()
CD = "C:"
font_size = 12
font = pygame.font.SysFont("Consolas", font_size)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


history = []
command_history = []
def render_history():
    for i in range(len(history)):
        text = font.render(str(history[i]), False, (255, 255, 255))
        screen.blit(text, (5, 5 + (i * font_size)))

def console(message):
    history.append(message)

prev_time = 0
cursor_delay = 0.5
cursor_visible = False
def render_input():
    global cursor_visible, prev_time
    text = font.render(CD + "> " + key_handler.command_input, False, (255, 255, 255))
    screen.blit(text, (5, 5 + (font_size * len(history))))
    if time.time() - prev_time >= cursor_delay:
        cursor_visible = not cursor_visible
        prev_time = time.time()
    if cursor_visible:
        cd_w, cd_l = font.size(CD + "> " + key_handler.command_input)
        pygame.draw.line(screen, (255, 255, 255), (cd_w + 5, 5 + (font_size * (len(history) + 1))),
                         (cd_w + 10, 5 + (font_size * (len(history) + 1))), 1)


def process_command(command):
    parts = command.split(" ")
    if event_handler.contains(f"command: {parts[0]}"):
        event_handler.fire(f"command: {parts[0]}", parts[1:])


def cd_command(args):
    console(CD)


def help_command(args):
    console("This is the help page")


def cls_command(args):
    history.clear()


event_handler.add_event(Event("process input", process_command))
event_handler.add_event(Event("command: cd", cd_command))
event_handler.add_event(Event("command: help", help_command))
event_handler.add_event(Event("command: cls", cls_command))

key_handler = KeyHandler(CD, history, command_history)
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN:
            key_handler.tick(event.key)
    screen.fill((0, 0, 0))
    render_history()
    render_input()
    pygame.display.update()
