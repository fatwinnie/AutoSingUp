import schedule
import time
import subprocess
from datetime import datetime
import sys

def run_ticket():
    python_executable = sys.executable
    subprocess.run([python_executable, "SignUP.py"])
    print("MSISignUP.py 已執行")
    return schedule.CancelJob  # 執行後取消任務

# 設定特定的執行時間,例如 2024/8/13 16:59:51
execution_time = datetime(2025,8,13,16,31,52)
now = datetime.now()
delay = (execution_time - now).total_seconds()

schedule.every(delay).seconds.do(run_ticket)

while True:
    schedule.run_pending()
    time.sleep(1)
