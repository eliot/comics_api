from enum import Enum

class ScrapeSiteType(Enum):
    COMIXOLOGY = 1

class ComixologyScrapeItemTypes(Enum):
    ISSUE = 1
    CREATOR = 2
    GENRE = 3
    PUBLISHER = 4
    STORYARC = 5
    SERIES = 6
