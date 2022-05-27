class FileSystem:
    def __init__(self):
        self.drives = {}

    def get(self, drive_letter):
        if drive_letter in self.drives:
            return self.drives[drive_letter]

    def exists(self, drive_letter):
        return drive_letter in self.drives

    def contains(self, drive):
        self.drives[drive.letter] = drive
        return self

    def path_exists(self, path):
        if path.startswith("\"") and path.endswith("\""):
            path = path[1:-1]
        components = path.split('/')
        components[0] = components[0][0]
        part = self
        for i in range(len(components)):
            part = part.get(components[i])
            if not part:
                return False
        return True

class Drive:
    def __init__(self, letter):
        self.letter = letter
        self.contents = {}

    def get(self, name):
        print(name)
        if name in self.contents:
            return self.contents[name]

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
        if name in self.contents:
            return self.contents[name]

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
#print(hard_disk.drives['C'].contents)