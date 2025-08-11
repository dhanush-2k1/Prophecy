from setuptools import setup, find_packages
setup(
    name = 'script',
    version = '1.0',
    packages = find_packages(include = ('script*', )) + ['prophecy_config_instances.script'],
    package_dir = {'prophecy_config_instances.script' : 'configs/resources/script'},
    package_data = {'prophecy_config_instances.script' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.0.11'],
    entry_points = {
'console_scripts' : [
'main = script.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
