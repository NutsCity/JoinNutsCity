import os
import sys
from ping3 import ping
import webbrowser

fast_cn = "china.nutscity.tk"
fast_cn2 = "111.67.193.130"
play = "play.nutscity.tk"

add_command = "minecraft://?addExternalServer={name}|{ip}"


def test_speed():
    test_cn = int(ping(fast_cn, 114514) * 1000)
    test_cn2 = int(ping(fast_cn2, 114514) * 1000)
    test_play = int(ping(play, 114514) * 1000)
    speed = {fast_cn: test_cn, fast_cn2: test_cn2, play: test_play}
    return speed

def get_better_ip():
    all_ip = test_speed()
    # n_l = list(all_ip.keys()) # ip列表
    s_l = list(all_ip.values()) # ping列表
    min_ping = min(s_l)
    for i, s in enumerate(all_ip.values()):
        if min_ping == s:
            return list(all_ip.keys())[i]

def add_to_minecraft(name: str, ip: str):
    """将服务器添加到Minecraft"""
    command = add_command.format(name=name, ip=ip)
    return webbrowser.open(command)

def title(t: str):
    if os.name == "nt":
        os.system(f"title {t}")

def pause():
    if os.name == "nt":
        os.system("pause")

def main():
    title("Join NC Server")
    if os.name != "nt":
        print("仅支持Windows 10进行运行!")
        sys.exit(1)
    ip = get_better_ip()
    print("Better NC Server ip is: {}".format(ip))
    res = input("你想让程序自动帮你添加到Minecraft中吗?(确认, [取消])/Do you want to add to Minecraft?(y, [N]): ").lower().replace(" ", "")
    if res in ["yes", "y", "是", "确认", "真"]:
        add_to_minecraft("NutsCity", ip)
    pause()


if __name__ == "__main__":
    main()
