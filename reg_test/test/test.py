# -*- coding:utf-8 -*-
__author__ = "leo"

import re

# line = "leo123"
# line = "hello11world"
line = "xxx出生于2000年3月2日"
line = "xxx出生于2000/3/2"
line = "xxx出生于2000-3-2"
line = "xxx出生于2000-03-02"
line = "xxx出生于2000-03"

# regex_str = "^l.*3$"
# regex_str = ".*?(e.*?o).*"
# regex_str = ".*(e.+o).*"
# regex_str = ".*(e.{2,}o).*"
# regex_str = "(leo|leo123)"
# regex_str = "([asdlkj]eo[^5]{3})"
# regex_str = "(hello\w+world)"
regex_str = ".*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}|[月/-]$|$))"

match_obj = re.match(regex_str, line)

if match_obj:
    print(match_obj.group(1))
else:
    print("no")