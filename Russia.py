import Youtube
import getId
import time
import screenshot


# XeniaDidThat

# Extract the URL from Text (Microworkers)
# With pyinput (Mouse hold) Not Playboy Bunny Tattoo #shorts  XeniaDidThat
getId.mouse_left(583, 1051)
getId.mouse_left(1778, 228)
getId.scroll_end()
getId.mouse_left(1423, 526)
getId.select_all()
getId.keyboard_ctrl_c()
getId.update_clipboard()
print(type(getId.clipboard))


# Get the search text
text = str(getId.clipboard)
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


# Go to youtube and search for video
getId.new_tab()
getId.type_youtube()
getId.keyboard_enter()
time.sleep(3)
getId.mouse_left(732, 128)
getId.keyboard_ctrl_v()
getId.keyboard_enter()
time.sleep(1)
getId.mouse_left(712, 328)
time.sleep(20)

# Copy the URL
getId.mouse_left(545, 51)
getId.keyboard_ctrl_c()
url = getId.pyperclip.paste()
print(url)

# Duration of video
#time_lst = Youtube.get_duration(url)
#print(time_lst)
#print(time_lst['items'])
time_lst = Youtube.get_duration(url)

min = ''
sec = ''
if Youtube.min:
    min = Youtube.min
if Youtube.sec:
    sec = Youtube.sec

'''
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
'''

time.sleep(5)   # test

# like video
getId.mouse_left(1002, 964)

# screenshot proof
getId.mouse_left(39, 325)
getId.scroll_down()
screenshot.takeScreenshot()

# Add screenshot



