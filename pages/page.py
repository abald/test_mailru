from page.base import BasePage
from selenium.webdriver.common.by import By


class MailLoginLocators:
    LOCATOR_MAIL_LOGIN_FIELD = (By.NAME, "login")
    LOCATOR_MAIL_LOGIN_BUTTON = (By.CLASS_NAME, "button")
    LOCATOR_MAIL_PASSWORD_FIELD = (By.NAME, "password")
    LOCATOR_MAIL_PASSWORD_BUTTON = (By.CLASS_NAME, "second-button")
    LOCATOR_MAIL_BOX = (By.XPATH, '//*[@id="sideBarContent"]/div/nav')


class MailSendLocators:
    LOCATOR_NEW_MAIL_BUTTON = (By.CLASS_NAME, "compose-button")
    LOCATOR_NEW_MAIL_TO_FIELD = (By.CLASS_NAME, "container--H9L5q")
    LOCATOR_NEW_MAIL_SUBJECT_FIELD = (By.NAME, "Subject")
    LOCATOR_NEW_MAIL_BODY_FIELD = (By.XPATH, "/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[5]/div/div/div[2]/div[1]/div[1]") # //div[@class='editable-ry1s cke_editable cke_editable_inline cke_contents_true cke_show_borders']/div[1]
    LOCATOR_NEW_MAIL_SEND_BUTTON =(By.XPATH, "//span[text()='Отправить']")


class MailLogin(BasePage):
    def enter_login(self, word):
        login_field = self.find_element(MailLoginLocators.LOCATOR_MAIL_LOGIN_FIELD)
        login_field.click()
        login_field.send_keys(word)
        return login_field

    def click_on_the_login_button(self):
        return self.find_element(MailLoginLocators.LOCATOR_MAIL_LOGIN_BUTTON,time=10).click()

    def enter_password(self, word):
        password_field = self.find_password_element(MailLoginLocators.LOCATOR_MAIL_PASSWORD_FIELD)
        password_field.click()
        password_field.clear()
        password_field.send_keys(word)
        return password_field

    def click_on_the_password_button(self):
        return self.find_element(MailLoginLocators.LOCATOR_MAIL_PASSWORD_BUTTON ,time=10).click()

    def check_mailbox(self):
        check_inbox_page = self.find_element(MailLoginLocators.LOCATOR_MAIL_BOX, time=20)
        if check_inbox_page:
            check = "redirect mailbox checked out"
        else:
            check = "Its not mailbox"
        return check


class MailSend(BasePage):
    def click_the_new_mail_button(self):
        return self.find_element(MailSendLocators.LOCATOR_NEW_MAIL_BUTTON,time=10).click()

    def enter_to(self,word):
        to_field = self.find_element(MailSendLocators.LOCATOR_NEW_MAIL_TO_FIELD)
        to_field.click()
        to_field.send_keys(word)
        return to_field

    def enter_subject(self,word):
        subject_field = self.find_element(MailSendLocators.LOCATOR_NEW_MAIL_SUBJECT_FIELD,time=60)
        subject_field.click()
        subject_field.send_keys(word)
        return subject_field

    def enter_bodymail(self,word):
        bodymail_field = self.find_element(MailSendLocators.LOCATOR_NEW_MAIL_BODY_FIELD)
        bodymail_field.click()
        bodymail_field.send_keys(word)
        return bodymail_field

    def click_send_button(self):
        return self.find_element(MailSendLocators.LOCATOR_NEW_MAIL_SEND_BUTTON,time=30).click()



