import re
from playwright.sync_api import Page, expect,sync_playwright

def test_Login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.lambdatest.com/selenium-playground/iframe-demo/")
        expect(page.get_by_role("heading")).to_contain_text("Simple iframe")
        expect(page.locator("div").filter(has_text=re.compile(r"^Simple iFrame containing Editor$")).locator("iframe").content_frame.get_by_role("button", name="𝐁")).to_be_visible()

        page.locator("div").filter(has_text=re.compile(r"^Simple iFrame containing Editor$")).locator("iframe").content_frame.get_by_text("Your content.").click()
        page.locator("div").filter(has_text=re.compile(r"^Simple iFrame containing Editor$")).locator("iframe").content_frame.get_by_text("Your content.").fill("Your content.Kailash How are you")
        page.wait_for_timeout(3000)
