from playwright.sync_api import Page
from typing import List

class DuckDuckGoResultPage:
    # add dependency injection with locators
    def __init__(self, page: Page) -> None:
        self.page = page
        self.result_links = page.locator('.result__title a.result__a')
        self.search_input = page.locator('#search_form_input')

    # add method to get all result link titles as a list
    def result_link_titles(self) -> List[str]:
        # wait for at least 5 elements to appear
        self.result_links.nth(4).wait_for()
        # get all the text contents for the found elements
        return self.result_links.all_text_contents()

    # add method to check if the list of result link titles contain a phrase
    def result_link_titles_contain_phrase(
        self, phrase: str, minimum: int = 1) -> bool:
        # call above method to get the list of titles
        titles = self.result_link_titles()
        # filter titles using list comprehension
        matches = [t for t in titles if phrase.lower() in t.lower()]
        # return a Boolean value  indicating if the number of matches
        # meets the minimum threshold
        return len(matches) >= minimum

# Assertions should not be done in page objects!
# Assertions should only be done in test cases
