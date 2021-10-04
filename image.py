import os

from PIL import Image, ImageDraw, ImageFont
import numpy
import base64
from io import BytesIO
from pathlib import \
    Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f


# image (PNG, JPG) to base64 conversion (string), learn about base64 on wikipedia https://en.wikipedia.org/wiki/Base64
def image_base64(img, img_type):
    with BytesIO() as buffer:
        img.save(buffer, img_type)
        return base64.b64encode(buffer.getvalue()).decode()


# formatter preps base64 string for inclusion, ie <img src=[this return value] ... />
def image_formatter(img, img_type):
    return "data:image/" + img_type + ";base64," + image_base64(img, img_type)


# color_data prepares a series of images for data analysis
def image_data(path=Path.cwd() / Path("static/assets/"), img_list=None):
    # def image_data(path=os.path.join("static", "assets"), img_list=None):
    # def image_data(path=Path("static/assets/"), img_list=None):  # path of static images is defaulted

    # img = Image.open(path / 'lassen-volcano-256.jpg')
    # img = Image.open('C:/Users/prish/IdeaProjects/flask_portfolio2/static/assets/lassen-volcano-256.jpg')
    # d1 = ImageDraw.Draw(img)
    # d1.text((0, 0), "Sample text Prisha")
    # img.show()
    # img.save(path / 'lassen-volcano-256.jpg')

    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            {'source': "Peter Carolin", 'label': "Lassen Volcano", 'file': "lassen-volcano-256.jpg"},
            {'source': "iconsdb.com", 'label': "Black square", 'file': "black-square-16.png"},
            {'source': "iconsdb.com", 'label': "Red square", 'file': "red-square-16.png"},
            {'source': "iconsdb.com", 'label': "Green square", 'file': "green-square-16.png"},
            {'source': "iconsdb.com", 'label': "Blue square", 'file': "blue-square-16.jpg"},
            {'source': "iconsdb.com", 'label': "White square", 'file': "white-square-16.png"},
        ]
    # gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        # File to open
        file = path / img_dict['file']  # file with path for local access (backend)
        # file =os.path.join(path, img_dict['file'])  # file with path for local access (backend)
        # Python Image Library
        print(file)
        img_reference = Image.open(file)
        # imgPath = 'C:/Users/prish/IdeaProjects/flask_portfolio2/static/assets/'
        # imgFullPath = imgPath + img_dict['file']
        # img = Image.open(imgFullPath)
        d1 = ImageDraw.Draw(img_reference)
        hori_flippedImage = img_reference.transpose(Image.FLIP_LEFT_RIGHT)
        img_reference.save(file)
        hori_flippedImage.save(file)

        if img_dict['file'] == "white-square-16.png":
            d1.text((0, 0), "Hi!", fill=(255, 0, 0))
        elif img_dict['file'] == "lassen-volcano-256.jpg":
            d1.text((0, 0), "TechFish is the best fish!")
        else:
            d1.text((0, 0), "Hi!")
        # img_reference.show()
        img_reference.save(file)
        # img.show()

        # img_reference = Image.open(r"C:\Users\awsum\IdeaProjects\flask_portfolio2\static\assets\lassen-volcano-256.jpg")  # PIL
        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size
        # Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])
        # Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
        # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
        img_dict['gray_data'] = []
        for pixel in img_dict['data']:
            average = (int(pixel[0]) + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
    return img_list  # list is returned with all the attributes for each image dictionary


# color_data prepares a series of images for data analysis
def prisha_image_data(path=Path.cwd() / Path("static/prishaassets/"), img_list=None):
    # def image_data(path=os.path.join("static", "assets"), img_list=None):
    # def image_data(path=Path("static/assets/"), img_list=None):  # path of static images is defaulted

    # img = Image.open(path / 'lassen-volcano-256.jpg')
    # img = Image.open('C:/Users/prish/IdeaProjects/flask_portfolio2/static/assets/lassen-volcano-256.jpg')
    # d1 = ImageDraw.Draw(img)
    # d1.text((0, 0), "Sample text Prisha")
    # img.show()
    # img.save(path / 'lassen-volcano-256.jpg')

    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            {'source': "Google", 'label': "NoelleGenshinImpact", 'file': "Noelle.jpg"},
            {'source': "Google", 'label': "YanfeiGenshinImpact", 'file': "Yanfei.jpg"},
            {'source': "Google", 'label': "LisaGenshinImpact", 'file': "Lisa.jpg"},
            {'source': "Google", 'label': "ZhongliGenshinImpact", 'file': "Zhongli.jpg"},
        ]

    # gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        # File to open
        file = path / img_dict['file']  # file with path for local access (backend)
        # file =os.path.join(path, img_dict['file'])  # file with path for local access (backend)
        # Python Image Library
        print(file)
        print("testing1212")
        img_reference = Image.open(file)
        # imgPath = 'C:/Users/prish/IdeaProjects/flask_portfolio2/static/assets/'
        # imgFullPath = imgPath + img_dict['file']
        # img = Image.open(imgFullPath)
        hori_flippedImage = img_reference.transpose(Image.FLIP_TOP_BOTTOM)
        img_reference.save(file)
        hori_flippedImage.save(file)

        d1 = ImageDraw.Draw(img_reference)
        if img_dict['file'] == "Noelle.png":
            d1.text((0, 0), "As a dutiful maid would!", fill=(255, 0, 0))
        elif img_dict['file'] == "Yanfei.png":
            d1.text((0, 0), "Time for your arraignment!", )
        elif img_dict['file'] == "Lisa.png":
            d1.text((0, 0), "Blitz!", )
        else:
            d1.text((3, 10), "This is my Genshin team", fill=(255, 255, 255))
        # img_reference.show()
        img_reference.save(file)
        #img_reference.show()

        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size
        # Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])
        # Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
        # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
        img_dict['gray_data'] = []
        for pixel in img_dict['data']:
            average = (int(pixel[0]) + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
    return img_list  # list is returned with all the attributes for each image dictionary


# color_data prepares a series of images for data analysis
def arushi_image_data(path=Path.cwd() / Path("static/arushiassets/"), img_list=None):
    # def image_data(path=os.path.join("static", "assets"), img_list=None):
    # def image_data(path=Path("static/assets/"), img_list=None):  # path of static images is defaulted

    # img = Image.open(path / 'lassen-volcano-256.jpg')
    # img = Image.open('C:/Users/prish/IdeaProjects/flask_portfolio2/static/assets/lassen-volcano-256.jpg')
    # d1 = ImageDraw.Draw(img)
    # d1.text((0, 0), "Sample text Prisha")
    # img.show()
    # img.save(path / 'lassen-volcano-256.jpg')

    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            {'source': "My Camera", 'label': "Bisky", 'file': "Dog.jpg"},
        ]

    # gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        # File to open
        file = path / img_dict['file']  # file with path for local access (backend)
        # file =os.path.join(path, img_dict['file'])  # file with path for local access (backend)
        # Python Image Library
        print(file)
        print("testing1212")
        img_reference = Image.open(file)
        # imgPath = 'C:/Users/prish/IdeaProjects/flask_portfolio2/static/assets/'
        # imgFullPath = imgPath + img_dict['file']
        # img = Image.open(imgFullPath)
        hori_flippedImage = img_reference.transpose(Image.FLIP_TOP_BOTTOM)
        img_reference.save(file)
        hori_flippedImage.save(file)
        font = ImageFont.truetype("arial.ttf", 300)
        d1 = ImageDraw.Draw(img_reference)
        d1.text((3, 10), "This is my favorite dog", fill=(255, 0, 0), font=font)
        # img_reference.show()
        #img_reference.save(file)
        img_reference.show()

        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size
        # Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])
        # Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
        # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
        img_dict['gray_data'] = []
        for pixel in img_dict['data']:
            average = (int(pixel[0]) + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
    return img_list  # list is returned with all the attributes for each image dictionary


# color_data prepares a series of images for data analysis
def vaishavi_image_data(path=Path.cwd() / Path("static/vaishaviassets/"), img_list=None):
    # def image_data(path=os.path.join("static", "assets"), img_list=None):
    # def image_data(path=Path("static/assets/"), img_list=None):  # path of static images is defaulted

    # img = Image.open(path / 'lassen-volcano-256.jpg')
    # img = Image.open('C:/Users/prish/IdeaProjects/flask_portfolio2/static/assets/lassen-volcano-256.jpg')
    # d1 = ImageDraw.Draw(img)
    # d1.text((0, 0), "Sample text Prisha")
    # img.show()
    # img.save(path / 'lassen-volcano-256.jpg')

    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            {'source': "My Camera", 'label': "Bisky", 'file': "Download.jpg"},
        ]

    # gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        # File to open
        file = path / img_dict['file']  # file with path for local access (backend)
        # file =os.path.join(path, img_dict['file'])  # file with path for local access (backend)
        # Python Image Library
        print(file)
        print("testing1212")
        img_reference = Image.open(file)
        # imgPath = 'C:/Users/prish/IdeaProjects/flask_portfolio2/static/assets/'
        # imgFullPath = imgPath + img_dict['file']
        # img = Image.open(imgFullPath)
        hori_flippedImage = img_reference.transpose(Image.FLIP_TOP_BOTTOM)
        img_reference.save(file)
        hori_flippedImage.save(file)
        font = ImageFont.truetype("arial.ttf", 300)
        d1 = ImageDraw.Draw(img_reference)
        d1.text((3, 10), "This is my favorite dog", fill=(255, 0, 0), font=font)
        # img_reference.show()
        #img_reference.save(file)
        img_reference.show()

        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size
        # Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])
        # Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
        # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
        img_dict['gray_data'] = []
        for pixel in img_dict['data']:
            average = (int(pixel[0]) + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
    return img_list  # list is returned with all the attributes for each image dictionary


# color_data prepares a series of images for data analysis
def siya_image_data(path=Path.cwd() / Path("static/siyaassets/"), img_list=None):
    # def image_data(path=os.path.join("static", "assets"), img_list=None):
    # def image_data(path=Path("static/assets/"), img_list=None):  # path of static images is defaulted

    # img = Image.open(path / 'lassen-volcano-256.jpg')
    # img = Image.open('C:/Users/prish/IdeaProjects/flask_portfolio2/static/assets/lassen-volcano-256.jpg')
    # d1 = ImageDraw.Draw(img)
    # d1.text((0, 0), "Sample text Prisha")
    # img.show()
    # img.save(path / 'lassen-volcano-256.jpg')

    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            #{'source': "My Camera", 'label': "Bisky", 'file': "Download.jpg"},
        ]

    # gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        # File to open
        file = path / img_dict['file']  # file with path for local access (backend)
        # file =os.path.join(path, img_dict['file'])  # file with path for local access (backend)
        # Python Image Library
        print(file)
        print("testing1212")
        img_reference = Image.open(file)
        # imgPath = 'C:/Users/prish/IdeaProjects/flask_portfolio2/static/assets/'
        # imgFullPath = imgPath + img_dict['file']
        # img = Image.open(imgFullPath)
        hori_flippedImage = img_reference.transpose(Image.FLIP_TOP_BOTTOM)
        img_reference.save(file)
        hori_flippedImage.save(file)
        font = ImageFont.truetype("arial.ttf", 300)
        d1 = ImageDraw.Draw(img_reference)
        d1.text((3, 10), "This is my favorite dog", fill=(255, 0, 0), font=font)
        # img_reference.show()
        #img_reference.save(file)
        img_reference.show()

        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size
        # Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])
        # Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
        # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
        img_dict['gray_data'] = []
        for pixel in img_dict['data']:
            average = (int(pixel[0]) + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
    return img_list  # list is returned with all the attributes for each image dictionary


# run this as standalone tester to see data printed in terminal
if __name__ == "__main__":
    local_path = Path("static/assets/")
    img_test = [
        {'source': "Peter Carolin", 'label': "Lassen Volcano", 'file': "lassen-volcano-256.jpg"},
    ]
    items = image_data(local_path, img_test)  # path of local run
    for row in items:
        # print some details about the image so you can validate that it looks like it is working
        # meta data
        print("---- meta data -----")
        print(row['label'])
        print(row['format'])
        print(row['mode'])
        print(row['size'])
        # data
        print("----  data  -----")
        print(row['data'])
        print("----  gray data  -----")
        print(row['gray_data'])
        print("----  hex of data  -----")
        print(row['hex_array'])
        print("----  bin of data  -----")
        print(row['binary_array'])
        # base65
        print("----  base64  -----")
        print(row['base64'])
        # display image
        print("----  render and write in image  -----")
        filename = local_path / row['file']
        image_ref = Image.open(filename)
        draw = ImageDraw.Draw(image_ref)
        draw.text((0, 0), "Size is {0} X {1}".format(*row['size']))  # draw in image
        image_ref.show()
print()
