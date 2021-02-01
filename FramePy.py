import os
print('Using FramePy as an API')
try:
  import FrameBoost
except:
  pass
  
def dynamic(code):
  #Dynamic cannot dynamicly import.
  eval(code)
