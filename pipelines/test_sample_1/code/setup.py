from setuptools import setup, find_packages
setup(
    name = 'test_sample_1',
    version = '1.0',
    packages = find_packages(include = ('test_sample_1*', )) + ['prophecy_config_instances.test_sample_1'],
    package_dir = {'prophecy_config_instances.test_sample_1' : 'configs/resources/test_sample_1'},
    package_data = {'prophecy_config_instances.test_sample_1' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.0.11'],
    entry_points = {
'console_scripts' : [
'main = test_sample_1.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
