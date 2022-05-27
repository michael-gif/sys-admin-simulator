class FileSystem:
    def __init__(self):
        self.drives = {}

    def get(self, drive_letter):
        return self.drives[drive_letter]

    def contains(self, drive):
        self.drives[drive.letter] = drive
        return self

class Drive:
    def __init__(self, letter):
        self.letter = letter
        self.contents = {}

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
        return self

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