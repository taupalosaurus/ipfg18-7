test = {
  'name': 'question 7.3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(d1) == dict
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(d1) == 8
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len([1 for k,v in items if k in d1 and d1[k]==v]) == len(d1)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': """
d1 = read_constants('data/constants.txt')
keys = ['gravitational constant', 'Boltzmann constant', 'speed of light', 'Planck constant', 'electron mass', 'Avogadro number', 'elementary charge', 'proton mass']
values = [6.67259e-11, 1.380658e-23, 299792458.0, 6.6260755e-34, 9.1093897e-31, 6.0221367e+23, 1.60217733e-19, 1.6726231e-27]
items = zip(keys, values)
""",
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
