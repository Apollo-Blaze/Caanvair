# Canvair 🎨✋

Canvair is an AI-powered virtual canvas that utilizes computer vision for intuitive drawing and interaction. Using hand gestures, you can draw, select tools, or erase content without touching any physical tools. It's an innovative project built with Python, OpenCV, and MediaPipe.

## Features
- **Drawing with Hand Gestures**: Use your index finger to draw on a virtual canvas.
- **Tool Selection**: Select different colors and brush types by showing two fingers and interacting with the top toolbar.
- **Eraser Mode**: Erase your drawings using an open palm (five fingers).
- **Dynamic Color Selection**: Choose from a range of colors using gestures to switch tools.
- **Interactive Header**: The top header displays available tools dynamically.
- **Canvas Integration**: Real-time drawing on a canvas with smooth brush and eraser functionalities.

## Demo of the Project
![Demo](demo.gif)

## Tech Stack
- **Python**: For scripting and backend logic.
- **OpenCV**: For video feed manipulation and real-time hand tracking.
- **MediaPipe**: For precise hand detection and tracking.
- **NumPy**: For array manipulations and canvas overlay.

## File Structure
- **canvair.py**: Main script that handles the drawing logic and gesture interactions.
- **HandTrackingModule.py**: Custom module for hand tracking using MediaPipe.
- **Header Folder**: Contains images for the toolbar (color and tool icons).
- **requirements.txt**: List of Python dependencies.

## Contributing
Feel free to fork the repository and submit pull requests for new features or bug fixes. Your contributions are always welcome!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy creating with **Canvair**! ✨
