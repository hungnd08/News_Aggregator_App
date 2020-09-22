import time
from django.shortcuts import render, redirect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from news.models import Headline

def scrape(request):
    url = "https://www.thegioididong.com/dtdd"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(executable_path=r"C:/Users/Ambition 61/Downloads/chromedriver.exe", chrome_options=options)
    driver.get(url)
    time.sleep(3)
    while len(driver.find_elements_by_css_selector(".viewmore")) != 0:
        try:
            driver.find_elements_by_css_selector(".viewmore")[0].click()
        except:
            pass
        time.sleep(1)
    time.sleep(3)
    phones = driver.find_elements_by_css_selector(".item")
    for phone in phones:
        main = phone.find_elements_by_css_selector("a")[0]
        link = main.get_attribute("href")
        image = main.find_elements_by_css_selector("img")[0]
        if image.get_attribute("data-original") != None:
            image_src = str(image.get_attribute("data-original"))
        else:
            image_src = str(image.get_attribute("src"))
        title = main.find_elements_by_css_selector("h3")[0]
        price = main.find_elements_by_css_selector(".price")
        if price:
            price = price[0]
            original_price = price.find_elements_by_css_selector("span")
            promotional_price = price.find_elements_by_css_selector("strong")
            if len(original_price) != 0:
                original_price = original_price[0].text
            else:
                original_price = None
            if len(promotional_price) != 0:
                promotional_price = promotional_price[0].text
            else:
                promotional_price = None
        new_headline = Headline()
        new_headline.title = title.text
        new_headline.url = link
        new_headline.image = image_src
        new_headline.original_price = original_price
        new_headline.promotional_price = promotional_price
        new_headline.save()
    return redirect("../")

def news_list(request):
    headlines = Headline.objects.all()
    context = {
        "object_list": headlines,
    }
    return render(request, "news/home.html", context)
