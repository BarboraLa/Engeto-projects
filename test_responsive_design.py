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

def test_responsive_design(page):
    devices=[
        {
            "width": 1920, "height": 1080 #počítač
            }, 
        {
            "width": 768, "height": 1024 #tablet
         }, 
        {
            "width": 375, "height": 667 #mobil
         }
        ]
    for device in devices: 
        page.set_viewport_size(device)
        page.goto("https://engeto.cz/")

        assert page.is_visible("text=Kurzy programování"), "Obsah není viditelný pro dané zařízení"