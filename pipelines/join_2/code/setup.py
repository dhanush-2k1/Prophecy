from setuptools import setup, find_packages
setup(
    name = 'join_2',
    version = '1.0',
    packages = find_packages(include = ('join_2*', )) + ['prophecy_config_instances.join_2'],
    package_dir = {'prophecy_config_instances.join_2' : 'configs/resources/join_2'},
    package_data = {'prophecy_config_instances.join_2' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.0.11'],
    entry_points = {
'console_scripts' : [
'main = join_2.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
