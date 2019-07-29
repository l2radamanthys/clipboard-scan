import os
import sys
import time
from dotenv import load_dotenv
import clipboard



def read_clipboard():
    content = clipboard.paste()
    last = get_last_content()
    if content != last:
        filter_ = get_filter()
        if filter_ is None or filter_.lower() in content.lower():
            with open(os.getenv("DATA"), 'a') as f:
                f.write(f"{content}\n")
                print('COPIADO \t', content)


def set_filter(filter_):
    with open(os.getenv("FILTER"), 'w') as f:
        f.write(filter_)


def get_filter():
    if os.path.isfile(os.getenv("FILTER")):
        with open(os.getenv("FILTER")) as f:
            filter_ = f.readline().replace('\n', '').strip()
            if filter_ != '':
                return filter_
            else:
                return None
    else:
        return None

def get_last_content():
    fname = os.getenv("DATA")
    if os.path.isfile(fname):
        last = os.popen(f"tail -n 1 {fname}").read()
        return last.replace('\n', '').strip()
    else:
        return None


def main():
    load_dotenv()
    if len(sys.argv) == 1:
        while True:
            read_clipboard()
            time.sleep(3)

    elif len(sys.argv) == 2:
        if sys.argv[1] == '-clear':
            os.remove(os.getenv("DATA"))

    elif len(sys.argv) == 3 and sys.argv[1] == '-f' or sys.argv[1] == '-filter':
        set_filter(sys.argv[2])

    else:
        pass


if __name__ == '__main__':
    main()