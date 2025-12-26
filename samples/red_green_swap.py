from lib.base_animation import BaseAnimation
from typing import Optional

# RGB values
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# A Simple 1D Animation
class RedGreenSwap(BaseAnimation):
  def __init__(self, frameBuf, *, fps: Optional[int] = 1):
    super().__init__(frameBuf, fps=fps)
    self.t = 0

  def renderNextFrame(self):
    for i in range(len(self.frameBuf)):
      # Alternate pattern based on frame: even frames = even indices red, odd frames = odd indices red
      is_even_frame = (self.t % 2 == 0)
      is_even_index = (i % 2 == 0)
      self.frameBuf[i] = RED if (is_even_frame == is_even_index) else GREEN
    self.t += 1
