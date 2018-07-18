from PIL import Image



WIDTH = 80

HEIGHT = 80

IMG = '/home/python/Desktop/static/images/006.jpg'

ascii_char = list("$@B.%8&WM#*oahkbdpqwmO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i    !1I;:,\"^' ")


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '

    length = len(ascii_char)

    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    print(gray)

    unit = (256.0 + 1) / length

    return ascii_char[int(gray / unit)]


if __name__ == '__main__':

    im = Image.open(IMG)

    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ''

    for i in range(HEIGHT):

        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
            # print(im.getpixel((j,i)))

        txt += '\n'

    print(txt)
    with open('/home/python/Desktop/123.txt','w') as f:
        f.write(txt)

