from fixtures.conftest import setup  # Import setup fixture

def test_valid_login(setup):
    driver = setup
    driver.get("https://google.com/")
    assert driver.title == "Google", "Failed: wrong title"
