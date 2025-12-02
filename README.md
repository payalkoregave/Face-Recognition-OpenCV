# Face Recognition System using OpenCV & LBPH

This project is a **Face Recognition System** built using **Python**, **OpenCV**, and the **LBPH (Local Binary Patterns Histogram)** algorithm.
It can detect faces using Haarcascade and recognize trained individuals from the dataset.

---

## 🚀 Features

* Real-time face detection using Haarcascade
* Face recognition using LBPH algorithm
* Supports multiple users (add unlimited people)
* Automatically detects unknown faces
* Saves unknown face images
* Fully customizable dataset folder

---

## 📁 Project Structure

```
Face-Recognition-Project
│── opencv.py
│── haarcascade_frontalface_default.xml
│── README.md
└── dataset/
      ├── user1/
      ├── user2/
      └── user3/
```

Inside each user folder, add 20–50 clear face images.

Example:

```
dataset/payal/   → payal1.jpg, payal2.jpg, …
dataset/aarati/  → aarati1.jpg, aarati2.jpg, …
dataset/akanksha/ → akanksha1.jpg, ak1.jpg, ak2.jpg …
```

---

## 🛠 Requirements

Install the necessary Python packages:

```bash
pip install opencv-python
pip install opencv-contrib-python
pip install numpy
```

Make sure `haarcascade_frontalface_default.xml` is in the same folder as `opencv.py`.

---

## ▶️ How to Run the Project

### **Step 1 — Prepare Dataset**

1. Create a folder called `dataset/`
2. Inside it, create one folder for each person:

   ```
   dataset/payal/
   dataset/aarati/
   dataset/akanksha/
   ```
3. Add **face images** (20–50 images recommended) in each folder.

⚠️ Images must be **clear**, **frontal** photos.

---

### **Step 2 — Run Training + Recognition Script**

Open terminal / command prompt inside the project folder:

```bash
python opencv.py
```

The script will:

✔ Read all dataset images
✔ Train LBPH recognizer
✔ Start webcam
✔ Detect and recognize faces

---

## 🧠 How It Works

### **1. Haarcascade detects faces**

Uses:

```
haarcascade_frontalface_default.xml
```

### **2. LBPH trains on dataset**

LBPH learns patterns of each user based on grayscale images.

### **3. Webcam starts recognition**

When you appear in front of the camera:

✔ If recognized → shows your name
✔ If unknown → labels as “unknown"
✔ If unknown for 100+ frames → captures image

---

## ❗ Common Errors & Fixes

### **❌ Error: Empty training data**

**Fix:** Ensure dataset folders contain images.

### **❌ Error: LBPH requires more than one sample**

**Fix:** Add at least 5–10 images per user.

### **❌ haarcascade not found**

**Fix:** Place the file in same folder OR give full path:

```
haarcascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
```

### **❌ Camera not opening**

Try:

```
webcam = cv2.VideoCapture(0)
```

or

```
webcam = cv2.VideoCapture(1)
```

---

## 📷 Output Preview

Recognized face example:

```
[ payal - 62.3 ]
```

Unknown face example:

```
unknown person
```

---

## 🙌 Author

**Payal Koregave**

If you upload this to GitHub, add:

```
⭐ Star this repo if you like this project!
```

---


