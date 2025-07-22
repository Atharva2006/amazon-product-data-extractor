Amazon Product Scraper (Earbuds Only)

This is a Playwright + Python scraper built to extract product titles, prices, and ASINs from Amazon India (tested only on the noise cancellation earbuds search URL).

It uses stealth mode via `patchright` and exports the data to an Excel file, sorted by price.

Disclaimer
- For **educational/demo purposes** only.
- Built specifically for a single Amazon search page.
- Amazon’s structure may change and break the script.
- Amazon's website and data are owned by Amazon Inc. 
- Use responsibly and respect their terms of service.


Features
- Scrapes product `title`, `price`, and `ASIN`.
- Paginates through 10 result pages.
- Cleans and sorts data by price.
- Exports to Excel using `pandas`.

Tech Used
- `patchright`
- `playwright`
- `pandas`