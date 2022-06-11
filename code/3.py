from models import *
from mimetypes import init
from mcpi.minecraft import Minecraft

mc = Minecraft.create() # 마인크래프트에 연결

real = Pos(-366, 63, 296)

pos = mc.player.getTilePos()
diff_pos = Pos(real.x - pos.x, real.y - pos.y, real.z - pos.z)

diff_pos = Pos(7, 81, 6)

print(f"minecraft : {real.x}, {real.y}, {real.z}")
print(f"python : {pos.x}, {pos.y}, {pos.z}")
print(f"diff : {diff_pos.x}, {diff_pos.y}, {diff_pos.z}")

def tp(x, y, z):
  mc.player.setTilePos(x - diff_pos.x, y - diff_pos.y, z - diff_pos.z)

tp(-208, 70, 460)