
def test_button_kurzy(page):
    page.goto("https://engeto.cz/")
    page.locator("text='Chápu a přijímám!'").click()
    button=page.locator("text=PŘEHLED IT KURZŮ")
    assert button.is_visible(), "Tlačítko Přehled kurzů není viditelné"

    button.click()

    assert page.url == "https://engeto.cz/prehled-kurzu/", "Přesměrování neproběhlo"