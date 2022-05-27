import pygame

pygame.font.init()

class Computer:
    def __init__(self):
        self.drives = {}
        self.CD = "C:"
        self.font_size = 12
        self.font_color = (255, 255, 255)
        self.font = pygame.font.SysFont("Consolas", self.font_size)

    def get(self, drive_letter):
        for drive in self.drives:
            if drive_letter.lower() == drive.lower():
                return self.drives[drive]

    def get_folder(self, path):
        absolute_path = self.path_exists(path)
        parts = absolute_path.split("/")
        parts[0] = parts[0][0]
        location = self
        for part in parts:
            location = location.get(part)
        return location

    def contains(self, drive):
        self.drives[drive.letter] = drive
        return self

    def path_exists(self, path):
        components = path.split('/')
        components[0] = components[0][0]
        part = self
        absolute_path = components[0] + ":"
        for i in range(len(components)):
            part = part.get(components[i])
            if type(part) == Drive:
                absolute_path = part.letter + ":"
            if type(part) == Folder:
                absolute_path += "/" + part.name
            if not part:
                return False
        return absolute_path


class Drive:
    def __init__(self, letter):
        self.letter = letter
        self.contents = {}

    def get(self, name):
        for key in self.contents:
            if name.lower() == key.lower():
                return self.contents[key]

    def contains(self, object):
        self.contents[object.name] = object
        return self


class File():
    def __init__(self, name):
        self.name = name
        self.extension = ""
        self.contents = ""


class Folder():
    def __init__(self, name):
        self.name = name
        self.contents = {}

    def get(self, name):
        for key in self.contents:
            if name.lower() == key.lower():
                return self.contents[key]

    def contains(self, object):
        self.contents[object.name] = object
        return self


SysAdmin = Computer()
SysAdmin.contains(Drive("C")
                   .contains(Folder("Windows"))
                   .contains(Folder("Users")
                             .contains(Folder("Default"))
                             .contains(Folder("Michael Franco")
                                       .contains(Folder("Desktop"))
                                       .contains(Folder("Documents"))
                                       .contains(Folder("3D Objects"))
                                       .contains(Folder("Contacts"))
                                       .contains(Folder("Downloads"))
                                       .contains(Folder("AppData"))
                                       .contains(Folder("Favorites"))
                                       .contains(Folder("Links"))
                                       .contains(Folder("Favorites"))
                                       .contains(Folder("Links"))
                                       .contains(Folder("Music"))
                                       .contains(Folder("OneDrive"))
                                       .contains(Folder("Pictures"))
                                       .contains(Folder("Saved Games"))
                                       .contains(Folder("Searches"))
                                       .contains(Folder("Videos"))
                                       ))
                   .contains(Folder("Programs"))
                   .contains(Folder("Programs (x86)"))
                   )
SysAdmin.contains(Drive("D"))

Server = Computer()
Server.contains(Drive("C")
                   .contains(Folder("Windows"))
                   .contains(Folder("Users")
                             .contains(Folder("Default"))
                             .contains(Folder("Ligma Balls")
                                       .contains(Folder("Desktop"))
                                       .contains(Folder("Documents"))
                                       .contains(Folder("3D Objects"))
                                       .contains(Folder("Contacts"))
                                       .contains(Folder("Downloads"))
                                       .contains(Folder("AppData"))
                                       .contains(Folder("Favorites"))
                                       .contains(Folder("Links"))
                                       .contains(Folder("Favorites"))
                                       .contains(Folder("Links"))
                                       .contains(Folder("Music"))
                                       .contains(Folder("OneDrive"))
                                       .contains(Folder("Pictures"))
                                       .contains(Folder("Saved Games"))
                                       .contains(Folder("Searches"))
                                       .contains(Folder("Videos"))
                                       ))
                   .contains(Folder("Programs"))
                   .contains(Folder("Programs (x86)"))
                   )