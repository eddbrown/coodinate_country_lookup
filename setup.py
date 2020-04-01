from distutils.core import setup
setup(
  name = 'coordinate_country_lookup',         # How you named your package folder (MyLib)
  packages = ['coordinate_country_lookup'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Returns the country of the latitude longitude tuple offline',   # Give a short description about your library
  author = 'Edward Brown',                   # Type in your name
  author_email = 'edward.j.e.brown@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['COORIDNATES', 'COUNTRY', 'LOOKUP'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'shapely',
          'geopandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
