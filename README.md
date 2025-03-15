# Danger Detection with ML

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A real-time threat detection system using computer vision and machine learning to identify potentially dangerous objects (firearms and fire) and provide instant email notifications with visual evidence.


Made with ❤️, for Safety 🦺


## 🎯 Features

- Real-time detection of guns, rifles, and fire in video streams
- Automated email notifications with captured images
- Easy-to-use interface for security monitoring
- Configurable alert thresholds and notification settings

## 🌟 System Requirements

- Python 3.8+
- OpenCV 4.5+
- CUDA support (optional, for GPU acceleration)
- Webcam or USB camera
- Minimum 4GB RAM
- x86_64 architecture
- Git (for cloning)

## 🚀 Quick Start

### Installation

1. Clone the repository:
```bash
git clone https://github.com/phanindra-max/danger-detection-with-ml.git
cd danger-detection-with-ml
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Your `requirements.txt` should contain:
```txt
opencv-python>=4.5.0
numpy>=1.19.0
argparse>=1.4.0
```

### Required Files Setup

1. **Download YOLOv3 weights and config:**
```bash
# Download weights
curl -L https://pjreddie.com/media/files/yolov3.weights -o yolov3.weights

# Download config
curl -L https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg -o yolov3.cfg
```

2. **Create obj.names file:**
Create a new file named `obj.names` with the following content:
```txt
gun
rifle
fire
```

### Email Configuration

1. **Setup Gmail Authentication:**
   - Enable 2-Factor Authentication in your Gmail account
   - Generate an App Password:
     1. Go to Google Account → Security → App Passwords
     2. Select "Mail" and "Windows Computer"
     3. Copy the 16-digit password

2. **Update Email Settings:**
```python
# In main.py, update these variables:
mailfrom = "<your.email@gmail.com>"
gmailpass = "<your-16-digit-app-password>"
mailto = "<receiver@email.com>"
```

## 💻 Usage

### Command Line Options

```bash
python main.py [--webcam True/False] [--image True/False] [--image_path PATH] [--verbose True/False]
```

Options:
- `--webcam`: Enable webcam mode
- `--image`: Enable image mode
- `--image_path`: Path to input image (default: "use-this.jpg")
- `--verbose`: Enable verbose output

### Basic Usage

```bash
python main.py
```
When prompted, enter 'Y' to start webcam detection.

## 📊 Performance

- Average processing speed: 25 FPS on CPU
- GPU acceleration available with CUDA support
- Accuracy depends on image quality and lighting conditions

## 🤝 Contributing

We welcome contributions! Please see Contributing Guidelines.

## 🌈 Community & Support

- [Twitter](https://x.com/phanindraMax)
- [BlueSky](https://bsky.app/profile/phanindra-max.bsky.social)
- [LinkedIn](https://www.linkedin.com/in/phanindra-max/)


## 🙏 Acknowledgments

- YOLOv3 team for the detection model
- OpenCV community for vision tools

## 📈 Roadmap

- [ ] Add support for more object types
- [ ] ~Implement real-time API~ (Abandoned due to monetary constraints)
- [ ] Improve detection accuracy
- [ ] Add cloud deployment options

---

Made with ❤️ for Safety 🦺
