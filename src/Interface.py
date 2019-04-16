import StringUtils
import time

def story(text):
    storyParts = text.split('#')
    for part in storyParts:
        if StringUtils.isNumber(part):
            time.sleep(float(part))
        else:
            print(part)
