import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import server
import sys
mc = minecraft.Minecraft()

mc.player.setTilePos(10,110,12)

time.sleep(5)

mc.player.setTilePos(0,0,0)