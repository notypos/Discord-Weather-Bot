import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_weather_data(location):
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.get(f"https://www.google.com/search?q=weather+{location}")
    time.sleep(1.3)

    # Finding temperature and address
    temperature_ = driver.find_element(By.ID, "wob_tm").text

    address_ = driver.find_element(By.CLASS_NAME, "eKPi4").text

    # Editing address
    edited_address_ = address_.replace("Results for", "").strip()

    # Getting weather icon
    weather_icon_ = driver.find_element(By.ID, "wob_tci")
    img_ = weather_icon_.screenshot_as_png

    # Getting weather description
    weather_description_ = weather_icon_.get_attribute("alt")

    weather_images_ = {
        "Showers": "https://img.freepik.com/premium-vector/button-icon-weather-mobile-app-website-rainy-forecast-element-3d-cloud-raindrops_313242-1413.jpg?w=740",
        "Mostly cloudy": "https://images.pling.com/img/00/00/59/73/18/1645413/cg.png",
        "Mostly sunny": "https://is1-ssl.mzstatic.com/image/thumb/Purple128/v4/7c/20/da/7c20da43-7845-6a43-4a34-8f4a7272bff1/AppIcon-1x_U007emarketing-0-0-GLES2_U002c0-512MB-P3-0-0-0-85-220-0-0-0-9.png/217x0w.webp",
        "Cloudy": "https://www.iconbunny.com/icons/media/catalog/product/cache/2/thumbnail/600x/1b89f2fc96fc819c2a7e15c7e545e8a9/4/8/484.13-partly-cloudy-i-icon-iconbunny.jpg",
        "Sunny": "https://cdn-icons-png.flaticon.com/512/3222/3222691.png",
        "Rain and snow": "https://cdn1.iconfinder.com/data/icons/weather-forecast-meteorology-color-1/128/weather-sleet-512.png",
        "Rain": "https://cdn3.iconfinder.com/data/icons/weather-ios-11-1/50/Heavy_Rain_Night_Rain_Raindrops_Apple_iOS_Flat_Weather-512.png",
        "Scattered showers": "https://www.shutterstock.com/image-vector/rain-sun-color-icon-sunny-260nw-1998923258.jpg",
        "Partly sunny": "https://is1-ssl.mzstatic.com/image/thumb/Purple128/v4/7c/20/da/7c20da43-7845-6a43-4a34-8f4a7272bff1/AppIcon-1x_U007emarketing-0-0-GLES2_U002c0-512MB-P3-0-0-0-85-220-0-0-0-9.png/217x0w.webp",
        "Partly cloudy": "https://is1-ssl.mzstatic.com/image/thumb/Purple128/v4/7c/20/da/7c20da43-7845-6a43-4a34-8f4a7272bff1/AppIcon-1x_U007emarketing-0-0-GLES2_U002c0-512MB-P3-0-0-0-85-220-0-0-0-9.png/217x0w.webp",
        "Clear with periodic clouds": "https://is1-ssl.mzstatic.com/image/thumb/Purple128/v4/7c/20/da/7c20da43-7845-6a43-4a34-8f4a7272bff1/AppIcon-1x_U007emarketing-0-0-GLES2_U002c0-512MB-P3-0-0-0-85-220-0-0-0-9.png/217x0w.webp"
    }

    # image URL is the value of the weather description key in the weather_images dictionary which is the 'alt' of Google icon
    image_url_ = weather_images_.get(weather_description_, "https://i.fbcd.co/products/resized/resized-750-500/0170461584d942d1ac67b1318c845234d5a1617f7727670bcf7b142b90f4e97a.jpg")
    #print("The temperature is", temperature_, "degrees, in", edited_address_, "and it looks like", weather_description_)

    #image_stream_ = BytesIO(img_)
    #image_file_ = Image.open(image_stream_)

    # Display the image
    #image_file_.show()

    driver.quit()

    return temperature_, edited_address_, weather_icon_, weather_description_, image_url_, img_
