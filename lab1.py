import cv2

img = cv2.imread(r"D:\ME\HAGA Market\LOGO\LOGO.jpg")

cv2.imshow('img',img)        
cv2.waitKey(1000)            
cv2.destroyAllWindows()

img_resize = cv2.resize(img,(1250,750))
cv2.imshow('img',img_resize)       
cv2.waitKey(1000)           
cv2.destroyAllWindows()   

cv2.imwrite('img_resized.png', img_resize)  
   
