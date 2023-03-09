async def get_stock_contract(self, symbol: str = '', exchange: str = 'SMART', currency: str = '', primaryExchange: str = ''):
        """
            Returns a stock contract.
            :param symbol: The symbol.
            :param exchange: Not used.
            :param currency: Not used.
            :param primaryExchange: Not used.
        """

        stock_contract = symbol
      
      
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
        period = self.period + self.
