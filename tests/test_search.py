import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from playwright.sync_api import expect, Page

ST_CHARACTERS = [
    'prime lorca',
    'picard',
    'michael burnham',
    'spock',
    'christopher pike',
    'paul stamets',
    'seven of nine',
    'philippa georgiou',
    'cristóbal rios',
    'hugh culber'
]

@pytest.mark.parametrize('phrase', ST_CHARACTERS)
def test_basic_duckduckgo_search(
    phrase: str,
    page: Page,
    search_page: DuckDuckGoSearchPage,
    result_page: DuckDuckGoResultPage) -> None:

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for a phrase
    search_page.search(phrase)

    # Then the search result query is the phrase
    expect(result_page.search_input).to_have_value(phrase)

    # And the search result links pertain to the phrase
    assert result_page.result_link_titles_contain_phrase(phrase)

    # And the search result title contains the phrase
    expect(page).to_have_title(f'{phrase} at DuckDuckGo')

# run headed test with delay of 1 sec with:
# python -m pytest tests --headed --slowmo 1000

# if using page objects, then all interactions should be performed using page
# objects
# It is not recommended to mix raw Playwright calls (except expect assertions)
# with page object calls. That becomes confusing, and it encourages poor
# practices like dirty hacks and copypasta. It also causes a test automation
# project to lose strength from a lack of conformity in design.

# testing different browsers: use command line option --browser + chromium,
# firefox or webkit
# run tests against multiple browsers at the same time and list each test
# result with its browser:
# python -m pytest tests --browser chromium --browser firefox
# --browser webkit --verbose
# test against stock browsers on your machine trough browser channels:
# python -m pytest tests --browser-channel chrome
# python -m pytest tests --browser-channel msedge

# to test responsive layouts:
# python -m pytest tests --device "<device name>"
# full list of available devices:
# https://github.com/microsoft/playwright/blob/master/packages/playwright-core/src/server/deviceDescriptorsSource.json

# capture a screenshot at the end of every test (old ones will be deleted):
# python -m pytest tests --screenshot on
# to save a screenshot for every failing test only:
# python -m pytest tests --screenshot only-on-failure
# to save a video for every failing test:
# python -m pytest tests --video retain-on-failure

# to run tests in parallel (with pytest-xdist installed) add the -n option
# python -m pytest tests -n 2
# Typically, the optimal degree of concurrency is the number of processors or
# cores on your machine. Try running these tests in parallel at different
# degrees of concurrency (2, 3, 4, 5, higher?) to find the fastest completion
# time.

# Warning: DuckDuckGo may throttle your tests' requests if they happen too
# quickly. To work around this problem, try running with
# --headed or with --slowmo 100.)

# You can also test multiple browsers in parallel. For example, the
# following command will run the parameterized tests against all three
# Playwright browsers at 5x parallel:

# $ python3 -m pytest tests -n 5 --browser chromium --browser firefox
# --browser webkit
