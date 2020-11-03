import cv2

# Read Image
# IMREAD_GRAYSCALE - FLAG TO GREY
# MORE FLAGS = https://preventionyun.tistory.com/25
img = cv2.imread('../images/test.png', cv2.)

# Display image on window
cv2.imshow('Test Image', img)
cv2.waitKey(0)
# Turn off window
cv2.destroyAllWindows()

# Create another test image file
cv2.imwrite('outputTest.jpg', img)