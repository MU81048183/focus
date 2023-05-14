import time

def start_pomodoro(focus_time=25, break_time=5):
    print(f"开始专注 {focus_time} 分钟.")
    time.sleep(focus_time * 60)
    print(f"专注时间结束，休息 {break_time} 分钟.")
    time.sleep(break_time * 60)
    print("休息结束，重新开始专注.")

while True:
    start_pomodoro()
