import cv2
import numpy as np

def get_color_name(R, G, B):

    if R > 200 and G > 200 and B > 200:
        return "White"
    elif R < 50 and G < 50 and B < 50:
        return "Black"
    elif R > G and R > B:
        return "Red"
    elif G > R and G > B:
        return "Green"
    elif B > R and B > G:
        return "Blue"
    elif R > 150 and G > 150 and B < 100:
        return "Yellow"
    elif R > 150 and B > 150 and G < 100:
        return "Purple"
    elif G > 150 and B > 150 and R < 100:
        return "Cyan"
    else:
        return "Custom Color"
    
cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    cap = cv2.VideoCapture(1, cv2.CAP_AVFOUNDATION)

print("Press 'q' on the video window to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera feed not available!")
        break

    height, width, _ = frame.shape
    
    cx = int(width / 2)
    cy = int(height / 2)

    pixel_center = frame[cy, cx]
    b, g, r = int(pixel_center[0]), int(pixel_center[1]), int(pixel_center[2])

    color_name = get_color_name(r, g, b)

    cv2.circle(frame, (cx, cy), 6, (255, 255, 255), 2)

    cv2.rectangle(frame, (20, 20), (520, 70), (b, g, r), -1)
    text = f"Color: {color_name} | RGB: ({r}, {g}, {b})"
    
    text_color = (0, 0, 0) if (r * 0.299 + g * 0.587 + b * 0.114) > 186 else (255, 255, 255)
    cv2.putText(frame, text, (30, 52), cv2.FONT_HERSHEY_SIMPLEX, 0.7, text_color, 2)

    cv2.imshow("Real-Time Colour Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()