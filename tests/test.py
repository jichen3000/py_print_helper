import os, sys, inspect

# add parent path aka minitest to sys.path, so I can import the files
# realpath() will make your script run, even if you symlink it :)
current_file_path = os.path.split(inspect.getfile( inspect.currentframe() ))[0]
parent_file_path = os.path.realpath(os.path.abspath(os.path.join(current_file_path, '..')))
if parent_file_path not in sys.path:
    sys.path.insert(0, parent_file_path)

import print_helper
message = "test"
none = None

message.p()
message.pp()
print(message.p_format())
print(message.pp_format())

none.p()


message.pl()
message.ppl()
print(message.pl_format())
print(message.ppl_format())

