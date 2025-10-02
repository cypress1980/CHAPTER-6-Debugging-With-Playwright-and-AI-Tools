import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://naveenautomationlabs.com/opencart/")
    expect(page.get_by_role("button", name="$ Currency  ")).to_be_visible()

    page.get_by_role("link", name=" My Account").click()
    page.get_by_role("link", name="Register").click()
    expect(page.get_by_role("group", name="Your Personal Details")).to_be_visible()

    page.get_by_role("textbox", name="* First Name").click()
    page.get_by_role("textbox", name="* First Name").fill("Harry")
    page.get_by_role("textbox", name="* First Name").press("Tab")
    page.get_by_role("textbox", name="* Last Name").fill("Potter")
    page.get_by_role("textbox", name="* Last Name").press("Tab")
    page.get_by_role("textbox", name="* E-Mail").fill("timsmith82882@yopmail.com")
    page.get_by_role("textbox", name="* E-Mail").press("Tab")
    page.get_by_role("textbox", name="* Telephone").fill("9999988888")
    page.get_by_role("textbox", name="* Telephone").press("Tab")
    page.get_by_role("textbox", name="* Password", exact=True).fill("Test@1234")
    page.get_by_role("textbox", name="* Password", exact=True).press("Tab")
    page.get_by_role("textbox", name="* Password Confirm").fill("Test@1234")
    page.get_by_role("checkbox").check()
    page.get_by_role("button", name="Continue").click()
    expect(page.locator("h1")).to_contain_text("Your Account Has Been Created!")