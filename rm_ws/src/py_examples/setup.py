from setuptools import find_packages, setup

package_name = 'py_examples'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kamal',
    maintainer_email='kamal@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': ["pub=py_examples.pub:main",
                            "sub=py_examples.sub:main",
                            "srv=py_examples.server:main",
                            "client=py_examples.client:main"
        ],
    },
)
