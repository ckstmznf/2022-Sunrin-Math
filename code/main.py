from models import *
import time, math
from mimetypes import init
from mcpi.minecraft import Minecraft

mc = Minecraft.create() # 마인크래프트에 연결

pos = mc.player.getTilePos()

for i in range(-5, 5):
  mc.setBlock(pos.x + i, pos.y, pos.z, 35, 15)

_x = 0
while True:
  x = pos.x + _x
  
  y_sin = 15 * math.sin(x / 30 * math.pi - pos.x) + pos.y
  y_cos = 15 * math.cos(x / 30 * math.pi - pos.x) + pos.y
  y_tan = 15 * math.tan(x / 30 * math.pi - pos.x) + pos.y
  
  mc.setBlock(x + 5, pos.y, pos.z, 35, 15)  # x축

  mc.setBlock(x, y_sin, pos.z, 35, 14)  # sin
  mc.setBlock(x, y_cos, pos.z, 35, 11)  # cos
  mc.setBlock(x, y_tan, pos.z, 35, 13)  # cos

  _x += 1

  time.sleep(0.25)