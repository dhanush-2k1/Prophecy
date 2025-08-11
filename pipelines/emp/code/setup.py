from setuptools import setup, find_packages
setup(
    name = 'emp',
    version = '1.0',
    packages = find_packages(include = ('emp*', )) + ['prophecy_config_instances.emp'],
    package_dir = {'prophecy_config_instances.emp' : 'configs/resources/emp'},
    package_data = {'prophecy_config_instances.emp' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.0.11'],
    entry_points = {
'console_scripts' : [
'main = emp.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
