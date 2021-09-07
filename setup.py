from setuptools import setup
import os

def get_data_files(mypkg, dirs):
    data_files = []
    for folder in dirs:
        start_point = os.path.join(mypkg, folder)
        for root, dirs, files in os.walk(start_point):
            data_files.extend([os.path.join(*(root.split(os.path.sep)[1:]),i) for i in files])
    return data_files

setup(name='slackipy',
      version='0.1',
      description='Automate user invites to your Slack channel!',
      author='Avinash Sajjanshetty',
      author_email='hi@avi.im',
      packages = ['slackipy'],
      package_data = {'slackipy': get_data_files('slackipy', ['static','templates']) },
      url='https://github.com/avinassh/slackipy')
