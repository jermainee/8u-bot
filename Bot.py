from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from seleniumrequests import Firefox
import requests
import time


class Bot:
    def __init__(
        self,
        username,
        password,
        game_name,
        minutes,
        history_length,
        initial_bet_amount,
        loss_multiplicator,
        low_threshold,
        low_bet_type,
        high_threshold,
        high_bet_type,
        max_bets
    ):
        self.game_name = game_name
        self.minutes = minutes
        self.history_length = history_length
        self.initial_bet_amount = initial_bet_amount
        self.loss_multiplicator = loss_multiplicator
        self.low_threshold = low_threshold
        self.low_bet_type = low_bet_type
        self.high_threshold = high_threshold
        self.high_bet_type = high_bet_type
        self.max_bets = max_bets

        self.start_time = 0

        webdriver = Firefox()
        webdriver.get("https://8u.com/#/login")
        webdriver.find_element(by=By.NAME, value="user").send_keys(username)
        webdriver.find_element(by=By.CSS_SELECTOR, value="input[type='password']").send_keys(password)
        webdriver.find_element(by=By.CSS_SELECTOR, value="button[type='button']").click()
        self.webdriver = webdriver

    def execute(self):
        while True:
            self.start_time = time.time()

            current_score = self.calculate_score()
            print("[score]", current_score)

            if current_score >= self.high_threshold:
                current_bet_type = self.high_bet_type
            elif current_score <= self.low_threshold:
                current_bet_type = self.low_bet_type
            else:
                self.wait_for_next_round()
                continue

            while not self.recursive_betting(current_bet_type, self.initial_bet_amount, self.max_bets):
                print("[result] loss")

            self.wait_for_next_round()

    def calculate_score(self):
        response = self.webdriver.request('POST', 'https://8u.com/api/game/gameDraw/history',
                                          data={"gameName": self.game_name, "pageNo": "1",
                                                "pageSize": self.history_length}).json()

        draw_results = response['data']['list']
        small_draws = ["0", "1", "2", "3", "4", "5", "6", "7"]
        score = 0

        for draw_result in draw_results:
            if draw_result['drawResult'] in small_draws:
                score -= 1
            else:
                score += 1

        return score

    def has_won(self):
        self.webdriver.get("https://8u.com/#/gameCenter?gameName=" + self.game_name)

        time.sleep(3)

        WebDriverWait(self.webdriver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//html/body/div[2]/div[1]/div[3]/div[3]/div[1]/span[2]"))).click()

        win_all_amount_element = WebDriverWait(self.webdriver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//html/body/div[2]/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/span")))

        win_all_amount = win_all_amount_element.text

        if win_all_amount == 'No Result':
            return self.has_won()

        return win_all_amount != '0.00 USDT'

    def bet(self, bet_type, bet_amount):
        print("[bet]", bet_type, bet_amount)
        self.webdriver.get("https://8u.com/#/gameCenter?gameName=" + self.game_name)

        time.sleep(3)

        if bet_type == "small":
            WebDriverWait(self.webdriver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Small')]"))).click()

        elif bet_type == "big":
            WebDriverWait(self.webdriver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Big')]"))).click()

        else:
            print("invalid bet type")
            return

        WebDriverWait(self.webdriver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Amount of per bet']"))).send_keys(bet_amount)

        WebDriverWait(self.webdriver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Bet Now')]"))).click()

        time.sleep(1)

        WebDriverWait(self.webdriver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//html/body/div[7]/div[2]/div/div/div[3]/div/button[2]/span"))
        ).click()

    def recursive_betting(self, bet_type, bet_amount, bets_left):
        if (bets_left == 0):
            print("[exit] maximum bets")
            return True
        else:
            bets_left -= 1

        if self.start_time == 0:
            self.start_time = time.time()

        self.bet(bet_type, bet_amount)
        self.wait_for_next_round()

        if self.has_won():
            print("[result] won")
            return True
        else:
            self.recursive_betting(bet_type, bet_amount * self.loss_multiplicator, bets_left)

    def wait_for_next_round(self):
        end_time = time.time()
        time_elapsed = (end_time - self.start_time)
        waiting_seconds = ((self.minutes * 60) - time_elapsed)

        print("[duration]", round(time_elapsed / 60, 2), "minutes")
        print("[waiting] waiting",  round(waiting_seconds / 60, 2), "minutes for next game")

        self.start_time = 0

        if waiting_seconds <= 0:
            return

        time.sleep(waiting_seconds)
