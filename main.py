import cv2
from fastapi import FastAPI
from fastapi.responses import StreamingResponse, HTMLResponse
from detector import detect_objects

app = FastAPI()

# global state
alert_count = 0
current_status = "SAFE"
last_alert_display_time = 0

# open webcam
camera = cv2.VideoCapture(0)

def generate_frames():
    global alert_count, current_status, last_alert_display_time

    while True:
        success, frame = camera.read()

        if not success:
            break

        try:
            # run AI detection
            frame, alert_triggered = detect_objects(frame)

            if alert_triggered:
                last_alert_display_time = time.time()
                alert_count += 1

            if time.time() - last_alert_display_time < 3:
                current_status = "ALERT"
            else:
                current_status = "SAFE"

        except Exception as e:
            print("ERROR IN DETECTION:", e)
            current_status = "ERROR"

        # ALWAYS show frame (even if error happens)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.get("/video")
def video_feed():
    return StreamingResponse(
        generate_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )


# 🆕 DASHBOARD UI
@app.get("/")
def home():
    return HTMLResponse(f"""
    <html>
        <head>
            <title>AI Surveillance Dashboard</title>
        </head>
        <body style="text-align:center; font-family:Arial;">
            <h1>🚨 AI Surveillance Dashboard</h1>

            <h2>Status: <span style="color:{'red' if current_status=='ALERT' else 'green'};">
                {current_status}
            </span></h2>

            <h3>Total Alerts: {alert_count}</h3>

            <img src="/video" width="720" />
        </body>
    </html>
    """)