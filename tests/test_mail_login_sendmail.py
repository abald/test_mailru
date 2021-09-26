from pages.page import MailLogin, MailSend


def test_mail_login(browser):
    mail_login_page = MailLogin(browser)
    mail_login_page.go_to_site()
    mail_login_page.enter_login("test.testov.85.85@mail.ru")
    mail_login_page.click_on_the_login_button()
    mail_login_page.enter_password("PasswordQAZwsx")
    mail_login_page.click_on_the_password_button()
    assert mail_login_page.check_mailbox() == "redirect mailbox checked out"


def test_send_mail(browser):
    inbox_page = MailSend(browser)
    inbox_page.click_the_new_mail_button()
    inbox_page.enter_to("baldinav@gmail.com")
    inbox_page.enter_subject("Отправка тестового письма")
    inbox_page.enter_bodymail("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
    inbox_page.click_send_button()



# test.testov.85.85@mail.ru
# PasswordQAZwsx
# PasswordQAZwsx