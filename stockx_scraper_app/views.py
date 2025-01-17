# Django Project Setup

# Main Python Script in Django App
# stockx_scraper_app/views.py

from django.http import JsonResponse
import requests
from multiprocessing import Pool

# Function to scrape StockX URLs
def scrape_stockx(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return {"url": url, "status": "success", "code": response.status_code}
    except requests.exceptions.RequestException as e:
        return {"url": url, "status": "failed", "error": str(e)}

# Django view for triggering scraping
def scrape_view(request):
    stockx_urls = [
        "https://stockx.com/sneaker1",
        "https://stockx.com/sneaker2",
        "https://stockx.com/sneaker3",
        "https://stockx.com/sneaker4",
    ]

    with Pool(processes=len(stockx_urls)) as pool:
        results = pool.map(scrape_stockx, stockx_urls)

    return JsonResponse({"results": results})
