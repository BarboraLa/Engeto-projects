
def test_kurzy(page):
    page.goto("https://engeto.cz/prehled-kurzu/")
    assert  "Kurzy" in page.title()
    assert page.is_visible("text=kurzy")
