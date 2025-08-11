from setuptools import setup, find_packages
setup(
    name = 'distrubuted',
    version = '1.0',
    packages = find_packages(include = ('distrubuted*', )) + ['prophecy_config_instances.distrubuted'],
    package_dir = {'prophecy_config_instances.distrubuted' : 'configs/resources/distrubuted'},
    package_data = {'prophecy_config_instances.distrubuted' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.0.11'],
    entry_points = {
'console_scripts' : [
'main = distrubuted.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
