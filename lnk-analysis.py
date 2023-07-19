import LnkParse3
import os

CYAN = '\033[36m'
RED = '\033[31m'
END = '\033[m'

filename = 'C:/badlink.lnk'

if os.path.isfile(filename):
    print(CYAN + 'Valid file\n', END)

    with open(filename, 'rb') as stream:
        lnk = LnkParse3.lnk_file(stream)
        res = lnk.get_json()

        print(CYAN + 'Original command', END)
        cmd = res['data']['command_line_arguments']
        print(cmd)

        print(CYAN + 'Tidied command', END)
        cmd = cmd.replace('^', '')
        cmd = cmd.lower()
        printable = '01234567890abcdefghijklmnopqrstuvwxyz/.:;()<>-_~#%$&*{}@?| !='
        cmd = ''.join(filter(lambda x: x in printable, cmd))
        while '  ' in cmd:
            cmd = cmd.replace('  ', ' ')
        print(cmd)

        print(CYAN + 'Description', END)
        print(res['data']['description'])

        print(CYAN + 'Machine identifier', END)
        if 'DISTRIBUTED_LINK_TRACKER_BLOCK' in res['extra']:
            print(res['extra']['DISTRIBUTED_LINK_TRACKER_BLOCK']['machine_identifier'])

else:
    print(RED + 'Not a valid file\n', END)
