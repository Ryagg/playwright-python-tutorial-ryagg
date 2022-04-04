from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from playwright.sync_api import expect, Page

# fixtures are declared as arguments
def test_basic_duckduckgo_search(
    page: Page,
    search_page: DuckDuckGoSearchPage,
    result_page: DuckDuckGoResultPage) -> None:

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

# if using page objects, then all interactions should be performed using page
# objects
# It is not recommended to mix raw Playwright calls (except expect assertions)
# with page object calls. That becomes confusing, and it encourages poor
# practices like dirty hacks and copypasta. It also causes a test automation
# project to lose strength from a lack of conformity in design.
