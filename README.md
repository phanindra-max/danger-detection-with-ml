# Danger Detection with ML

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A real-time threat detection system using computer vision and machine learning to identify potentially dangerous objects (firearms and fire) and provide instant email notifications with visual evidence.

## 🎯 Features

- Real-time detection of guns, rifles, and fire in video streams
- Automated email notifications with captured images
- Easy-to-use interface for security monitoring
- Configurable alert thresholds and notification settings

## 🌟 Impact & Use Cases

- Enhanced security monitoring for public spaces
- Early fire detection systems
- Research and development in computer vision security
- Educational tool for ML/CV students

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Git (for cloning)
- Webcam or video input device

### Installation

1. Clone the repository:
```bash
git clone https://github.com/phanindra-max/danger-detection-ml.git
cd danger-detection-ml
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download YOLOv3 weights:
```bash
# Option 1: Using wget
wget https://mega.nz/file/jFxnXIJI#q7NgkCPMzWje2M_0EvOYyxT9oIkCLJ2SlbyklxfR13k -O yolov3.weights

# Option 2: Manual download
# Visit the link below and place the file in the project root:
# https://mega.nz/file/jFxnXIJI#q7NgkCPMzWje2M_0EvOYyxT9oIkCLJ2SlbyklxfR13k
```

### Configuration

1. Copy the example configuration file:
```bash
cp config.example.yml config.yml
```

2. Update `config.yml` with your email settings:
```yaml
email:
  sender: "your-email@gmail.com"
  password: "your-app-specific-password"
  recipient: "recipient@example.com"
```

### Usage

Run the main detection script:
```bash
python with_mail.py
```

## 📖 Documentation

- [Detailed Installation Guide](docs/installation.md)
- [Configuration Options](docs/configuration.md)
- [API Reference](docs/api.md)
- [Contributing Guidelines](CONTRIBUTING.md)


## 📊 Performance

- Average processing speed: 25 FPS on CPU
- Accuracy is dependent on image quality and performance is dependent on CPU capability.

## 🤝 Contributing

We welcome contributions from the community! Please be aware of the 

- Code style and standards
- Submission process
- Development workflow
- Bug reports and feature requests

## 🌈 Community & Support

Feel free to reach out to me in the discussions tab or in the following places:
- [Twitter](https://x.com/phanindraMax)
- [BlueSky](https://bsky.app/profile/phanindra-max.bsky.social)
- [LinkedIn](https://www.linkedin.com/in/phanindra-max/)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- YOLOv3 team for the object detection model
- OpenCV community for computer vision tools


## 📈 Roadmap

- [ ] Add support for more object types
- [ ] Implement real-time API
- [ ] Improve detection accuracy
- [ ] Add cloud deployment options


---

> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." – Martin Fowler

Made with Love❤️ for Safety🦺
