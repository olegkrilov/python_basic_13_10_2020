import json  # first import  built-in libs

import requests  # then pip modules


data = {
    'name': 'Vailiy',
    'surname': 'Pupkin',
    'age': 1321,
    'posts': ['a', 'b', 'c', 'f']
}

# SETS can not be serialized!!!
# ensure_ascii=False to code cyrrilyc symbols


# with open('test.json', 'w', encoding='utf-8') as json_file:
#     json_file.write(json.dumps(data))

with open('test.json', 'r', encoding='utf-8') as file:
    _str = json.loads(file.read())
    print(_str)


# then other shit


# url = 'https://geekbrains.ru/posts/bitva-umov-geekbrains-proverte-znaniya-i-poluchite-prizy'
# image_url = 'https://d2xzmw6cctk25h.cloudfront.net/geekbrains/public/ckeditor_assets/pictures/9898/retina-c02461738f9570b643224f572f9b15d7.png'

# Text
# response = requests.get(url)
# file = open('gb_blog.html', 'w', encoding='UTF-8')
#
# try:
#     file.write(response.text)
# except IOError as err:
#     print(err)
# finally:
#     file.close()

# IMAGE
# resp = requests.get(image_url)
# file = open('img.png', 'wb')
# try:
#     file.write(resp.content)
# except IOError as err:
#     print(err)
# finally:
#     file.close()
#
# if __name__ == '__main__':
#     print('les 5 draft')



# with open('text.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line)

with open('img.png', 'rb') as img:
    lines = img.read(100)
