import cv2

cap = cv2.VideoCapture(1)  

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

cv2.namedWindow('Projet vision', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Projet vision', 520, 340)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame.")
        break
    
    cv2.imshow('Projet vision', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
