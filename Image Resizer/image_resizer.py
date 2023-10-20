# Program to resize an image

''' This program resizes the dimesnions of the photo.
If the original photo is 2048*1024 then in this case the dimensions will be reduced by 50% which results to 1024*512
and the image will be saved to the location provided below '''

import cv2

# Taking the image as an input
# This will return a tuple containing information about the image's dimensions
''' cv2.IMREAD_UNCHANGED ensures that the image is read exactly as it is present in the directory
without any modification, it preserves the original format of the image '''

image_input = cv2.imread("football.jpg",cv2.IMREAD_UNCHANGED)



# Showing the image
# cv2.imshow("title", image_input)


# Percentage by which the image is to be resized
resize_percent = 50


# Calculate the 50 percent of original dimension
''' Here, image_input.shape[1] refers to the width of the input image
and image_input.shape[0] refers to the height of the input image
because the variable 'image_input' contains information about image dimesnions as a tuple so we need to access it using index '''
# In general, the shape of an image is represented as a tuple in the form (height, width, channels) or (rows, columns, channels)

new_width = int(image_input.shape[1] * resize_percent/100)
new_height = int(image_input.shape[0] * resize_percent/100)



# Storing the values for new size (as a tuple)
new_size = (new_width, new_height)


# Resizing the image
output = cv2.resize(image_input, new_size)


# Storing the new resized image in our directory
cv2.imwrite("C:\\Users\\charc\\Desktop\\Python\\Mini Projects 2\\Image Resizer\\resized_image.jpg", output)


cv2.waitKey(0)