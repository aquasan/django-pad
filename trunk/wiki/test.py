import merge3

base = """abc
def
ghi
"""
a = """abc
de
ghi
"""

b = """abc
d
ghi
"""
merger = merge3.Merge3(base, a, b)

print "".join([i for i in merger.merge_lines()])
