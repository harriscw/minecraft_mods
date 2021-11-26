from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x=4
y=64
z=9
blockType=103
mc.setBlock(x,y+1,z,blockType)