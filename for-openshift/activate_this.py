'''
Copyright (c) 2007 Ian Bicking and Contributors
Copyright (c) 2009 Ian Bicking, The Open Planning Project
Copyright (c) 2011-2015 The virtualenv developers

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

# Most of the content in following file is from `activate_this.py` file
# from virtualenv. It is modified to be used for Openshift only. (and version
# python 3.3 and above)

try:
    __file__
except NameError:
    raise AssertionError('You must run this using `exec`')

import sys
import os

old_os_path = os.environ.get('PATH', '')
virtenv = os.path.join(os.environ.get('OPENSHIFT_PYTHON_DIR', '.'), 'virtenv')
base = os.path.join(virtenv, 'venv')
os.environ['PATH'] = os.path.join(base, 'bin') + os.pathsep + old_os_path
site_packages = os.path.join(
    base, 'lib', 'python%s' % sys.version[:3], 'site-packages')
prev_sys_path = list(sys.path)

import site
site.addsitedir(site_packages)
sys.real_prefix = sys.prefix
sys.prefix = base
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path
