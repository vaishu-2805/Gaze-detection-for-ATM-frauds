import cv2
import mediapipe as mp

class FaceGazeDetector:
    def __init__(self):
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=3,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.LEFT_IRIS = [474, 475, 476, 477]
        self.RIGHT_IRIS = [469, 470, 471, 472]
        self.LEFT_EYE = [33, 133]
        self.RIGHT_EYE = [362, 263]

    def detect_faces_and_gaze(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb)
        face_count = 0
        suspicious_gaze = False

        if results.multi_face_landmarks:
            face_count = len(results.multi_face_landmarks)

            if face_count == 1:
                landmarks = results.multi_face_landmarks[0]
                h, w, _ = frame.shape

                # LEFT eye
                lx, rx = int(landmarks.landmark[self.LEFT_EYE[0]].x * w), int(landmarks.landmark[self.LEFT_EYE[1]].x * w)
                lcx = int(landmarks.landmark[self.LEFT_IRIS[0]].x * w)
                left_ratio = (lcx - lx) / (rx - lx) if (rx - lx) != 0 else 0.5

                # RIGHT eye
                lx2, rx2 = int(landmarks.landmark[self.RIGHT_EYE[0]].x * w), int(landmarks.landmark[self.RIGHT_EYE[1]].x * w)
                rcx = int(landmarks.landmark[self.RIGHT_IRIS[0]].x * w)
                right_ratio = (rcx - lx2) / (rx2 - lx2) if (rx2 - lx2) != 0 else 0.5

                # Average the two
                iris_ratio = (left_ratio + right_ratio) / 2.0

                print(f"[DEBUG] Left: {left_ratio:.2f}, Right: {right_ratio:.2f}, Avg: {iris_ratio:.2f}")

                if iris_ratio < 0.25 or iris_ratio > 0.75:
                    suspicious_gaze = True


                print(f"[DEBUG] Iris ratio: {iris_ratio:.2f}")

                if iris_ratio < 0.25 or iris_ratio > 0.75:
                    suspicious_gaze = True

        return frame, face_count, suspicious_gaze
