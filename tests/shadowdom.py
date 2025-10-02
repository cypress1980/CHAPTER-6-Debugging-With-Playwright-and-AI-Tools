import re
from playwright.sync_api import Page, expect,sync_playwright

def test_Login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.lambdatest.com/selenium-playground/shadow-dom")
        expect(page.locator("h1")).to_contain_text("Shadow DOM")
        page.locator("input[name=\"username\"]").click()
        page.locator("input[name=\"username\"]").fill("Kailash")
        page.locator("shadow-signup-form input[name=\"email\"]").click()
        page.locator("shadow-signup-form input[name=\"email\"]").fill("jiyhahha@yopmail.com")
        page.locator("input[name=\"password\"]").click()
        page.locator("input[name=\"password\"]").fill("Test@1234")
        page.locator("input[name=\"confirm_password\"]").click()
        page.locator("input[name=\"confirm_password\"]").fill("Test@1234")
        page.get_by_role("button", name="Submit").click()
        page.wait_for_timeout(3000)