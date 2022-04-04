from playwright.sync_api import Page

# Warning: Base URLs should typically be passed into automation code as an input, not hard-coded in a page object. We are doing this here as a matter of simplicity for this tutorial.
class DuckDuckGoSearchPage:
    URL = 'https://www.duckduckgo.com'

    # handle dependency injection for the browser automator
    def __init__(self, page: Page) -> None:
        # store argument page as an instance variable
        self.page = page
        # add locators for search page elements
        self.search_button = page.locator('#search_button_homepage')
        self.search_input = page.locator('#search_form_input_homepage')

    # load the DuckDuckGo search page
    def load(self) -> None:
        # the method uses the injected page as well as the URL variable
        self.page.goto(self.URL)

    # search for a phrase using the page objects and taking in the search phrase as an argument
    def search(self, phrase: str) -> None:
        self.search_input.fill(phrase)
        self.search_button.click()
