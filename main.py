import string

import pygame
import time

from key_handler import KeyHandler
from event_system import event_handler, Event
from computers import SysAdmin, Server
from command_manager import command_manager

computers = [SysAdmin, Server]
localhost = computers[0]
prev_localhost = localhost
ssh_session = False

pygame.init()
screen = pygame.display.set_mode((800, 400))  # , pygame.FULLSCREEN)
pygame.display.set_caption(f"cmd.exe - {localhost.hostname}")
clock = pygame.time.Clock()

history = []
visible_history = []
command_history = []
x, y = screen.get_size()
possible_lines = ((y - 5) // localhost.font_size) - 1
mouse_wheel_offset = 0


def render_history():
    global visible_history, mouse_wheel_offset
    if mouse_wheel_offset < 0:
        mouse_wheel_offset = 0
    if mouse_wheel_offset > len(history) - possible_lines:
        mouse_wheel_offset = len(history) - possible_lines
    if len(history) > possible_lines:
        visible_history = history[possible_lines * -1 - mouse_wheel_offset:len(history) - mouse_wheel_offset + 1]
    else:
        visible_history = history
    for i in range(len(visible_history)):
        text = localhost.font.render(str(visible_history[i]), False, localhost.font_color)
        screen.blit(text, (5, 5 + (i * localhost.font_size)))


def console(message):
    history.append(message)


prev_time = 0
cursor_delay = 0.5
cursor_visible = False


def render_input():
    global cursor_visible, prev_time
    text = localhost.font.render(localhost.CD + "> " + key_handler.command_input, False, localhost.font_color)
    if mouse_wheel_offset <= 0:
        screen.blit(text, (5, 5 + (localhost.font_size * len(visible_history))))
    if time.time() - prev_time >= cursor_delay:
        cursor_visible = not cursor_visible
        prev_time = time.time()
    if cursor_visible and mouse_wheel_offset <= 0:
        cd_w, cd_l = localhost.font.size(localhost.CD + "> " + key_handler.command_input)
        pygame.draw.line(screen, (255, 255, 255), (cd_w + 5, 5 + (localhost.font_size * (len(visible_history) + 1))),
                         (cd_w + 10, 5 + (localhost.font_size * (len(visible_history) + 1))), 1)


def process_command(command):
    command += " "
    parts = []
    quote_counter = 0
    prev_index = 0
    for i in range(len(command)):
        if command[i] == "\"":
            quote_counter += 1
        if command[i] == " " and quote_counter % 2 == 0:
            parts.append(command[prev_index:i])
            prev_index = i + 1
    command_manager.execute(parts[0], parts[1:])


def cd_command(args):
    if not args:
        console(localhost.CD)
    else:
        path = args[0].lower()
        if path == '.' or path == './':
            return
        if path == '..':
            if len(localhost.CD) == 2 and localhost.CD.endswith(":") and localhost.CD[0] in string.ascii_letters:
                return
            absolute_path = '/'.join(localhost.CD.split('/')[:-1])
        elif path.startswith('./'):
            absolute_path = localhost.CD + path[1:]
        elif path.startswith(localhost.CD + "/"):
            absolute_path = path
        else:
            if path.startswith("\"") and path.endswith("\""):
                path = path[1:-1]
            if len(path) == 2 and path.endswith(":") and path[0] in string.ascii_letters:
                absolute_path = path
            else:
                absolute_path = localhost.CD + "/" + path
        full_path = localhost.path_exists(absolute_path)
        if full_path:
            localhost.CD = full_path
            key_handler.CD = localhost.CD
        else:
            console("Could not find the path specified")


def dir_command(args):
    folder = localhost.get_folder(localhost.CD)
    for key in folder.contents:
        console(key)
    console("")


def help_command(args):
    console("This is the help page")


def cls_command(args):
    history.clear()


def exit_command(args):
    global running, ssh_session, localhost
    if ssh_session:
        localhost = prev_localhost
        console(f"Stopped SSH session {localhost.hostname}@{localhost.ip}")
        ssh_session = False
        return
    running = False


def color_command(args):
    colors = {'1': (10, 42, 218),
              '2': (19, 161, 14),
              '3': (58, 150, 221),
              '4': (197, 15, 31),
              '5': (136, 23, 152),
              '6': (193, 156, 0),
              '7': (255, 255, 255),
              '8': (118, 118, 118),
              '9': (45, 120, 255),
              }
    if not args:
        localhost.font_color = colors['7']
        return
    if args[0] in colors:
        localhost.font_color = colors[args[0]]
    else:
        console(f"Unknown color {args[0]}")


def ipconfig_command(args):
    console(localhost.ip)
    console("")


def ssh_command(args):
    global localhost, ssh_session, prev_localhost
    for computer in computers:
        if computer.hostname != "SysAdmin":
            if computer.ip == args[0]:
                prev_localhost = localhost
                localhost = computer
                console(f"Started SSH session {localhost.hostname}@{localhost.ip}")
                ssh_session = True
            else:
                console(f"Unknown ip {args[0]}")


def net_command(args):
    if not args:
        return
    if args[0] == "share":
        if len(args) == 1:
            for share in localhost.shares:
                console(f"Share name: {share.name} Resource: {share.path}")
    if args[0] == "view":
        if len(args) > 1:
            if not args[1].startswith("\\\\"):
                console("The network path was not found")
                return
            args[1] = args[1][2:]
            addresses = [c.ip for c in computers]
            hostnames = [c.hostname for c in computers]
            computer = None
            if args[1] in addresses or args[1] in hostnames:
                computer = [c for c in computers if c.hostname == args[1] or c.ip == args[1]][0]
            if not computer:
                console("The network path was not found")
                return
            for share in computer.shares:
                console(f"Share name: {share.name} Resource: {share.path}")
        else:
            for c in computers:
                console(f"Hostname: {c.hostname} Address: {c.ip}")


def whoami_command(args):
    console(localhost.hostname)


event_handler.add_event(Event("process input", process_command))
command_manager.add_command("cd", cd_command)
command_manager.add_command("help", help_command)
command_manager.add_command("cls", cls_command)
command_manager.add_command("exit", exit_command)
command_manager.add_command("color", color_command)
command_manager.add_command("dir", dir_command)
command_manager.add_command("ipconfig", ipconfig_command)
command_manager.add_command("ssh", ssh_command)
command_manager.add_command("net", net_command)
command_manager.add_command("whoami", whoami_command)

key_handler = KeyHandler(localhost.CD, history, command_history)
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            key_handler.tick(event.key)
        if event.type == pygame.MOUSEWHEEL:
            mouse_wheel_offset += event.y
    screen.fill((0, 0, 0))
    render_history()
    render_input()
    pygame.display.update()
