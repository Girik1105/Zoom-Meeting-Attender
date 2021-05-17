import os, time, csv
import subprocess
import pyautogui
from datetime import datetime

dir = 'C:\\Users\girik\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Zoom\Zoom'

def join_meeting(meeting_id, meeting_pwd):

    print('Opening Zoom')
    
    os.startfile(dir)
    
    # os.system(dir)
    # subprocess.Popen([dir])
    # subprocess.call([dir])
    
    print('Zoom opened successfully')
    
    # locatecenteronscreen will locate the button and by move to we will move the mouse over there
    # so that the next step takes place until zoom has loaded completely
    time.sleep(10)
    
    print('\nFinding Join Button')
    
    join_btn = pyautogui.locateCenterOnScreen('locators/join_meeting.png') 
    
    print('Located join button at', join_btn)  
   
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    print('Clicked on join button')

    time.sleep(3)
    
    print('\nTyping Meeting ID')
    
    pyautogui.write(meeting_id)
    
    print('Typed Meeting ID')

    print('\nFinding join button')
    
    join_meeting_btn = pyautogui.locateCenterOnScreen('locators/join.png')
    
    print('Located join button at', join_meeting_btn)

    pyautogui.click(join_meeting_btn)
    
    print('Clicked on join button')

    time.sleep(3)

    print('\nTyping meeting Password')

    pyautogui.write(meeting_pwd)

    print('Typed meeting Password')

    time.sleep(3)
    pyautogui.press('enter')
    print('\nPressed Enter')
    
    time.sleep(3)
    print('\nMeeting joined successfuly')


def leave_meeting():
    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)
    print('\nMeeting Left Successfully')
    

meetings = []

with open('meetings.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            print(f'Column names are {", ".join(row)}')
        else:
            meeting_val = {}
            meeting_val['start_time'] = row[0]
            meeting_val['end_time'] = row[1]
            meeting_val['id'] = row[2]
            meeting_val['pwd'] = row[3]
            meetings.append(meeting_val)
            print(row[0], row[1], row[2], row[3])
            line_count += 1
    

in_meeting = False

total_meetings = len(meetings)

start_meeting_counter = 0
end_meeting_counter = 0


while True:
    now = datetime.now().strftime('%H:%M')

    for val in meetings:
        
        if now in str(val['start_time']):
            meeting_id = val['id']
            meeting_pwd = val['pwd']

            join_meeting(meeting_id, meeting_pwd)

            print('\nMeeting will end at:', val['end_time'])

            start_meeting_counter += 1
            in_meeting = True
            
        
        if now in str(val['end_time']) and in_meeting == True:
            leave_meeting()

            next_meeting = meetings.index(val) + 1
            
            if next_meeting < len(meetings):
                print('\nNext meeting will start at:', meetings[next_meeting]['start_time'])

            end_meeting_counter += 1
            in_meeting = False

    if start_meeting_counter == end_meeting_counter == total_meetings:
        print('\nAll meetings completed for Today!')
        print('Have a nice Day!')
        break