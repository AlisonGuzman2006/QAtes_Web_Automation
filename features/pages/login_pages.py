class HomePage:
    def __init__(self, browser):
        self.browser = browser

    def get_title(self):
        return self.browser.title
