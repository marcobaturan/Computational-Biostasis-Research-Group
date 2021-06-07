from random import randint
from PIL import Image, ImageDraw

""" Generates images with random damage. Returns N damaged images and corresponding masks.

Currently implemented types of damage: 
- holes
- cracks
"""

MAX_ELLIPSES = 10
MAX_CRACKS = 7
CRACK_WIDTH_FACTOR = 70 # the bigger, the lower will be the max width of cracks
ELLIPSE_SIZE_FACTOR = 10 # the bigger, the smaller will be the biggest holes

input_image = Image.open("input.png")
# MyImage.show()

input_size = input_image.size  # returns a tuple
print(input_size)

background_color = (255, 255, 255)  # white
damage_color = (0, 0, 0)  # black
# MyImage = Image.new('RGB', (600, 400), WHITE)


def draw_random_crack(draw_obj, size):

    sections_num = randint(3, 10)
    crack_width = randint(1, round(size[0]/CRACK_WIDTH_FACTOR))

    max_step_diff = round(min(size[0] / 5, size[1] / 5))

    top_left_x = randint(0, size[0])
    top_left_y = randint(0, size[1])


    for j in range(sections_num):
        diff_x = randint(-max_step_diff, max_step_diff)
        diff_y = randint(-max_step_diff, max_step_diff)

        end_x = top_left_x + diff_x
        end_y = top_left_y + diff_y

        draw_obj.line([top_left_x, top_left_y, end_x, end_y], width=crack_width, fill=0)

        top_left_x = end_x
        top_left_y = end_y


def draw_random_ellipse(draw_obj, size):
    top_left_x = randint(0, size[0])
    top_left_y = randint(0, size[1])

    max_dimension = round(min(size[0], size[1]) / ELLIPSE_SIZE_FACTOR)

    height = randint(0, max_dimension)
    width = randint(0, max_dimension)

    ellipse_box = [top_left_x, top_left_y, top_left_x + width, top_left_y + height]

    draw_obj.ellipse(ellipse_box, width=1, fill=0)


def generate_mask(size):
    alpha_mask = Image.new("L", size, 255)

    draw_obj = ImageDraw.Draw(alpha_mask)

    ellipses_num = randint(1, MAX_ELLIPSES)
    cracks_num = randint(1, MAX_CRACKS)

    for i in range(cracks_num):
        draw_random_crack(draw_obj, size)

    for i in range(ellipses_num):
        draw_random_ellipse(draw_obj, size)

    full_mask = alpha_mask.copy()
    full_mask.convert("RGB")

    return alpha_mask, full_mask


def generate_damaged_image(intact_image, alpha_mask):

    cropped_image = intact_image.copy()
    cropped_image.putalpha(alpha_mask)

    damaged_image = Image.new("RGB", intact_image.size, damage_color)
    damaged_image.paste(cropped_image, (0, 0), cropped_image)

    return damaged_image


for n in range(5):
    alpha_mask, full_mask = generate_mask(input_size)
    damaged_image = generate_damaged_image(input_image, alpha_mask)
    full_mask.save("{}output_mask.png".format(n))
    damaged_image.save("{}output_damaged.png".format(n))

# damaged_image.show()
# full_mask.show()
