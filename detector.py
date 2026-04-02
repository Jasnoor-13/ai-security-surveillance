import cv2
import time
from ultralytics import YOLO
import simpleaudio as sa

model = YOLO("yolov8n.pt")

alert_display_time = 0
person_detected_time = None
alert_triggered = False
last_alert_time = 0
sound_playing = False

def detect_objects(frame):
    global person_detected_time, last_alert_time, alert_display_time, sound_playing

    person_found = False
    alert_triggered = False

    results = model(frame, classes=[0])

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            if model.names[cls] == "person":
                person_found = True

    if person_found:
        if person_detected_time is None:
            person_detected_time = time.time()

        duration = time.time() - person_detected_time

        if duration > 5 and time.time() - last_alert_time > 5:
            alert_triggered = True
            last_alert_time = time.time()
            alert_display_time = time.time()

    else:
        person_detected_time = None

    annotated_frame = results[0].plot()

    if time.time() - alert_display_time < 3:
        alert_triggered = True

        if not sound_playing:
            wave_obj = sa.WaveObject.from_wave_file("alarm.wav")
            play_obj = wave_obj.play()
            sound_playing = True

        cv2.putText(
            annotated_frame,
            "ALERT: LOITERING DETECTED",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )
    else:
        sound_playing = False

    # ✅ THIS MUST BE INSIDE FUNCTION
    return annotated_frame, alert_triggered