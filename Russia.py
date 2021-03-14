import Youtube
import getId
import time
# XeniaDidThat

# Extract the URL from Text
# With pyinput (Mouse hold) Not Playboy Bunny Tattoo #shorts  XeniaDidThat

text = 'Search Not Playboy Bunny Tattoo #shorts You have to choose the same preivew image:'
text_list = text.split(' ')
print(text_list.index('Search'))
print(text_list.index('You'))
text = ''
for i in text_list[text_list.index('Search'):text_list.index('You')]:
    text += i + ' '
text = text.replace('Search', '')
text = text + ' XeniaDidThat'
getId.save_clipboard(text)
print(text)

# Click on the video and get the URL of it
getId.mouse_left(583, 1051)
getId.mouse_left(732, 128)
getId.keyboard_ctrl_v()
getId.keyboard_enter()
time.sleep(1)
getId.mouse_left(712, 328)

# Copy the URL
getId.mouse_left(545, 51)
getId.keyboard_ctrl_c()
url = getId.pyperclip.paste()
print(url)

# Duration of video
time_lst = Youtube.get_duration(url)
min = ''
sec = ''
if Youtube.min:
    min = Youtube.min
if Youtube.sec:
    sec = Youtube.sec

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

# proof
# screenshot
# Add screenshot