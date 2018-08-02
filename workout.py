import time
import webbrowser

total_breaks = 3
break_count = 0

while(break_count < total_breaks):
    time.sleep(7200)
    webbrowser.open("https://www.youtube.com/watch?v=nBlYlSs2fIU")
    break_count = break_count + 1
