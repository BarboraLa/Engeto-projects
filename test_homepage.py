
def test_engeto_homepage(page):
    page.goto("https://www.engeto.cz")
    assert  "Kurzy programování" in page.title()
    assert page.is_visible("text=Engeto")
    assert page.is_visible("text=Kurzy")
    assert page.is_visible(".logo-link")

    tiles = page.locator("nav")
    assert tiles.count() > 0, "Dlaždice nebyly nalezeny na homepage."

    chatbot = page.locator("#intercom-frame")
    page.locator("text='Chápu a přijímám!'").click()
    chatbot.wait_for(state="visible", timeout=15000)
    assert chatbot.is_visible(), "Chatbot není zobrazen na homepage."

    success_story_block = page.locator(".block-success-story") 
    success_story_block.wait_for(state="visible", timeout=10000)  
    assert success_story_block.is_visible(), "Úspěšné příběhy nejsou zobrazeny na homepage."
