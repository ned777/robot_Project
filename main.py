from playwright.sync_api import sync_playwright, TimeoutError
from urllib.parse import quote_plus

SEARCH_TERM = "kvm displayport"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=120)
        page = browser.new_page()
        try:
            url = f"https://www.ebay.com/sch/i.html?_nkw={quote_plus(SEARCH_TERM)}"
            print(f"Opening {url}")
            page.goto(url, wait_until="domcontentloaded", timeout=30000)

            page.mouse.wheel(0, 1500)

            page.wait_for_selector("div.su-card-container__content", timeout=20000)

            cards = page.query_selector_all("div.su-card-container__content a[href*='/itm/']")
            product = None

            for c in cards:
                txt = (c.get_attribute("aria-label") or c.inner_text() or "").strip()
                if not txt:
                    continue
                if "sponsored" in txt.lower() or "shop on ebay" in txt.lower():
                    continue
                product = txt
                break

            if product:
                print(f"Success! Found product: {product}")
            else:
                print("No valid product title found.")
        except TimeoutError as te:
            print(f"Timeout: {te}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    main()

