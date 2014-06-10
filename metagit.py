#!/usr/bin/env python3

from optparse import OptionParser
import sys
import meta_commands
import os
import time

parser = OptionParser()

commands = {'list': meta_commands.cmd_list, 'cd': meta_commands.cmd_cd, 'tags': meta_commands.cmd_tags, 'find': meta_commands.cmd_find, 'sync': meta_commands.cmd_sync}


if __name__ == "__main__":
    options, args = parser.parse_args()

    # check for offline cache file existance or 5h age
    if (not os.path.isfile("metagit_cache.json")) or (time.time() -
            os.stat("metagit_cache.json").st_mtime) > 60*60*5:
        print("Cache File is too old, syncing")
        commands['sync']()

    if len(args) > 0 and args[0] in commands:
        commands[args[0]]()
    else:
        print("Give me a command! Valid Commands are " + ", ".join(commands.keys()))
        sys.exit(1)
