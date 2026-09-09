class login_page:
    def __init__(self):
        self.url="https://saucedemo.com"
        self.username="standard_user"
        self.password="secret_sauce"
        self.login_button="login_button"

    def visit_url(self):
        print("visiting login url", self.url)

    def enter_username(self):
        print("Entering username", self.username)

    def enter_password(self):
        print("Entering password ", self.password)

    def click_login(self):
        print("Clicking login button", self.login_button)


