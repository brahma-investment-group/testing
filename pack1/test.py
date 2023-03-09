def get_stock_contract(api_key: str, use_async: bool = False, connect_timeout: int = 10, read_timeout: int = 10,
                 pool_timeout: int = 10, max_connections: int = None, max_keepalive: int = None,
                 write_timeout: int = 10):
    
    """
    Initiates a Client to be used to access all REST Stocks endpoints.

    :param api_key: Your API Key. Visit your dashboard to get yours.
    :param use_async: Set it to ``True`` to get async client. Defaults to usual non-async client.
    :param connect_timeout: The connection timeout in seconds. Defaults to 10. basically the number of seconds to
                            wait for a connection to be established. Raises a ``ConnectTimeout`` if unable to
                            connect within specified time limit.                         
    """

    pass
