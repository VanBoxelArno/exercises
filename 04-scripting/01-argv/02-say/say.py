#!/usr/bin/env python
# Currently, in order to execute a script, you need to write `python script.py`.
# You can shorten this to `./script.py` if you add the following line at the top of your script:
import sys

print(" ".join(sys.argv[1:]))
