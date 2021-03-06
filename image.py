
from PIL import Image, ImageDraw, ImageFont

def tweet2image(video, image, tweet):
  tweets = tweet.split(" ")
  tw_len = 0
  text_temp = ""
  for tw in tweets:
    tw_len = tw_len + len(tw) + 1
    if (tw_len > 60):
      text_temp =  text_temp + "\n"
      tw_len = 0
    txt_temp = txt_temp + " " + tw
  text_temp = text_temp.encode('utf-8')


 font = ImageFont.load_default()
 filename = "images/" + str(video) + "-" + str(image) + ".png"
 tw_image = Image.new(mode = "RGB", size = (600,200), color = 'white')
 tweeter = ImageDraw.Draw(tw_image)
 tweeter.text((0,50),txt,fill=(0,0,0),spacing=10,align='left')
 tw_image.save(filename)   
