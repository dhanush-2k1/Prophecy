from setuptools import setup, find_packages
setup(
    name = 'test_spark',
    version = '1.0',
    packages = find_packages(include = ('test_spark*', )) + ['prophecy_config_instances.test_spark'],
    package_dir = {'prophecy_config_instances.test_spark' : 'configs/resources/test_spark'},
    package_data = {'prophecy_config_instances.test_spark' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.0.11'],
    entry_points = {
'console_scripts' : [
'main = test_spark.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
