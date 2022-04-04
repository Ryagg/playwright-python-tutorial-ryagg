import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from playwright.sync_api import Page

# call the Playwright page fixture and use it to construct a page object
@pytest.fixture
def result_page(page: Page) -> DuckDuckGoResultPage:
    return DuckDuckGoResultPage(page)

@pytest.fixture
def search_page(page: Page) -> DuckDuckGoSearchPage:
    return DuckDuckGoSearchPage(page)
