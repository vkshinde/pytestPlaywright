class BaseAPI:
    def __init__(self, api_context, base_url):
        """
        Initialize the BaseAPI with a Playwright API context and base URL.
        Args:
            api_context: Playwright APIRequestContext.
            base_url (str): The base URL for the API.
        """
        self.api_context = api_context
        self.base_url = base_url
        self.default_headers = {
            "Content-Type": "application/json"
        }

    def set_headers(self, headers):
        """
        Set or update request headers.
        Args:
            headers (dict): Key-value pairs for the headers.
        """
        self.default_headers.update(headers)

    def get(self, endpoint, params=None):
        """
        Perform a GET request.
        Args:
            endpoint (str): API endpoint.
            params (dict): Query parameters.
        Returns:
            Response object.
        """
        response = self.api_context.get(
            url=f"{self.base_url}{endpoint}",
            headers=self.default_headers,
            params=params
        )
        return response

    def post(self, endpoint, data=None, json=None):
        """
        Perform a POST request.
        Args:
            endpoint (str): API endpoint.
            data (dict): Form-encoded data.
            json (dict): JSON-encoded data.
        Returns:
            Response object.
        """
        response = self.api_context.post(
            url=f"{self.base_url}{endpoint}",
            headers=self.default_headers,
            data=data,
            json=json
        )
        return response

    def put(self, endpoint, data=None, json=None):
        """
        Perform a PUT request.
        Args:
            endpoint (str): API endpoint.
            data (dict): Form-encoded data.
            json (dict): JSON-encoded data.
        Returns:
            Response object.
        """
        response = self.api_context.put(
            url=f"{self.base_url}{endpoint}",
            headers=self.default_headers,
            data=data,
            json=json
        )
        return response

    def delete(self, endpoint):
        """
        Perform a DELETE request.
        Args:
            endpoint (str): API endpoint.
        Returns:
            Response object.
        """
        response = self.api_context.delete(
            url=f"{self.base_url}{endpoint}",
            headers=self.default_headers
        )
        return response
