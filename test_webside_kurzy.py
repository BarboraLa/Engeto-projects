import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()

def test_kurzy(page):
    page.goto("https://engeto.cz/prehled-kurzu/")
    assert  "Kurzy" in page.title()
    assert page.is_visible("text=kurzy")
