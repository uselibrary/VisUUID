import uuid
import binascii
from PIL import Image, ImageDraw
import random

UUID_list = []


# function: generate image with 32 pixels x 4 pixels
def generateUUID():
    uuid_data = uuid.uuid4()
    print("First Image: \n", uuid_data)
    # delete the hyphen
    uuid_data = str(uuid_data).replace('-', '')
    # for each character in the string, it is hex, convert it to binary and print it, and then for next character
    for i in uuid_data:
        # print result and save it to UUID list
        # print(bin(int(i, 16))[2:].zfill(4), end='')
        # print('\n')
        UUID_list.append(bin(int(i, 16))[2:].zfill(4))
    return UUID_list


def generateImageColor(UUID_list):
    print("Second Image: \n", UUID_list)

    # add sort number to the element in the list
    # example: 0000 is the first element, 0001 is the second element, 0010 is the third element, and so on
    # 0000 -> 0000 + 00000 -> 000000000
    # 0001 -> 0001 + 00001 -> 000100001
    # 0010 -> 0010 + 00010 -> 001000010

    for element in range(len(UUID_list)):
        UUID_list[element] = UUID_list[element] + bin(element)[2:].zfill(5)
    print("Second Image add sort number: \n", UUID_list)
    # re-arrange UUID_list as UUID_list_sort, from small to large, only sort the first 4 digits, not the last 5 digits
    UUID_list_sort = sorted(UUID_list, key=lambda x: x[:4])
    print("Second Image re-arrange : \n", UUID_list_sort)

    # create a new image with 32 pixels x 32 pixels, transparent background
    img = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
    # 32 columns, 9 rows, 1 pixel each;
    # fill each pixel with the corresponding value in the UUID list
    # for first 4 digital: if the value is 1, fill with black, if the value is 0, fill with white
    # for last 5 digital: if the value is 1, fill with red, if the value is 0, fill with blue
    for x in range(32):
        for y in range(4):
            if UUID_list_sort[x][y] == '1':
                img.putpixel((x, y), (0, 0, 0, 255))
            else:
                img.putpixel((x, y), (255, 255, 255, 255))
        for y in range(4, 9):
            if UUID_list_sort[x][y] == '1':
                img.putpixel((x, y), (255, 0, 0, 255))
            else:
                img.putpixel((x, y), (0, 0, 255, 255))
    # for other pixels, fill with random color
    for x in range(32):
        for y in range(9, 32):
            img.putpixel((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255))

    # save the image
    img.save('image/logo2.png')


# function: enlarge the image from 32x32 to 512x512 pixels
def enlargeImage():
    # open the image
    img = Image.open('image/logo2.png')
    # resize the image, one pixel to 16 pixels
    img = img.resize((512, 512), Image.NEAREST)
    # save the image

    img.save('image/logoEnlarge2.png')


# function: re-arrange the image pixels
def reArrangeImage():
    # open the image
    img = Image.open('image/logo2.png')
    # create a new image with 32 pixels x 32 pixels, transparent background
    img_new = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
    # the new image copy the 32x9 pixels from the old image
    for x in range(32):
        for y in range(9):
            img_new.putpixel((x, y), img.getpixel((x, y)))
    # the new image copy the 32x23 pixels from the old image, but re-arrange the pixels, sum the rgb value of each pixel, and then sort the pixels from small to large
    for x in range(32):
        # create a list to save the sum of rgb value of each pixel
        rgb_sum = []
        for y in range(9, 32):
            rgb_sum.append(img.getpixel((x, y))[0] + img.getpixel((x, y))[1] + img.getpixel((x, y))[2])
        # sort the list from small to large
        rgb_sum_sort = sorted(rgb_sum)
        print(rgb_sum_sort)
        # re-arrange the pixels in the new image, but using gray scale rather than rgb
        for y in range(9, 32):
            img_new.putpixel((x, y), (rgb_sum_sort[y - 9], rgb_sum_sort[y - 9], rgb_sum_sort[y - 9], 255))





    # save the image
    img_new.save('image/logoReArrange2.png')


if __name__ == '__main__':
    UUID = generateUUID()
    generateImageColor(UUID)
    enlargeImage()
    reArrangeImage()


