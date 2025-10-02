import re
from playwright.sync_api import Page, expect,sync_playwright

def test_Login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://testing.qaautomationlabs.com/iframe.php")
        expect(page.get_by_role("heading")).to_contain_text("IFrame Demo")
        expect(page.locator("section")).to_contain_text("IFrame")
        expect(page.locator("iframe[name=\"iframe1\"]").content_frame.get_by_role("heading", name="I am iFrame")).to_be_visible()

        page.locator("iframe[name=\"iframe1\"]").content_frame.get_by_role("button", name="CLick Me").click()
        expect(page.locator("#message")).to_contain_text("You have clicked on iframe 1 button")
        expect(page.locator("iframe[name=\"iframe2\"]").content_frame.get_by_role("heading", name="I am IFrame")).to_be_visible()

        page.locator("iframe[name=\"iframe2\"]").content_frame.get_by_role("button", name="Click Me").click()
        expect(page.locator("#message")).to_contain_text("You have clicked on iframe 2 button")
