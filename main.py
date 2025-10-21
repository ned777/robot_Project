from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Go to URL
        page.goto("https://example.com", timeout=60000)

        # Interact (click, type, etc.)
        page.click("text=Sign In")
        page.fill("input[name='username']", "myUsername")
        page.fill("input[name='password']", "myPassword")
        page.click("button[type='submit']")

        # Wait for something to confirm success
        page.wait_for_selector("text=Welcome", timeout=10000)

        print("✅ Success! Logged in successfully.")
        browser.close()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ An error occurred: {e}")

