import sys
import os
from dotenv import load_dotenv
import clipboard



def read_clipboard():
    content = clipboard.paste()
    filter = get_filter()
    if filter is None or filter.lower() in content.lower():
        with open(os.getenv("DATA"), 'a') as f:
            f.write(content)
    print(filter, content)


def set_filter(filter):
    with open(os.getenv("FILTER"), 'w') as f:
        f.write(filter)


def get_filter():
    if os.path.isfile(os.getenv("FILTER")):
        with open(os.getenv("FILTER")) as f:
            filter = f.readline().replace('\n', '').strip()
            if filter != '':
                return filter
            else:
                return None
    else:
        return None

def get_last_content():
    if os.path.isfile(os.env("DATA")):
        with open(os.env("DATA")) as f:
            filter = f.readline().replace('\n', '').strip()
            if filter != '':
                return filter
            else:
                return None
    else:
        return None


def main():
    load_dotenv()
    if len(sys.argv) == 1:
        read_clipboard()

    elif len(sys.argv) == 2:
        if sys.argv[2] == '-clear':
            pass

    elif len(sys.argv) == 3 and sys.argv[1] == '-f' or sys.argv[1] == '-filter':
        set_filter(sys.argv[2])

    else:
        pass


if __name__ == '__main__':
    main()
