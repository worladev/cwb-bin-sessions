'''
SESSION 24 (01/10/2023)
Mentor and Facilitator ==> ANDY AFFUL

TITLE: Dynamic Web App Configuration Loader

PROBLEM STATEMENT: You are working on a web application that requires various configurations like database
credentials, API keys, and other settings. Instead of hardcoding these configurations directly into the
application, they are stored in a configuration file named "config.ini". Each configuration item has a key and
a value, and they are stored in the following format:

---------------------------
|[Database]              |
|host = localhost        |
|port = 3306             |
|username = myuser       |
|password = mypassword   |
|                        |
|[API]                   |
|key = abcdef12345       |
|                        |
|[General]               |
|debug = true            |
--------------------------

Write a Python program to read the configurations from "config.ini" and dynamically create configuration objects
for different parts of your web application using enums. Implement the following:

CONFIGURATION OBJECT CREATION:
Create an enum ConfigType with values DATABASE, API, and GENERAL representing different configuration types.
Implement a function load_config(filename: str) that reads the configurations from "config.ini" and returns
instances of the appropriate configuration classes based on the config type enums.

WEB APPLICATION USAGE:
Simulate the usage of these configurations in a web application scenario. For example, print the database host
and API key to simulate their usage in database connection and API calls.

CONSTRAINTS:
The keys and values in the configuration file are non-empty strings with a maximum length of 100 characters.
The configuration file will have at most 50 configuration items.

Example:

from enum import Enum

class ConfigType(Enum):

class Config:

def load_config(filename):
    # Read configurations from the file and return a dictionary with ConfigType enums as keys
    # ...

# Usage
filename = "config.ini"
configurations = load_config(filename)

database_config = configurations[ConfigType.DATABASE]
api_config = configurations[ConfigType.API]
general_config = configurations[ConfigType.GENERAL]

print("Database Host:", database_config.host)
print("API Key:", api_config.key)
print("Debug Mode:", general_config.debug)
'''
from enum import Enum
import configparser

# a class to handle constant enum values mapping to the sections in the config.ini file
class ConfigType(Enum):
    DATABASE = "Database"
    API = "API"
    GENERAL = "General"

# a class to handle the Database section of the config.ini file
class ConfigDatabase:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

# a class to handle the API section of the config.ini file
class ConfigApi:
    def __init__(self, key):
        self.key = key

# a class to handle the General section of the config.ini file
class ConfigGeneral:
    def __init__(self, debug):
        self.debug = debug
        
# method to create configuration based on the configuration type and data passed
def createConfig(config_type, config_data):
    if config_type == ConfigType.DATABASE:
        return ConfigDatabase(**config_data)
    if config_type == ConfigType.API:
        return ConfigApi(**config_data)
    if config_type == ConfigType.GENERAL:
        return ConfigGeneral(**config_data)

# method to read config.ini file and create a dictionary item.
def load_config(filename):
    # Read configurations from the file and return a dictionary with ConfigType enums as keys
    configData = dict()
    config = configparser.ConfigParser()
    config.read(filename)
    # loop through the sections in the config.ini file and create a dictionary where
      # the section header is key and the fields, values
    for section in config.sections():
        config_type = ConfigType[section.upper()]
        config_data = dict(config[section])
        # print(config_data)
        configData[config_type] = createConfig(config_type, config_data)
    return configData # return the dictionary


# Example Usage
filename = "config.ini"
configurations = load_config(filename)

# configuration instances on DATABASE, API and GENERAL data
database_config = configurations[ConfigType.DATABASE]
api_config = configurations[ConfigType.API]
general_config = configurations[ConfigType.GENERAL]
