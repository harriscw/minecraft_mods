from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# get player position
position=mc.player.getTilePos()
x=position.x
y=position.y
z=position.z

# super jump player
mc.player.setTilePos(x,y+5,z)

# put player on a safe pedestal above lava
for i in range(4):
    mc.setBlock(x,y+i,z,103)

# create a protective 5x5 lava moat
for xmod in range(-2,3):
    for zmod in range(-2,3):
        if xmod==0 and zmod==0:
            continue
        else:
            mc.setBlock(x+xmod,y-1,z+zmod,10)