from dataclasses import dataclass


@dataclass
class MiddlewareInfo:
    # The IP or hostname of the middleware
    address: str
    # The middleware user's id
    user_id: str
    # The middleware user's password
    password: str

    def build_api_endpoint(self, path: str) -> str:
        """Builds an API endpoint on the middleware.

        Args:
            path (str): endpoint path
        Returns:
            _type_: complete URI to requested endpoint
        """

        return f"http://{self.address}/{path}"


@dataclass
class NetAppLocation:
    # The IP or hostname of the NetApp interface
    address: str
    # The port of the NetApp interface
    port: int

    def build_api_endpoint(self, path: str) -> str:
        """Builds an API endpoint on the NetApp interface.

        Args:
            path (str): endpoint path
        Returns:
            _type_: complete URI to requested endpoint
        """

        return f"http://{self.address}:{self.port}/{path}"