from hit import HitBox, HitBoxOBB
import numpy as np
import glm
from model import Model

class Cube(Model):
    def __init__(self, position=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), name="cube", hittable=True):
        self.name = name
        self.position = glm.vec3(*position)
        self.rotation = glm.vec3(*rotation)
        self.scale = glm.vec3(*scale)
        self.__colision = HitBoxOBB(
            get_model_matrix=lambda: self.get_model_matrix(), hittable=hittable
        )
        vertices = np.array([
            # posiciones        # colores
            -1, -1, -1,        1, 0, 0,
             1, -1, -1,        0, 1, 0,
             1,  1, -1,        0, 0, 1,
            -1,  1, -1,        1, 1, 0,
            -1, -1,  1,        1, 0, 1,
             1, -1,  1,        0, 1, 1,
             1,  1,  1,        1, 1, 1,
            -1,  1,  1,        0, 0, 0
        ], dtype='f4')

        colors = np.array([
            1,0,0, 0,1,0, 0,0,1, 1,1,0,
            1,0,1, 0,1,1, 1,1,1, 0,0,0
        ], dtype='f4')

        normals = np.array([
            -1,-1,-1, 1,-1,-1, 1,1,-1, -1,1,-1,
            -1,-1,1, 1,-1,1, 1,1,1, -1,1,1
        ], dtype='f4')

        textcoords = np.array([
            0,0, 1,0, 1,1, 0,1,
            0,0, 1,0, 1,1, 0,1
        ], dtype='f4')

        indices = np.array([
            0, 1, 2, 2, 3, 0,  # atrás
            4, 5, 6, 6, 7, 4,  # frente
            0, 4, 7, 7, 3, 0,  # izquierda
            1, 5, 6, 6, 2, 1,  # derecha
            3, 2, 6, 6, 7, 3,  # arriba
            0, 1, 5, 5, 4, 0   # abajo
        ], dtype='i4')
        super().__init__(vertices, indices, colors, normals, textcoords)

    def check_hit(self,origin, direction):
        return self._colision.check_hit(origin, direction)

    def get_model_matrix(self):
        model = glm.mat4(1)
        model = glm.translate(model, self.position)
        model = glm.rotate(model, glm.radians(self.rotation.x %360), glm.vec3(1, 0, 0))
        model = glm.rotate(model, glm.radians(self.rotation.y %360), glm.vec3(0, 1, 0))
        model = glm.rotate(model, glm.radians(self.rotation.z %360), glm.vec3(0, 0, 1))
        model = glm.scale(model,self.scale)
        return model
