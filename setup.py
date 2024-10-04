from setuptools import setup, find_packages

setup(
    name='chat_streamlit',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        # Adicione outras dependências
    ],
    entry_points={
        'console_scripts': [
            'chat_streamlit=app.main:main',
        ],
    },
)
