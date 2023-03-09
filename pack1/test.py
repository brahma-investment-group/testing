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


def get_historic_stock_data(self):
    """
    :Parameters:
        period_type : str
            Valid periods_types: d, mo, y
            Either Use period parameters or use start and end
        period : str
            Valid periods: 1,5 (d), 1,3,6 (mo), 1,2,5,10 (y), ytd, max
            Either Use period parameters or use start and end
        frequency_type : str
            Valid frequency_type: m, h, d, wk, mo
            Intraday data cannot exceed last 60 days
        frequency : str
            Valid intervals: 1,2,5,15,30,60,90 (m),1 (h), 1,5 (d), 1 (wk), 1,3 (mo)
            Intraday data cannot exceed last 60 days
        start: str
            Download start date string (YYYY-MM-DD) or _datetime.
            Default is 1900-01-01
        end: str
            Download end date string (YYYY-MM-DD) or _datetime.
            Default is now
    """
    pass