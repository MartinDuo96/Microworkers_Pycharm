from openpyxl import load_workbook
import getId
import time

# variables
search = '/userinfo.php?Id='
clipboard = ''
employer_id = ''
employer_dict = {'Member_9867397535': 'Canada', 'Member_497313': 'France', 'Member_589432': 'Thailand',
                 'Member_5423101138': 'Cyprus', 'Member_9301310899': 'Russia', 'Member_69213': 'Test'}

# open inspect
mouse = getId.pynput.mouse.Controller()
keyboard = getId.pynput.keyboard.Controller()

# Read pointer position/userinfo.php?Id=
print('The current pointer position is {0}', format(mouse.position))

getId.mouse_left(583, 1051)
getId.mouse_right(1014, 612)
getId.mouse_left(1087, 935)
getId.mouse_left(1506, 382)
getId.keyboard_ctrl_f()
getId.save_clipboard(search)
getId.keyboard_ctrl_v()
getId.keyboard_enter()
getId.mouse_right(1739, 635)
getId.mouse_left(1763, 754)
getId.mouse_left(1646, 756)
getId.update_clipboard()
getId.get_employer_id()






'''
path = r'C:\Users\marti\OneDrive\Desktop\Microworker\Microworker_1.xlsx'
wb = load_workbook(path)
ws = wb['Tabelle1']
'''