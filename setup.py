from setuptools import setup

setup(
    name="clerk",
    version='0.0.1',
    packages=['clerk', 'clerk.processors'],
    install_requires=[
        'masonite',
        'stripe'
    ],
    include_package_data=True,
)
