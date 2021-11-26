from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position=mc.player.getTilePos()

x=position.x+1
y=position.y
z=position.z
blockType=103

for i in range(6):
    mc.setBlock(x,y+i,z,blockType)