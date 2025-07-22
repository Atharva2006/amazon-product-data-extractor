from patchright.sync_api import sync_playwright
import pandas as pd
import time

data = []

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir="C:\\playwright",
        channel="chrome",
        headless=False,
        no_viewport=True,
    )


    page = browser.new_page()
    page.goto('https://www.amazon.in/s?k=noise+cancellation+ear+bud')
    

    page_n = 1

    while page_n <= 10:
        print(f"\n Scraping page {page_n}")

        product_block = page.locator('div[role="listitem"][data-asin][data-index]')

        items_count = product_block.count()
        print(f" Found {items_count} titles")

        temp_data = []

        for i in range(product_block.count()):
            try:
                
                block = product_block.nth(i)

                asin_attr = block.get_attribute("data-asin")
                if not asin_attr or asin_attr.strip() == "":
                    continue

                title = block.locator("h2[aria-label] span").inner_text()
                title = title.split(",")[0]
                prices = block.locator("span.a-price-whole").inner_text()


                temp_data.append({
                    "ASIN": asin_attr,
                    "Title": title,
                    "Price": prices
                })
            except Exception as e:
                print(f"Error processing item {i}: {e}")
                continue

       
        data.extend(temp_data)
                
        next_button = page.locator('a.s-pagination-next[role="button"]')
        next_button.click()
        page.wait_for_selector('div[role="listitem"][data-asin][data-index]', timeout=15000)
        
        page_n += 1
        
    print("Scraping completed.")

    df = pd.DataFrame(data)
    df = df.drop_duplicates(subset='ASIN')
    df.to_excel("amazon_data.xlsx", index=False)

    df = pd.read_excel("amazon_data.xlsx")
    df["Price"] = df["Price"].str.replace(r"[^\d.]", "", regex=True)
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
    df = df.dropna(subset=["Price"])
    df = df.drop_duplicates(subset=['Title', 'Price'])

    df_sorted = df.sort_values(by="Price", ascending=True)
    df_sorted.to_excel("amazon_data.xlsx", index=False)

    print("Data saved to amazon_data.xlsx")

    browser.close()





    