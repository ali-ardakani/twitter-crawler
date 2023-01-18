# Base Crawler class

from abc import ABC, abstractmethod


class CrawlerInterface(ABC):    
    @abstractmethod
    def get_data_with_keyword(self, keyword):
        """Get data with keyword"""
        pass