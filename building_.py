from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# get player position
position=mc.player.getTilePos()
x=position.x
y=position.y
z=position.z
width=10
height=6
length=5
blockType=4
air=0

# create structure
mc.setBlocks(x,y,z,x+width,y+height,z+length,blockType)

# make it hollow
mc.setBlocks(x+1,y+1,z+1,x+width-1,y+height-1,z+length-1,air)
