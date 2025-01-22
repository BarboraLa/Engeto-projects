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

def test_button_kurzy(page):
    page.goto("https://engeto.cz/")
    if page.is_visible("text=Přijmout všechny cookies"):
        page.locator("text=/chápu a přijímám!/i").click()
    button=page.locator("text=PŘEHLED IT KURZŮ")
    assert button.is_visible(), "Tlačítko Přehled kurzů není viditelné"

    button.click()

    assert page.url == "https://engeto.cz/prehled-kurzu/", "Přesměrování neproběhlo"