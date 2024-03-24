import requests
from sel_tut import get_weather_data


# Get the weather data
temperature_, edited_address_, weather_icon_, weather_description_, image_url_, img_ = get_weather_data()

# # Convert image for Discord
# image_stream_ = BytesIO(img_)
# image_file_ = Image.open(image_stream_)
# image_file_.save("weather_icon.png")

webhook_url = 'https://discord.com/api/webhooks/1177670103752515584/DJd25scHB96dBa-2fgnEqwsbiKTsPGT6q2hnteuG0M87le79wvjD9cwdYHQo_2J2inPT'
data = {
    "avatar_url": "https://www.shutterstock.com/image-photo/mostly-sunny-weather-260nw-286242953.jpg",
    "embeds": [
        {
            "title": f"Current Weather of {edited_address_}",
            "thumbnail": {
                "url": image_url_
            }, 
            "fields": [
                {
                    "name": "Temperature",
                    "value": f"{temperature_} °F", 
                    "inline": True
                }, 
                {
                    "name": "Weather",
                    "value": weather_description_,
                    "inline": False
                }
            ]
        }        
    ]
}



r = requests.post(webhook_url, json=data)

print(r)