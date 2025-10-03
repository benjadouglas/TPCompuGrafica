from graphics import Graphics
import glm

class Scene:
    def __init__(self, ctx, camera):
        self.ctx = ctx
        self.objects = []
        self.graphics = {}
        self.camera = camera
        self.model = glm.mat4(1)
        self.view = camera.get_view_matrix()
        self.projection = camera.get_perspective_matrix()

    def add_object(self, obj, shader_program):
        self.objects.append(obj)
        self.graphics[obj.name] = Graphics(self.ctx, shader_program, obj.vertices, obj.indices)

    def render(self):
       self.time += 0.01
       for obj in self.objects:
           obj.rotation.x += 0.8
           obj.rotation.y += 0.6
           obj.rotation.z += 0.4
           obj.position.x += math.sin(self.time) *0.01
           model = obj.get_model_matrix()
           mvp = self.projection * self.view * model
           self.graphics[obj.name].set_uniform('Mvp', mvp)
           self.graphics[obj.name].vao.render()


    def on_mouse_click(self, u, v):
        ray = self.camera.raycast(u, v)
        for obj in self.objects:
            if obj.check_hit(ray.origin, ray.direction):
                print(f"Golpeaste un objeto {obj.name}!")

    def on_resize(self, width, height):
        self.ctx.viewport = (0, 0, width, height)
        self.camera.aspect = width / height if height != 0 else 1.0
