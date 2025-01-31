import pytest

@pytest.mark.parametrize("device", [
    {"width": 1920, "height": 1080},  # Počítač
    {"width": 768, "height": 1024},  # Tablet
    {"width": 375, "height": 667},   # Mobil
])
def test_responsive_design(page, device):
    page.set_viewport_size(device)
    page.goto("https://engeto.cz/")

    assert page.is_visible("text=Kurzy programování"), f"Obsah není viditelný pro zařízení s rozměry: {device}"