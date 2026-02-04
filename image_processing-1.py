import cv2

# Step 1: Read the image
image = cv2.imread("input.jpg")

# Check if image loaded correctly
if image is None:
    print("Error: Image not found!")
    exit()

# Step 2: Display original image
cv2.imshow("Original Image", image)

# Step 3: Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 4: Display grayscale image
cv2.imshow("Gray Scale Image", gray_image)

# Step 5: Save the grayscale image
cv2.imwrite("grayscale_output.jpg", gray_image)

print("Grayscale image saved successfully!")

# Wait until any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
