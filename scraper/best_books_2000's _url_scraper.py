from selenium.webdriver.common.by import By
from selenium import webdriver
from tqdm import tqdm
import pandas as pd
import time


if __name__ == "__main__":
    driver = webdriver.Chrome()
    base_url = "https://www.goodreads.com/list/show/5.Best_Books_of_the_Decade_2000s"
    book_urls = []
    
    for idx in tqdm(range(73)):

        page_no = idx + 1
        page_url = f"{base_url}?page={page_no}"
        driver.get(page_url)
        rows = driver.find_elements(By.TAG_NAME, 'tr')

        for row in rows:
            url_tag = row.find_element(By.CLASS_NAME, 'bookTitle')
            title = url_tag.text 
            book_url = url_tag.get_attribute('href')
            book_urls.append({
                "title": title,
                "url": book_url
            })
        
        time.sleep(1)
    
    df = pd.DataFrame(data=book_urls, columns=book_urls[0].keys())
    df.to_csv("best_books_2000's _urls.csv", index=False)
