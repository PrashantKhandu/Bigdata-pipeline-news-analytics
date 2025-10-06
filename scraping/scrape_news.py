from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import traceback

def scrape():
    print("News scraping started...")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        print("crawling aajtak.in website", flush=True)
        driver.get("https://www.aajtak.in/")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2 a, h3 a")))

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        headlines = soup.select("h2 a, h3 a")

        for h in headlines:
            text = h.get_text(strip=True)
            link = h.get("href")
            if text and link:
                print(f"{text} — {link}", flush=True)
        return True
    except Exception as e:
        print(e, flush=True)
        print(traceback.format_exc(), flush=True)
    finally:
        driver.quit()
        print("driver quited", flush=True)

if __name__ == "__main__":
    status = scrape()
    if status:
        print("Program executed successfully")
    else:
        print("Something strange error")
