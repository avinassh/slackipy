from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='slackipy',
      version='0.1',
      description='Automate user invites to your Slack channel!',
      author='Avinash Sajjanshetty',
      author_email='hi@avi.im',
      url='https://github.com/avinassh/slackipy',
      install_requires=requirements,
      )
