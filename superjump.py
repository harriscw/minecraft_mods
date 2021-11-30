from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position=mc.player.getTilePos()

x=position.x
y=position.y+15
z=position.z

mc.player.setTilePos(x,y,z)