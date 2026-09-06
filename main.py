import cv2

print("AI-Based Smart Surveillance and Anomaly Detection System")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Unable to access camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Smart Surveillance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
