from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from playwright.sync_api import expect, Page

# give test access to a fresh page in a new browser context
def test_basic_duckduckgo_search(page: Page) -> None:
    search_page = DuckDuckGoSearchPage(page)
    result_page = DuckDuckGoResultPage(page)

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for a phrase
    search_page.search('prime lorca')

    # Then the search result query is the phrase
    expect(result_page.search_input).to_have_value('prime lorca')

    # And the search result links pertain to the phrase
    assert result_page.result_link_titles_contain_phrase('prime lorca')

    # And the search result title contains the phrase
    expect(page).to_have_title('prime lorca at DuckDuckGo')

# run headed test with delay of 1 sec with 'python -m pytest tests --headed
# --slowmo 1000

# supported selectors:
# Text, CSS, XPath, N-th element, React, Vue, ID attributes
# Try to stick to text, IDs, or CSS selectors

# expect connects page locator calls to Playwright's assertions
# the expect function performs implicit waiting for the element to satisfy the
# to_have_value condition
# assert 'prime lorca' == page.input_value('#search_form_input') would wait for
# the element to appear, but not for the input value to become 'prime lorca'

# the selector .result__title a.result__a can be used to identify all result
# links on a page

# explicit waiting is necessary to safely mitigate potential race conditions

# locator is a method that returns a Locator object for the target element. A Locator object can make many of the same calls as a page, like clicking and getting text. However, it can also make calls for explicit waiting and calls that target multiple elements.
# .result__title a.result__a is the selector for the result links.
# nth(4) is an N-th element fetcher. N-th element fetchers are zero-indexed and may be appended to any selector. In this call, it will fetch the fifth result link element.
# wait_for is a method that will wait for the target element to be visible.
