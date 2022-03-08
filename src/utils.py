import os


class utils:
    @staticmethod
    def clear():
        return os.system("cls" if os.name == "nt" else "clear")