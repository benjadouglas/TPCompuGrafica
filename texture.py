import numpy as np

class Texture:
    def __init__(self, name="u_texture", width=1, height=1, channels_amount=4, image_data=None,
                 repeat_x=False, repeat_y=False, build_mipmaps=False):
        self.name = name
        self.size = (width, height)
        self.channels_amount = channels_amount
        self.image_data = image_data.tobytes() if image_data is not None else None
        self.repeat_x = repeat_x
        self.repeat_y = repeat_y
        self.build_mipmaps = build_mipmaps

class ImageData:
    def __init__(self, height, width, channels, color=(0, 0, 0)):
        self.data = np.full((height, width, channels), color, dtype=np.uint8)

    def set_pixel(self, x, y, color):
        self.data[y, x] = color  # ojo invertido!! es (y,x), no (x,y)

    def tobytes(self):
        return self.data.tobytes()
