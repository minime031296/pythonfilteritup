#project apply filter on image gaussianblur and edge
import pyscreenshot
import cv2

image_path =(r"C:\\Users\\Admin\Desktop\robby.jpg") #user can give any path this is to just explain how to take the image path 

try:
    image = cv2.imread(image_path)
    edges = cv2.Canny(image,100,200)
    if image is None:
        print("Failed to load the image. Please double-check the file path.")
    else:
        blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

        cv2.imshow("Original image", image)
        cv2.imshow("Blurred image", blurred_image)
        cv2.imshow("Edges",edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        screenshot = pyscreenshot.grab()
        screenshot.save("screenshot.png")
        print("Screenshot saved successfully!")
except cv2.error as e:
    print(f"An error occurred: {e}")