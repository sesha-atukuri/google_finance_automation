from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleFinancePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    stock_section_xpath = '//*[@id="smart-watchlist-title"]'
    stock_symbols_list_xpath = '//ul[@class="sbnBtf"]/li//div[@class="COaKTb"]'

    def get_page_title(self):
        return self.driver.title

    def retrieve_stock_symbols(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.stock_section_xpath)))
        stock_symbols = [symbol.text for symbol in self.driver.find_elements(By.XPATH,self.stock_symbols_list_xpath)]
        return stock_symbols


