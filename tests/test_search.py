from playwright.sync_api import Page

# give test access to a fresh page in a new browser context
def test_basic_duckduckgo_search(page: Page) -> None:
    # Given the DuckDuckGo home page is displayed
    page.goto('https://www.duckduckgo.com', wait_until='networkidle')
    # When the user searches for a phrase
    page.locator('#search_form_input_homepage').fill('prime lorca')
    page.locator('#search_button_homepage').click()
    # Then the search result query is the phrase
    # And the search result links pertain to the phrase
    # And the search result title contains the phrase
    pass

# run headed test with delay of 1 sec with 'python -m pytest tests --headed
# --slowmo 1000

# supported selectors:
# Text, CSS, XPath, N-th element, React, Vue, ID attributes
# Try to stick to text, IDs, or CSS selectors
