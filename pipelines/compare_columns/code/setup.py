from setuptools import setup, find_packages
setup(
    name = 'compare_columns',
    version = '1.0',
    packages = find_packages(include = ('compare_columns*', )) + ['prophecy_config_instances.compare_columns'],
    package_dir = {'prophecy_config_instances.compare_columns' : 'configs/resources/compare_columns'},
    package_data = {'prophecy_config_instances.compare_columns' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.0.11'],
    entry_points = {
'console_scripts' : [
'main = compare_columns.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
