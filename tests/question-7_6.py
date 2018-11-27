test = {
  'name': 'question 7.6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(read_densities_join) == types.FunctionType
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(param_j)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(read_densities_substrings) == types.FunctionType
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(param_s)
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': """
import inspect, types
param_j = inspect.signature(read_densities_join).parameters
param_s = inspect.signature(read_densities_substrings).parameters
""",
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> type(d_join) == dict
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(d_substrings) == dict
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(d_join) == len(d_substrings) == 19
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': """
f='data/densities.dat';
d_join=read_densities_join(f);
d_substrings=read_densities_substrings(f)
""",
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> sorted(list(d_join.keys()))
          ['Earth core', 'Earth mean', 'Moon', 'Sun core', 'Sun mean', 'air', 'gasoline', 'gold', 'granite', 'human body', 'ice', 'iron', 'limestone', 'mercury', 'platinium', 'proton', 'pure water', 'seawater', 'silver']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len([1 for k in d_join if k in d_substrings and d_join[k]==d_substrings[k]]) == len(d_join)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': """
f='data/densities.dat';
d_join=read_densities_join(f);
d_substrings=read_densities_substrings(f)
""",
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
