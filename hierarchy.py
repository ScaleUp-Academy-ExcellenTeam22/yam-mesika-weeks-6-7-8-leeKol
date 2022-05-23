class User:
    """
        A User class. Holds the username, the password, and the user's file list.
    """
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.file_list = []


class SystemAdministrator(User):
    """
        A System Administrator class. An heir from the "User" class.
    """
    pass


class RegularUser(User):
    """
        A Regular User class. An heir from the "User" class.
    """
    pass


class UserManagementSystem:
    """
        A User Management System class. Holds a list of the users in the system.
    """
    def __init__(self):
        self.users = []


class File:
    """
        A File class. Holds the file name, its weight, its contents, and the user who created it.
    """
    def __init__(self, name: str, weight: int, content, creating_user: User):
        self.name = name
        self.weight = weight
        self.content = content
        self.creating_user = creating_user

    def read(self, user: User):
        """
            The function gets a user. It returns the content of the file if the user is the one who created it,
            or if the user is a system administrator. Else it returns None.
            :param user: The user who accessed the file.
            :return: The content of the file or None.
        """
        if user.username == self.creating_user.username or isinstance(user, SystemAdministrator):
            return self.content
        else:
            return None


class Folder:
    """
        A Folder class. Holds the folder name, and a list of the files it contains.
    """
    def __init__(self, name: str):
        self.name = name
        self.file_list = []


class TextualFile(File):
    """
        A Textual File class. An heir from the "File" class.
    """
    def count(self, string_to_search: str) -> int:
        """
            The function gets a string. The function returns how many times the string appeared in the file's content.
            :param string_to_search: The string to be searched in the file's content.
            :return: The number of instances of the string in the file's content.
        """
        return self.content.count(string_to_search)


class BinaryFile(File):
    """
        A Binary File class. An heir from the "File" class.
    """
    pass


class ImageFile(BinaryFile):
    """
        An Image File class. An heir from the "BinaryFile" class.
    """
    def get_dimensions(self) -> [int, int]:
        """
            The function returns the dimensions of the image.
            :return: The dimensions of the image.
        """
        pass
