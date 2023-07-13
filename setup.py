from setuptools import setup

description = """Sample code for calling functions using native JSON feature of OpenAI API. 
Includes samples of calling multiple functions, 
chaining, and returning values back to ChatGPT."""

setup(
    name='gptFunctions',
    version='0.1',
    packages=[''],
    url='',
    license='MIT',
    author='Poul Hornsleth',
    author_email='',
    description=description,
    install_requires=[
        'openai',
        'python-dotenv',
        'yfinance'
    ]
)
