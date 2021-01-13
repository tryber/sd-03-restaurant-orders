from setuptools import setup

setup(
    name="restaurant_orders",
    description="Projeto Restaurant Orders",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    install_requires=["pypubsub==4.0.3"],
)
