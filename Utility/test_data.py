class TestData:
    def __init__(self):
        self.__properties = None
        self.__url = None
        self._data = {}

    def set_properties(self, properties):
        self.__properties = properties
        self.__url = self.__properties.get("base_url").__getattribute__("data")

    def get_property(self, key):
        return self.__properties.get(key).__getattribute__("data")


    def set(self, key, value):
        """Attach runtime data."""
        self._data[key] = value

    def get(self, key, default=None):
        """Retrieve runtime data."""
        return self._data.get(key, default)

    def clear(self):
        """Clear all attached data."""
        self._data.clear()

    
    @property
    def get_url(self):
        return self.__url
