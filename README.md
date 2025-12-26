# Christmas Lights Animation Runner

A simplified animation runner for creating and visualizing 3D light animations using matplotlib. This repository contains everything you need to create and run a single animation.

## Requirements

- Python 3.10 or higher
- pip (Python package manager)

## Quick Start

1. **Set up a virtual environment (recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create your animation:**

   - Write your animation class in `animation.py`, OR
   - Use a sample: `python run_animation.py --sample moving_rainbow`

4. **Run your animation:**
   ```bash
   python run_animation.py
   ```

## Creating an Animation

Create a file called `animation.py` with a class that inherits from `BaseAnimation`:

```python
from lib.base_animation import BaseAnimation
from typing import Optional
import numpy as np

class MyAnimation(BaseAnimation):
    def __init__(self, frameBuf, *, fps: Optional[int] = 30):
        super().__init__(frameBuf, fps=fps)
        self.t = 0

    def renderNextFrame(self):
        # Update self.frameBuf with RGB values (0-255)
        # frameBuf is a numpy array of shape (NUM_PIXELS, 3)
        for i in range(len(self.frameBuf)):
            # Your animation logic here
            self.frameBuf[i] = [255, 0, 0]  # Red
        self.t += 1
```

### Key Points:

- **`frameBuf`**: A numpy array of shape `(500, 3)` containing RGB values (0-255) for each pixel
- **`fps`**: Optional frames per second (None = run as fast as possible)
- **`renderNextFrame()`**: Called every frame - update `self.frameBuf` here
- **Parameters**: Add optional parameters with defaults in `__init__` (use keyword-only args with `*`)

### Example with Parameters:

```python
from lib.base_animation import BaseAnimation
from typing import Optional, Collection
from utils.validation import is_valid_rgb_color

class SolidColor(BaseAnimation):
    def __init__(self, frameBuf, *, fps: Optional[int] = None,
                 color: Collection[int] = (255, 255, 255)):
        super().__init__(frameBuf, fps=fps)
        self.color = color

    def renderNextFrame(self):
        self.frameBuf[:] = self.color

    @classmethod
    def validate_parameters(cls, parameters):
        super().validate_parameters(parameters)
        full_parameters = {**cls.get_default_parameters(), **parameters}
        color = full_parameters['color']
        if not is_valid_rgb_color(color):
            raise TypeError("color must be a valid rgb color tuple")
```

## Running Animations

### Basic Usage

```bash
# Run with default parameters
python run_animation.py

# Run with custom parameters (JSON format)
python run_animation.py --args '{"fps": 60, "color": [255, 0, 0]}'

# Change background color
python run_animation.py --background white

# Skip parameter validation
python run_animation.py --no_validation
```

### Using Sample Animations

```bash
# List available samples
python run_animation.py --list-samples

# Run a sample directly
python run_animation.py --sample moving_rainbow

# Run a sample with custom parameters
python run_animation.py --sample snake --args '{"numFood": 20, "isRainbow": true}'
```

## Available Utilities

### Color Utilities (`utils/colors.py`)

- `hsv_to_rgb(h, s, v)` - Convert HSV to RGB
- `rgb_to_hsv(r, g, b)` - Convert RGB to HSV
- `randomColor()` - Generate a random color
- `rainbowFrame(t, NUM_PIXELS)` - Generate rainbow gradient
- `brightnessFrame(color, NUM_PIXELS)` - Generate brightness gradient

### Geometry Utilities (`utils/geometry.py`)

- `POINTS_3D` - Numpy array of shape `(500, 3)` with 3D coordinates for each pixel

### Validation Utilities (`utils/validation.py`)

- `is_valid_rgb_color(color)` - Validate RGB color tuple

## Sample Animations

The `samples/` folder contains example animations:

- **solid.py** - Solid color animation
- **moving_rainbow.py** - Animated rainbow wave
- **spiral.py** - 3D spiral pattern
- **snake.py** - Snake game animation

## Project Structure

```
.
├── animation.py              # Your animation (create this, or use --sample to run samples directly)
├── run_animation.py          # Main script
├── samples/                  # Example animations
│   ├── down_the_line.py
│   ├── red_green_swap.py
│   └── sweeping_planes.py
├── utils/                    # Utility functions
│   ├── colors.py            # Color utilities
│   ├── geometry.py          # 3D point coordinates
│   ├── validation.py        # Validation helpers
│   └── points/
│       └── 3dpoints.npy     # 3D coordinate data
├── lib/                      # Framework library (you don't need to modify these)
│   ├── base_animation.py    # BaseAnimation class
│   ├── base_controller.py   # BaseController class
│   ├── matplotlib_controller.py # Matplotlib visualization
│   └── constants.py        # NUM_PIXELS = 500
├── requirements.txt
└── README.md
```

## Notes

- The animation runs in a matplotlib 3D scatter plot window
- Press Ctrl+C to stop the animation
- `NUM_PIXELS` is hardcoded to 500 in `lib/constants.py`
- All animations must inherit from `BaseAnimation`
- Parameters are validated by default (use `--no_validation` to skip)
