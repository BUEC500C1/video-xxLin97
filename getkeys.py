import configparser

def getkeys():
  config = configparser.ConfigParser()
  config.read(r'keys')
  consumer_key = config.get('auth','consumer_key').strip()
  consumer_secret = config.get('auth','consumer_secret').strip()
  access_key = config.get('auth','access_token').strip()
  access_secret = config.get('auth','access_secret').strip()

  return([consumer_key,consumer_secret,access_key,access_secret])