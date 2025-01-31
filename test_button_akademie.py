
def test_button_akademie(page):
    page.goto("https://engeto.cz/prehled-kurzu/")
    page.locator("text='Chápu a přijímám!'").click()
    button = page.locator("a.block-button.size-xl.type-primary:has-text('Akademie')")
    assert button.is_visible(), "Tlačítko Přehled kurzů není viditelné"

    button.click()

    assert page.url == "https://engeto.cz/prehled-kurzu/#akademie", "Přesměrování neproběhlo"