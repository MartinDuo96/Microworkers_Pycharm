import Youtube
import getId
import time
# XeniaDidThat

# Search for the URL
url = 'https://www.youtube.com/watch?v=XbqFZMIidZI&ab_channel=PopCornRest-TikTok'
time_lst = Youtube.get_duration(url)
min = ''
sec = ''
if Youtube.min:
    min = Youtube.min
if Youtube.sec:
    sec = Youtube.sec

# open video link
getId.mouse_left(583, 1051)
getId.mouse_left(545, 51)
getId.keyboard_ctrl_v()
getId.keyboard_enter()

# Watch Youtube via pynput
if min:
    if sec:
        time.sleep(int(min)*60 + int(sec))
        print('waited:', str(int(min)*60 + int(sec)))
    else:
        time.sleep(int(min)*60)
        print('waited:', str(int(min)*60))
else:
    time.sleep(int(sec))
    print('waited:', str(int(sec)))
