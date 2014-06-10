#!/usr/bin/env python3

from optparse import OptionParser
import sys
import meta_commands

parser = OptionParser()

commands = {'list': meta_commands.cmd_list, 'cd': meta_commands.cmd_cd, 'tags': meta_commands.cmd_tags, 'find': meta_commands.cmd_find, 'sync': meta_commands.cmd_sync}


if __name__ == "__main__":
    options, args = parser.parse_args()
    print(args)
    if len(args) > 0 and args[0] in commands:
        commands[args[0]]()
    else:
        print("Give me a command! Valid Commands are " + ", ".join(commands.keys()))
        sys.exit(1)
