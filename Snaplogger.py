import cv2
import time
import os

def save_snapshot(frame):
    os.makedirs("snapshots", exist_ok=True)
    filename = f"snapshots/snapshot_{int(time.time())}.jpg"
    cv2.imwrite(filename, frame)
    print(f"[INFO] Snapshot saved: {filename}")
