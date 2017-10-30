"""

>>> import subprocess
>>> subprocess.check_output('python3.6 wc.py testinputs/testcase0.txt', shell=True)
b'wc: testinputs/testcase0.txt open: No such file or directory\\n'

>>> subprocess.check_output('python3.6 wc.py testinputs/testcase1.txt', shell=True)
b'\\t0\\t0\\t0 testinputs/testcase1.txt\\n'

>>> subprocess.check_output('python3.6 wc.py testinputs/testcase2.txt', shell=True)
b'\\t9\\t10\\t20 testinputs/testcase2.txt\\n'

>>> subprocess.check_output('python3.6 wc.py -w testinputs/testcase3.py', shell=True)
b'\\t31 testinputs/testcase3.py\\n'

>>> subprocess.check_output('python3.6 wc.py -wlc testinputs/testcase4.txt', shell=True)
b'\\t6\\t133\\t795 testinputs/testcase4.txt\\n'

>>> subprocess.check_output('python3.6 wc.py -w testinputs/testcase5.txt', shell=True)
b'\\t2 testinputs/testcase5.txt\\n'

>>> subprocess.check_output('python3.6 wc.py testinputs/testcase6.txt', shell=True)
b'\\t0\\t1\\t4 testinputs/testcase6.txt\\n'

>>> subprocess.check_output('python3.6 wc.py testinputs/testcase6.txt', shell=True)
b'\\t0\\t1\\t4 testinputs/testcase6.txt\\n'

>>> subprocess.check_output('python3.6 wc.py testinputs/testcase6.txt', shell=True)
b'\\t0\\t1\\t4 testinputs/testcase6.txt\\n'

>>> subprocess.check_output('python3.6 wc.py testinputs/testcase6.txt', shell=True)
b'\\t0\\t1\\t4 testinputs/testcase6.txt\\n'

>>> subprocess.check_output('python3.6 wc.py testinputs/testcase6.txt', shell=True)
b'\\t0\\t1\\t4 testinputs/testcase6.txt\\n'

>>> subprocess.check_output('python3.6 wc.py -y', shell=True)
b"wc: invalid option -- '-y'Try 'wc --help' for more information.\\n"

>>> subprocess.check_output('python3.6 wc.py -w testinputs/testcase5.txt testinputs/testcase6.txt', shell=True)
b'\\t2 testinputs/testcase5.txt\\n\\t1 testinputs/testcase6.txt\\n\\t0\\t3\\t0 total\\n'


"""
