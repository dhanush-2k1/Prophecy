from setuptools import setup, find_packages
setup(
    name = 'reparition',
    version = '1.0',
    packages = find_packages(include = ('reparition*', )) + ['prophecy_config_instances.reparition'],
    package_dir = {'prophecy_config_instances.reparition' : 'configs/resources/reparition'},
    package_data = {'prophecy_config_instances.reparition' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.0.11'],
    entry_points = {
'console_scripts' : [
'main = reparition.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
