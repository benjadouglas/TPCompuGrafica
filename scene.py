from graphics import Graphics
import glm

class Scene:
    def __init__(self, ctx, camera):
        self.ctx = ctx
        self.objects = []
        self.graphics = {}
        self.camera = camera

    def add_object(self, obj, shader_program):
        self.objects.append(obj)
        self.graphics[obj.name] = Graphics(self.ctx, shader_program, obj.vertices, obj.indices)

    def render(self):
        # Clear the screen
        self.ctx.clear(0.1, 0.1, 0.1, 1.0)
        self.ctx.enable(self.ctx.DEPTH_TEST)

        # Get camera matrices
        view = self.camera.get_view_matrix()
        projection = self.camera.get_perspective_matrix()

        # Add rotation to each object to show 3D
        for i, obj in enumerate(self.objects):
            # Cubes rotate in Y, sphere rotates in X and Y
            if obj.name == "Cube1":
                obj.rotation.y += 1.0  # Cube1: clockwise
            elif obj.name == "Cube2":
                obj.rotation.y -= 1.0  # Cube2: counterclockwise
            elif obj.name.startswith("Sphere"):
                obj.rotation.x += 1.0
                obj.rotation.y += 1.0
            model = obj.get_model_matrix()
            mvp = projection * view * model

            # Set the MVP uniform
            graphics_obj = self.graphics[obj.name]
            if 'Mvp' in graphics_obj.vao.program:
                graphics_obj.vao.program['Mvp'].write(mvp.to_bytes())

            # Render
            graphics_obj.vao.render()

    def on_mouse_click(self, u, v):
        ray = self.camera.raycast(u, v)
        for obj in self.objects:
            if obj.check_hit(ray.origin, ray.direction):
                print(f"Golpeaste un objeto {obj.name}!")

    def on_resize(self, width, height):
        self.ctx.viewport = (0, 0, width, height)
        self.camera.aspect = width / height if height != 0 else 1.0
