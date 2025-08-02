import cv2
from face_gaze_detector import FaceGazeDetector
from alert_system import play_alert_sound
from Snaplogger import save_snapshot

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

        # Display face and gaze info
        cv2.putText(frame, f"Faces: {face_count}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Gaze: {'Suspicious' if suspicious_gaze else 'Normal'}", (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                    (0, 0, 255) if suspicious_gaze else (0, 255, 0), 2)

        # Trigger alert when face count jumps from <=1 to >1
        if face_count > 1 and previous_face_count <= 1:
            print("[ALERT] Second person detected!")
            play_alert_sound()
            save_snapshot(frame)
            atm_app.show_warning()
            alert_active = True

        # Reset if faces drop to 1 or 0
        if face_count <= 1:
            alert_active = False

        previous_face_count = face_count

        # Blur overlay when alert is active
        if alert_active:
            overlay = frame.copy()
            cv2.rectangle(overlay, (0, 0), (frame.shape[1], frame.shape[0]), (0, 0, 0), -1)
            frame = cv2.addWeighted(overlay, 0.5, frame, 0.5, 0)
            cv2.putText(frame, "??? SCREEN LOCKED", (50, 200),
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
