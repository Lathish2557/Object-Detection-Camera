import cv2
import numpy as np
import requests

# Load YOLO model and COCO labels
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getUnconnectedOutLayersNames()

# Load COCO labels
with open("coco.names.txt", "r") as f:
    classes = [line.strip() for line in f.readlines()]

CONFIDENCE_THRESHOLD = 0.5

# Function to send a Duo Push notification
def send_duo_push_notification():
    integration_key = 'YOUR_INTEGRATION_KEY'
    secret_key = 'YOUR_SECRET_KEY'
    api_hostname = 'api-XXXXXXXX.duosecurity.com'

    # Prepare the request parameters
    payload = {
        'username': 'XXXXXXX',  # Replace with the username associated with the Duo account
        'pushinfo': 'Bottle detected!',
        'type': 'Push',
    }

    # Make the Duo Push API call
    response = requests.post(
        f'https://{api_hostname}/auth/v2/auth',
        auth=(integration_key, secret_key),
        data=payload
    )

    if response.status_code == 200:
        print('Duo Push notification sent successfully!')
    else:
        print('Failed to send Duo Push notification.')

# Initialize video capture from laptop camera
cap = cv2.VideoCapture(0)  # Use 0 for default camera

while True:
    ret, frame = cap.read()
    if not ret:
        break
    height, width = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(layer_names)

    # Process the outs to get bounding boxes, confidences, and class ids
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > CONFIDENCE_THRESHOLD:
                if class_id == 37:  # Assuming class ID 37 corresponds to a bottle
                    # Bottle detected! Send a Duo Push notification
                    send_duo_push_notification()

    # Display the results on the frame
    cv2.imshow("Object Detection", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
