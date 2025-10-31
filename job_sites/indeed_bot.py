from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from time import sleep
from utils.logger import get_logger

logger = get_logger("IndeedBot")

class IndeedBot:
    def __init__(self, email, password, resume_path, keywords, location):
        self.email = email
        self.password = password
        self.resume_path = resume_path
        self.keywords = keywords
        self.location = location

        self.driver = uc.Chrome()

    def login(self):
        logger.info("logging Indeed...")
        self.driver.get("https://secure.indeed.com/account/login")
        sleep(2)
        self.driver.find_element(By.NAME, "__email").send_keys(self.email)
        # self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        input("Press Enter after completing CAPTCHA...")

    def search_jobs(self):
        logger.info(f"search position：{self.keywords} - {self.location}")
        self.driver.get("https://www.indeed.com")
        sleep(3)
        what = self.driver.find_element(By.ID, "text-input-what")
        where = self.driver.find_element(By.ID, "text-input-where")

        what.clear(); what.send_keys(self.keywords)
        where.clear(); where.send_keys(self.location)
        where.send_keys(Keys.RETURN)
        sleep(4)

    def apply_jobs(self):
        logger.info("auto applying to jobs...")
        jobs = self.driver.find_elements(By.CLASS_NAME, "result")

        for i, job in enumerate(jobs[:5]):
            try:
                job.click()
                sleep(2)
                apply_btn = self.driver.find_element(By.CSS_SELECTOR, "button.ia-IndeedApplyButton")
                apply_btn.click()
                sleep(2)
                upload = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
                upload.send_keys(self.resume_path)
                logger.info(f"successfully apply {i+1} positions")
                sleep(3)
            except Exception as e:
                logger.warning(f"apply failed: {e}")

    def run(self):
        self.login()
        self.search_jobs()
        self.apply_jobs()
        self.driver.quit()
