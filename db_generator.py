import requests
import os
import time
current_total_images = len(os.listdir("faces/images"))
IMAGE_URL = "https://thispersondoesnotexist.com/image"
number_images = 1000
for i in range(1+current_total_images, current_total_images+number_images+1):
    i = "0"+str(i) if i <=9 else str(i)
    with open(f"faces/images/face{i}.png", 'wb') as f:
      image = requests.get(IMAGE_URL).content
      f.write(image)
      if int(i)%100==0: print(i)
      time.sleep(1)
