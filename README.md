Hi 👋, I'm atharva,
 A passionate webscraping beginner


I’m currently working on amazon web scraper
I’m currently learning camoufox and js
How to reach : narkhedeatharva200637@gmail.com

Amazon Product Scraper 

This is a Playwright + Python scraper built to extract product titles, prices, and ASINs from amazon.in and amazon.com.

It uses stealth mode via `patchright` and exports the data to an Excel file, sorted by price.


How It Works:

       Launch Browser:
       - The script uses Playwright to launch a Chromium browser with persistent context (saves login, cookies, etc.).

       User Input:
       - You’re prompted to enter a valid Amazon search URL (either .in or .com).

       Scraping Loop:

       - It scrapes product titles and prices from the first 2 pages of the search results:
       - Locates each product block.
       - Extracts the product title and price.
       - Skips items without proper ASIN or missing data.

       Pagination:
       - After scraping a page, it clicks the "Next" button and waits for the next page to load.

       Excel Output:

       - Saves the scraped data to an Excel file.
       - Cleans and converts price to numeric.
       - Removes duplicates and sorts products by price (ascending).
       - Overwrites the file with the cleaned, sorted data.

Disclaimer
- For **educational/demo purposes** only.
- Built specifically for a single Amazon search page.
- Amazon’s structure may change and break the script.
- Amazon's website and data are owned by Amazon Inc. 
- Use responsibly and respect their terms of service.


Features
- Scrapes product `title` and `price`.
- Paginates through 10 result pages.
- Cleans and sorts data by price.
- Exports to Excel using `pandas`.

Tech Used
- `patchright`
- `playwright`
- `pandas`
