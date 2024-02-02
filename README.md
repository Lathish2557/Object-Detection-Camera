This project is a simple object detection camera that uses the YOLO (You Only Look Once) model to detect objects in real-time from a webcam feed. When a specific object (e.g., a bottle) is detected with a confidence level above a threshold, a Duo Push notification is triggered.

Dependencies
OpenCV: pip install opencv-python
NumPy: pip install numpy
Requests: pip install requests

Download the YOLO weights and configuration file, as well as the COCO labels file:

YOLO weights: yolov3.weights
YOLO configuration: yolov3.cfg
COCO labels: coco.names.txt
Place these files in the project directory.

Set up Duo Security:

Create a Duo account and obtain the integration key and secret key.
Replace 'YOUR_INTEGRATION_KEY' and 'YOUR_SECRET_KEY' in the code with your Duo credentials.
Run the code:

bash
Copy code
python object_detection_camera.py
Press 'q' to exit the camera feed.

Duo Push Notification
When a bottle is detected, a Duo Push notification is sent to the associated Duo account. Ensure that the Duo credentials are correctly set up in the code.
