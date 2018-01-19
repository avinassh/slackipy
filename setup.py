from setuptools import setup

setup(name='slackipy',
      version='0.1',
      description='Automate user invites to your Slack channel!',
      author='Avinash Sajjanshetty',
      author_email='hi@avi.im',
      packages = ['slackipy'],
      package_data = {'slackipy': ['static/*', 'templates/*']},
      url='https://github.com/avinassh/slackipy')
