from PIL import Image

def remove_white_bargin(file_name,output_name):
    image = Image.open(file_name)
    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]

            if r == 255 and g == 255 and b == 255:
                pixels[x, y] = (r, g, b, 0)

    image.save(output_name)

if __name__ == '__main__':

    im = Image.open("new_image.png")
    try:
        # 放大图片
        image = im.resize((50, 50))
        # 将新图像保存至桌面
        image.save("target2.png")
        print("查看新图像的尺寸", image.size)
    except IOError:
        print("放大图像失败")