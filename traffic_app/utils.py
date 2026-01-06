import cv2
import os
from ultralytics import YOLO
from collections import Counter
from django.conf import settings

model = YOLO('yolov8n.pt') 

def detect_and_annotate(image_path, filename):
    img = cv2.imread(image_path)
    results = model(img)
    vehicle_counts = Counter()
    annotated_img = img.copy()

    for result in results:
        for box in result.boxes:
            conf = float(box.conf[0])
            if conf >= 0.5:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cls = int(box.cls[0])
                label = model.names[cls]
                vehicle_counts[label] += 1
                cv2.rectangle(annotated_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(annotated_img, f"{label} {conf:.2f}", (x1, y1-10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    output_name = f"output_{filename}"
    output_path = os.path.join(settings.MEDIA_ROOT, 'processed', output_name)
    cv2.imwrite(output_path, annotated_img)
    return output_name, vehicle_counts