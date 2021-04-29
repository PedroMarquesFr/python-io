import requests
from parsel import Selector


def save_image_in_file(image_list):
    for image in image_list:
        filename = image.split("/")[-1]
        image_content = requests.get(image).content
        with open(filename, "wb") as file:
            file.write(image_content)


def get_images_by_url(url):
    response = requests.get(url)
    selector = Selector(text=response.text)
    image_list = selector.css("img::attr(src)").getall()
    formated_image_list = []
    for image in image_list:
        print(image)
        if image.startswith("//"):
            formated_image_list.append(image[len("//"):])
    save_image_in_file(formated_image_list)


get_images_by_url(
    "https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags"
)
