import pathlib


class Storage:

    def __init__(self, sep : str) -> None:
        self.sep = sep
        self.__storage = open('path.txt', "r").readlines()

    def add_path(self, path: str) -> None:
        if ".." in path and len(self.__storage) != 1:
            self.__storage.pop(-1)
        elif ".." in path:
            print("Нельзя выйти из рабочей директории")
        else:
            self.__storage.append(path)

    def file2path(self, file_name: str) -> str:
        locale_storage = self.__storage.copy()
        locale_storage.append(file_name)
        abs_path = pathlib.Path(__file__).parent.absolute()
        return str(abs_path) + self.sep + self.sep.join(locale_storage)

    @property
    def path(self):
        abs_path = pathlib.Path(__file__).parent.absolute()
        return str(abs_path) + self.sep + self.sep.join(self.__storage)

    @property
    def upper_path(self):
        abs_path = pathlib.Path(__file__).parent.absolute()
        print(self.__storage[1:])
        return str(abs_path) + self.sep + self.sep.join(self.__storage[:1])