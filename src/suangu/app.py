# coding=utf-8
import os
import time
import datetime


project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
os.chdir(project_dir)
os.sys.path.insert(0, os.path.join(project_dir, "src"))

from suangu import main


def send_msg(msg):
    os.system('msg /server:127.0.0.1 * "{0}"'.format(msg))


def log_msg(msg):
    now = datetime.datetime.now()
    now_str = now.strftime("%Y-%m-%d %H%M")
    _msg = "{now_str} {msg}".format(now_str=now_str, msg=msg)

    with open("log/st.log", "w+") as st_log_file:
        st_log_file.write(_msg)


def run_my_timer():
    while True:
        now = datetime.datetime.now()

        time_str = now.strftime("%H%M")

        if time_str not in ["13:35", "14:05", "14:35"]:
            time.sleep(10)
            continue

        selected_codes = main.suan_gu()
        if not selected_codes:
            log_msg("未选中任何股票")

        else:
            log_msg(",".join(selected_codes))
            send_msg(",".join(selected_codes))

        time.sleep(61)


if __name__ == '__main__':
    pid = os.getpid()
    log_msg("Start process:%s" % pid)
    send_msg("Start SuanGU process:%s" % pid)

    run_my_timer()
    print("over")




