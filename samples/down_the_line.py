from lib.base_animation import BaseAnimation
from utils.colors import randomColor
from typing import Optional
from lib.constants import NUM_PIXELS

# Example 1D Animation
class DownTheLine(BaseAnimation):
  def __init__(self, frameBuf, *, fps: Optional[int] = None, rate: int = 10, decay: float = 0.9):
    super().__init__(frameBuf, fps=fps)
    self.rate = rate
    self.decay = decay
    self.t = 0
    self.color = randomColor()
    
  def renderNextFrame(self):
    # Change color every full cycle
    if self.t % NUM_PIXELS == 0:
      self.color = randomColor()

    # Light up pixels moving down the line
    for i in range(self.rate):
      index = (self.t % NUM_PIXELS) - (i * NUM_PIXELS // self.rate)
      self.frameBuf[index] = self.color
    
    # Apply decay to all pixels
    for i in range(NUM_PIXELS):
      self.frameBuf[i] = tuple(int(c * self.decay) for c in self.frameBuf[i])
    
    self.t += 1

  @classmethod
  def validate_parameters(cls, parameters):
    super().validate_parameters(parameters)
    full_parameters = {**cls.get_default_parameters(), **parameters}
    rate = full_parameters['rate']
    decay = full_parameters['decay']

    if rate <= 0:
      raise TypeError("rate must be > 0")
    if decay < 0 or decay >= 1:
      raise TypeError("decay must be between [0, 1)")
