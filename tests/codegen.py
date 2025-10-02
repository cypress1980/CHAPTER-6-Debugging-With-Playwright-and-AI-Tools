import re
from playwright.sync_api import Playwright, sync_playwright, expect

def test_Login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://shop.qaautomationlabs.com/index.php")
        page.get_by_role("textbox", name="Email").click()
        page.get_by_role("textbox", name="Email").fill("demo@demo.com")
        page.get_by_role("textbox", name="Password").click()
        page.get_by_role("textbox", name="Password").fill("demo")
        page.get_by_role("button", name="Login").click()
        expect(page.locator("#navbarCollapse")).to_contain_text("Home")

        # ---------------------
        context.close()
        browser.close()