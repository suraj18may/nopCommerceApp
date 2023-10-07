import configparser
config=configparser.RawConfigParser()
config.read(".\\Configrations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        URL=config.get("common info","baseURL")
        return URL

    @staticmethod
    def getUserName():
        username= config.get("common info", "Username")
        return username

    @staticmethod
    def getPassword():
        password= config.get("common info", "Password")
        return password