# # from ursina import *
# # from ursina.prefabs.first_person_controller import FirstPersonController

# # app = Ursina() # app object with ursina.


# # textures = {
# #     1: load_texture("Assets/Textures/Grass.png"),
# #     2: load_texture("Assets/Textures/Dirt.png"),
# #     3: load_texture("Assets/Textures/Brick.png"),
# #     4: load_texture("Assets/Textures/Stone.png"),
# #     5: load_texture("Assets/Textures/Wood.png"),
# # }

# # sky_bg = load_texture("Assets/Textures/Sky.png")
# # build_sound = Audio("Assets/SFX/Build_Sound.wav", loop=False, autoplay=False) # autoplay false since not a background game

# # class Block(Button):
# #     # every block in minecraft is a button
# #     def __init__(self, position=(0,0,0), texture = textures[1], breakable=True): # since every block has a position
# #         super().__init__(
# #             parent = scene,
# #             position = position,
# #             model = "Assets/Models/Block.obj",
# #             origin_y = 0.5,
# #             texture = texture,
# #             # color = color.color(0, 0, random.uniform (0.9, 1)), # changes so not all green
# #             # highlight_color = color.light_gray, # light gray to know that we are looking at the block
# #             scale = 0.5
# #         )
# #         self.breakable = breakable

# # for z in range(20): # game is 20x20
# #     for x in range(20):
# #         block = Block(position = (x, 0, z))
# #         bedrock = Block(position = (x, -1, z), texture = textures[5], breakable = False)

# # def update():
# #     if held_keys["escape"]:
# #         application.quit()


# # if __name__ == "__main__":
# #     app.run()
# from panda3d.core import loadPrcFileData
# loadPrcFileData('', 'gl-version 3 2')
# # loadPrcFileData('', 'gl-version 4 1')  # try this if 3 2 doesn't work



# from ursina import * 
# from ursina.prefabs.first_person_controller import FirstPersonController 

# app = Ursina()

# gsg = base.win.getGsg()
# print("OpenGL version:", gsg.getDriverVersion())
# print("Vendor:", gsg.getDriverVendor())
# print("Renderer:", gsg.getDriverRenderer())

# # load all assets
# textures = {
#     1: load_texture("Assets/Textures/Grass.png"),
#     2: load_texture("Assets/Textures/Dirt.png"),
#     3: load_texture("Assets/Textures/Brick.png"),
#     4: load_texture("Assets/Textures/Wood.png"),
#     5: load_texture("Assets/Textures/Stone.png"),
    
# }

# sky_bg = load_texture("Assets/Textures/Sky.png")
# build_sound = Audio("Assets/SFX/Build_Sound.wav", loop=False, autoplay=False)

# block_pick = 1

# class Block(Button):
#     def __init__(self, position=(0,0,0), texture=textures[1], breakable=True):
#         super().__init__(
#             parent=scene,
#             position=position,
#             model="Assets/Models/Block.obj",
#             origin_y=0.5,
#             texture=texture,
#             color=color.hsv(0,0,random.uniform(0.9, 1)),
#             # highlight_color=color.rgb.light_gray,
#             scale=0.5
#         )
#         self.breakable = breakable
    
#     def input(self, key):
#         if self.hovered:
#             if key == "left mouse down":
#                 build_sound.play()
#                 new_block = Block(position=self.position + mouse.normal, texture=textures[block_pick])
#             elif key == "right mouse down" and self.breakable:
#                 build_sound.play()
#                 destroy(self)
        
           
# class Sky(Entity):
#     def __init__(self):
#         super().__init__(
#             parent=scene,
#             model="sphere",
#             texture=sky_bg,
#             scale=150,
#             double_sided=True
#         )
    
  
# class Tree(Entity):
#     def __init__(self, position=(0,0,0)):
#         super().__init__(
#             parent=scene,
#             position=position,
#             model="Assets/Models/Lowpoly_tree_sample.obj",
#             scale=(0.6,0.6,0.6),
#             collider="mesh"
#         )  
        
# def generate_trees(num_trees=3, terrain_size=20):
#     for _ in range(num_trees):
#         x = random.randint(0, terrain_size-1)
#         y = 3
#         z = random.randint(0, terrain_size-1)
#         Tree(position=(x,y,z))


# def generate_terrain():
#     height = 5 
#     for z in range(20):
#         for x in range(20):
            
#             for y in range(height):
#                 if y == height-1:
#                     Block(position=(x,y,z), texture=textures[1])
#                 elif y >= height-3:
#                     Block(position=(x,y,z), texture=textures[2])
#                 else:
#                     Block(position=(x,y,z), texture=textures[5])
            
#             Block(position=(x,-1,z), texture=textures[5], breakable=False)
            



# # update / input
# def update():
#     global block_pick
#     for i in range(1,6):
#         if held_keys[str(i)]:
#             block_pick = i
#             break
    
    
#     if held_keys["escape"]:
#         application.quit()   
#     if player.y <= -5:
#         player.position = (10,10,10)



# player = FirstPersonController(position=(10,10,10))
# player.cursor.visible = False
# sky = Sky()
# generate_trees()
# generate_terrain()

# if __name__ == "__main__":
#     app.run()








# from ursina import *
# from ursina.prefabs import button

# # create a window
# app = Ursina()

# # most things in ursina are Entities. An Entity is a thing you place in the world.
# # you can think of them as GameObjects in Unity or Actors in Unreal.
# # the first parameter tells us the Entity's model will be a 3d-model called 'cube'.
# # ursina includes some basic models like 'cube', 'sphere' and 'quad'.

# # the next parameter tells us the model's color should be orange.

# # 'scale_y=2' tells us how big the entity should be in the vertical axis, how tall it should be.
# # in ursina, positive x is right, positive y is up, and positive z is forward.

# player = Entity(model='cube', color=color.orange, scale_y=2)

# # create a function called 'update'.
# # this will automatically get called by the engine every frame.

# def update():
#     player.x += held_keys['d'] * time.dt
#     player.x -= held_keys['a'] * time.dt

# # this part will make the player move left or right based on our input.
# # to check which keys are held down, we can check the held_keys dictionary.
# # 0 means not pressed and 1 means pressed.
# # time.dt is simply the time since the last frame. by multiplying with this, the
# # player will move at the same speed regardless of how fast the game runs.


# def input(key):
#     if key == 'space':
#         player.y += 1
#         invoke(setattr, player, 'y', player.y-1, delay=.25)


# # start running the game
# app.run()


