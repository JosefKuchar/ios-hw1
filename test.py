import fileinput
from subprocess import check_output, STDOUT
import os
tests = [a.lstrip() for a in ''.join(fileinput.input()).split('---')]
for test in tests[int(os.environ.get('START', 0)):]:
    i, _, do = test.partition('\n')
    do = do.replace('\r', '')
    print(i)
    assert i.startswith(
        '$'), f"the first character of a test case must $, got {i}"
    ro = check_output(i.removeprefix('$ '), shell=True,
                      stderr=STDOUT).decode('ascii')
    ro = ro.replace('\r', '')
    if '...' in do:
        start, end = do.split('...')
        assert ro.startswith(start), f"expected:\n{start!r}...\ngot:\n{ro!r}"
        assert ro.endswith(end), f"expected:\n...\n{end!r}\n\ngot:\n{ro!r}"
    else:
        assert ro == do, f"expected:\n{do}\n\ngot:\n{ro}"
