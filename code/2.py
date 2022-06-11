import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create() # 마인크래프트에 연결


while True:
  pos = mc.player.getTilePos() # 플레이어의 위치를 정수로 가져 옴 
  mc.postToChat(f"{pos.x}, {pos.y}, {pos.z}")

  time.sleep(0.5)