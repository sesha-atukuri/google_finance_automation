import pytest
from pages.google_finance_homepage import GoogleFinancePage

@pytest.mark.usefixtures('setup')
class TestGoogleFinance:

    test_data = ["NFLX","MSFT","TSLA"]

    def test_page_title(self):
        finance_page = GoogleFinancePage(self.driver)
        title = "Google Finance - Stock Market Prices, Real-time Quotes & Business News"
        assert finance_page.get_page_title().__eq__(title)

    def test_retrieve_stock_symbols(self):
        finance_page = GoogleFinancePage(self.driver)
        symbols_list = finance_page.retrieve_stock_symbols()
        print("printing retrieved stock symbols from 'you maybe interested in- section'",symbols_list)
        assert len(symbols_list) == 6

    def test_print_stock_symbols_extra_in_retrieved(self):
        finance_page = GoogleFinancePage(self.driver)
        symbols_list = finance_page.retrieve_stock_symbols()
        print("Extra symbols present in retrieved list but not in Test data", list(set(symbols_list)-set(self.test_data)))

    def test_print_stock_symbols_missing_in_retrieve_list(self):
        finance_page = GoogleFinancePage(self.driver)
        symbols_list = finance_page.retrieve_stock_symbols()
        print("Missing symbols in retrieved list but present in Test data", list(set(self.test_data) - set(symbols_list)))
