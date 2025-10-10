import platform

#현재 파이썬이 실행되는 플랫폼 확인

def is_windows_platform():
    return platform.system() == 'Windows'

def is_mac_platform():
    return platform.system() == 'Darwin'

def is_linux_platform():
    return platform.system() == 'Linux'

def get_font_name():
    if is_mac_platform():
        return 'AppleGothic'
    elif is_linux_platform():
        return 'linuxFont?'
    else:
        return 'Malgun Gothic'