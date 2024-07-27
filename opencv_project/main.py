import cv2
import numpy as np

image_path = "opencv_project/images/lena.jpg"
gray_image_path = "opencv_project/images/gray_lena.jpg"
image = cv2.imread(image_path)
gray_image = cv2.imread(gray_image_path)

print(f"Image shape: {image.shape}")

gray_image[100,100]  = [0,255,0]

if image is None:
    print(f"Image not found,plese check the path:{image_path}")
else:
    # cv2.namedWindow("Image", cv2.WINDOW_NORMAL) # Create a window with the name "Image"

    trans_gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # Convert the image to grayscale
    # cv2.imshow("Gray Image", trans_gray_image) # Display the grayscale image in the window

    trans_hsv_image = cv2.cvtColor(gray_image,cv2.COLOR_BGR2HSV) # Convert the image to HSV
    # cv2.imshow("HSV Image", trans_hsv_image) # Display the HSV image in the window

    resize_image = cv2.resize(gray_image,(300,300)) # Resize the image to 300x300 pixels
    cv2.imshow("Resized Image", resize_image) # Display the resized image in the window

    center = (gray_image.shape[1]//2, gray_image.shape[0]//2) # Get the center of the image
    rotation_matrix = cv2.getRotationMatrix2D(center, 180, 1.0) # Create a rotation matrix for 45 degrees
    rotated_image = cv2.warpAffine(gray_image, rotation_matrix, (gray_image.shape[1], gray_image.shape[0])) # Rotate the image
    cv2.imshow("Rotated Image", cv2.resize(rotated_image, (300,300))) # Display the rotated image in the window

    bulue_channel = image[:, :, 0]
    cv2.imshow("Blue Channel", bulue_channel) # Display the blue channel of the image in the window

    height, width = image.shape[:2]
    start_row, start_col = int(height * 0.25), int(width * 0.25)
    end_row, end_col = int(height * 0.75), int(width * 0.75)
    cropped_image = image[start_row:end_row, start_col:end_col] # Crop the image    

    cv2.imshow("Cropped Image", cropped_image) # Display the cropped image in the window

    cv2.waitKey(0) # Wait for a key press
    cv2.destroyAllWindows() # Close all windows