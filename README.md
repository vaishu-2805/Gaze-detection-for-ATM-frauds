# 🛡️ ATM Shoulder-Surfing Detection System

This Python-based prototype detects **shoulder surfing attacks** at ATM machines using **real-time face detection, gaze analysis**, and **visual + audio alerts**. It also displays a warning pop-up when a second face is detected, helping protect user privacy during sensitive operations like PIN entry.

---

## 📸 Features Implemented

- ✅ Real-time webcam face detection using **MediaPipe**  
- ✅ Gaze direction analysis (suspicious vs normal)  
- ✅ Alert triggered when:
  - A **second face** appears in the camera view
- ✅ Pop-up **Tkinter ATM GUI**
- ✅ Audio alert using **Pygame**
- ✅ Screen blur + lock overlay when suspicious activity is detected
- ✅ Snapshot of the frame saved with timestamp
- 🔄 Alerts re-trigger when second person **re-enters**
- 🔘 Reset using `'r'` key

---

## 🛠️ Tech Stack

| Component             | Tool / Library                     |
|----------------------|-------------------------------------|
| Language             | Python 3.11.13                      |
| Face Detection       | MediaPipe / OpenCV                  |
| GUI Interface        | Tkinter                             |
| Audio Alerts         | Pygame                              |
| Snapshot Logging     | OpenCV                              |
| Gaze Detection       | Iris ratio (custom logic)           |
| Multithreading       | Python `threading` module           |

---

## 🖥️ Folder Structure

```
📁 shoulder-surfing/
├── main.py                   # App launcher (GUI + Camera)
├── camera_thread.py          # Camera processing and detection logic
├── atm_gui.py                # ATM PIN input GUI + warning pop-up
├── face_gaze_detector.py     # Face + gaze detection class
├── alert_system.py           # Audio alert system
├── Snaplogger.py             # Snapshot saving module
├── assets/
│   └── alert.wav             # Warning sound file
└── snapshots/                # Auto-saved screenshots
```

---

## 🚀 How to Run

1. ✅ **Install Python 3.11.13**  
   You can download it from the official site: [https://www.python.org/downloads/release/python-31113](https://www.python.org/downloads/release/python-31113)

2. ✅ **Set up a virtual environment** (optional but recommended):

```bash
python -m venv shoulder-surfing
```

3. ✅ **Activate the virtual environment**:

- On **Windows**:

```bash
shoulder-surfing\Scripts\activate
```

- On **Mac/Linux**:

```bash
source shoulder-surfing/bin/activate
```

4. ✅ **Install dependencies**:

```bash
pip install opencv-python pygame mediapipe
```

5. ✅ **Ensure your folder has**:

- `assets/alert.wav` (alert sound)
- Webcam access is enabled

6. ✅ **Run the app**:

```bash
python main.py
```

---

## 🧪 Demo Flow

1. The ATM GUI and camera feed window will open.
2. One person in the frame → **No alert**.
3. A second person appears → **Audio plays**, **screen blurs**, and **warning popup appears**.
4. If the second person leaves → system **resets silently**.
5. Second person re-enters → **alert triggers again**.