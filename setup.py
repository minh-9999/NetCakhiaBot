from setuptools import setup, find_packages

setup(
    name="net_cakhia_bot",
    version="0.1",
    packages=find_packages(),
    install_requires=["speedtest-cli", "schedule", "gtts", "selenium", "yagmail"],
    entry_points={"console_scripts": ["net-cakhia=main:main"]},
)
