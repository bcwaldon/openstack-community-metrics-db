from distutils.core import setup

setup(name='openstack-community-metrics',
      version='0.1',
      description='Python wrapper around OpenStack community metrics db',
      author='Brian Waldon',
      author_email=' bcwaldon@gmail.com',
      packages=['ocm'],
      install_requires=['sqlalchemy'],
)
