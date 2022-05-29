import pygame

pygame.font.init()


class Computer:
    def __init__(self, hostname, ip):
        self.drives = {}
        self.hostname = hostname
        self.ip = ip
        self.CD = "C:"
        self.font_size = 12
        self.font_color = (255, 255, 255)
        self.font = pygame.font.SysFont("Consolas", self.font_size)
        self.shares = []

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

    def build(self):
        for letter in self.drives:
            drive = self.drives[letter]
            if drive.shared:
                self.shares.append(Share(letter, letter + ":"))
            for name in drive.contents:
                folder = drive.contents[name]
                self.create_shares(folder, letter + ":/" + name)

    def create_shares(self, folder, path):
        if folder.shared:
            self.shares.append(Share(folder.name, path + "/" + folder.name))
        for f in folder.contents:
            self.create_shares(folder.contents[f], path + "/" + folder.name)

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
    def __init__(self, letter, shared=False):
        self.letter = letter
        self.name = letter
        self.contents = {}
        self.shared = shared

    def get(self, name):
        for key in self.contents:
            if name.lower() == key.lower():
                return self.contents[key]

    def contains(self, object):
        self.contents[object.name] = object
        return self


class Folder():
    def __init__(self, name, shared=False):
        self.name = name
        self.contents = {}
        self.shared = shared

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


class Share:
    def __init__(self, name, path):
        self.name = name
        self.path = path


SysAdmin = Computer("SysAdmin", "192.168.1.43")
SysAdmin.contains(Drive("C", shared=True)
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
SysAdmin.build()

Server = Computer("server", "10.1.1.1")
Server.contains(Drive("C", shared=True)
                .contains(Folder("Windows"))
                .contains(Folder("Users")
                          .contains(Folder("Default"))
                          .contains(Folder("Ligma Balls")
                                    .contains(Folder("Desktop", shared=True))
                                    .contains(Folder("Documents", shared=True))
                                    .contains(Folder("3D Objects", shared=True))
                                    .contains(Folder("Contacts", shared=True))
                                    .contains(Folder("Downloads", shared=True))
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
Server.build()
