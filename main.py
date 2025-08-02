import cv2
import threading
from face_gaze_detector import FaceGazeDetector
from alert_system import play_alert_sound
from Snaplogger import save_snapshot
from atm_gui import ATMApp

def run_camera(atm_app):
    cap = cv2.VideoCapture(0)
    detector = FaceGazeDetector()

    previous_face_count = 1
    alert_active = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame, face_count, suspicious_gaze = detector.detect_faces_and_gaze(frame)

        # ✅ Show alert if second face appears
        if face_count > 1 and previous_face_count <= 1:
            print("[ALERT] Second face detected!")
            play_alert_sound()
            save_snapshot(frame)
            atm_app.show_warning()
            alert_active = True

        # ✅ Reset alert if back to one or zero faces
        if face_count <= 1:
            alert_active = False

        previous_face_count = face_count

        # 🧾 Overlay info
        cv2.putText(frame, f"Faces: {face_count}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Gaze: {'Suspicious' if suspicious_gaze else 'Normal'}", (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255) if suspicious_gaze else (0, 255, 0), 2)

        # 💡 Apply blur if suspicious
        if alert_active:
            overlay = frame.copy()
            cv2.rectangle(overlay, (0, 0), (frame.shape[1], frame.shape[0]), (0, 0, 0), -1)
            alpha = 0.6
            cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
            cv2.putText(frame, "⚠ SCREEN LOCKED", (40, 200),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

        cv2.imshow("ATM Camera", frame)
        key = cv2.waitKey(1)

        if key == ord('q'):
            break
        elif key == ord('r'):
            previous_face_count = 1
            alert_active = False
            atm_app.reset()

    cap.release()
    cv2.destroyAllWindows()

# --- Launch GUI and camera thread ---
atm_app = ATMApp()
camera_thread = threading.Thread(target=run_camera, args=(atm_app,))
camera_thread.daemon = True
camera_thread.start()

atm_app.root.mainloop()
