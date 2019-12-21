from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time
from credentials import USER


def mimic_typing(text_input, text, speed=0.01):
    """Mimics real user typing"""
    for char in text:
        text_input.send_keys(char)
        time.sleep(speed)


class Bot:
    username_login_xpath = '//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input'
    password_login_xpath = '//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input'
    submit_login_xpath = '//*[@id="page-container"]/div/div[1]/form/div[2]/button'
    tweet_text_xpath = '//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[' \
                       '1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div '
    tweet_button_xpath = '//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[' \
                         '1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span '

    def __init__(self):
        self.options = Options()
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', options=self.options)  # You'd have to
        # change the Chromedriver.exe path, according to your system.
        self.login()

    def login(self):
        """
            Logins to twitter using the given credentials.
        """
        self.driver.get('https://twitter.com/login')
        username_input = self.driver.find_element_by_xpath(self.username_login_xpath)
        password_input = self.driver.find_element_by_xpath(self.password_login_xpath)
        login_button = self.driver.find_element_by_xpath(self.submit_login_xpath)

        mimic_typing(username_input, USER['id'])
        mimic_typing(password_input, USER['pass'])

        login_button.click()

        if self.driver.current_url[-len(USER['id']):] == USER['id']:
            self.driver.quit()
            raise ValueError('Wrong Credentials.')

    def tweet(self, text):
        self.driver.get('https://twitter.com/compose/tweet')
        text_area = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, self.tweet_text_xpath)))
        tweet_button = self.driver.find_element_by_xpath(self.tweet_button_xpath)

        mimic_typing(text_area, text)
        tweet_button.click()
        print(self.driver.current_url)
        WebDriverWait(self.driver, 10).until(expected_conditions.url_matches('https://twitter.com/home'))
        print('Successfully Posted!')
        time.sleep(5)

    def exit(self):
        self.driver.quit()


def main():
    bot = Bot()
    bot.tweet('Hello!!!!!')
    bot.exit()


if __name__ == '__main__':
    main()
