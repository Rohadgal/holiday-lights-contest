from typing import Dict
from lib.base_controller import BaseController
import numpy as np
from utils.geometry import POINTS_3D
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class MatplotlibController(BaseController):

  def __init__(self, animation, animation_kwargs: Dict, n_pixels: int, validate_parameters=True, background_color: str = 'black'):
    super().__init__(animation, animation_kwargs, n_pixels, validate_parameters=validate_parameters)
    screencolor = background_color
    self.fig = plt.figure(figsize=(10, 10), facecolor=screencolor)
    self.ax = self.fig.add_subplot(111, projection='3d')
    self.ax.set_facecolor(screencolor)
    self.points = POINTS_3D
    self.sizes = 100 * np.ones(n_pixels)
    self.scatter = self.ax.scatter(self.points[:, 0], self.points[:, 1], self.points[:, 2], c=self.frameBuf / 255, s=self.sizes, marker='o', edgecolors=None, alpha=0.4)
    self.ax.set_aspect('equal')

  def run(self):
    interval = int(self.animation.period * 1000) if self.animation.period > 0 else 10
    self.ani = FuncAnimation(self.fig, self.update, interval=interval, frames=None, cache_frame_data=False)
    plt.grid(False)
    plt.axis('off')
    plt.show()

  def update(self, frame):
    self.animation.renderNextFrame()
    self.scatter.set_color(self.frameBuf / 255)

