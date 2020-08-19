from PTL import Image, ImageDraw, ImageFont
from image import tweet2image

def imageflow (video_num, tweets):
  image = 0;
  for tweets in tweets:
    tweet2image(video, image, tweets)
    image += 1