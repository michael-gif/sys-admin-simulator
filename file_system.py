import string


class FileSystem:
    def __init__(self):
        self.drives = {}

    def get(self, drive_letter):
        for drive in self.drives:
            if drive_letter.lower() == drive.lower():
                return self.drives[drive]

    def contains(self, drive):
        self.drives[drive.letter] = drive
        return self

    def path_exists(self, path):
        if len(path) == 2 and path.endswith(':') and path[0] in string.ascii_letters:
            if not self.get(path[0]):
                return False
            return path
        components = path.split('/')
        components[0] = components[0][0]
        part = self
        absolute_path = components[0] + ":"
        for i in range(len(components)):
            part = part.get(components[i])
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


hard_disk = FileSystem()
hard_disk.contains(Drive("C")
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
hard_disk.contains(Drive("D"))
