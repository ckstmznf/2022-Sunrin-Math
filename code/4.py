import time
from models import *
from mimetypes import init
from mcpi.minecraft import Minecraft

mc = Minecraft.create() # 마인크래프트에 연결

diff_pos = Pos(7, 81, 6)

pos = mc.player.getPos()

for i in range(1000):
  print(f"{pos.x + i / 100}, {pos.y}, {pos.z}")
  mc.player.setTilePos(pos.x + i / 100, pos.y, pos.z)
  time.sleep(0.001)

diff_pos = Pos(7, 81, 6)
def tp(x, y, z):
  mc.player.setTilePos(x - diff_pos.x, y - diff_pos.y, z - diff_pos.z)

def setBlock(x, y, z, blockId, blockState = 1):
  mc.setBlock(x - diff_pos.x, y - diff_pos.y, z - diff_pos.z, blockId, blockState)