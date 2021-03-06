test = {
  'name': 'question 7.4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(triangle_area_list) == types.FunctionType
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(param)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(triangle_area_list([[0,0], [1,0], [0,2]]), 1.)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(triangle_area_list([[0,0], [2,1], [0,3]]), 3.)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(triangle_area_list([[0,0], [1,0], [0,1]]), 0.5)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': """
import numpy as np, inspect, types
param = inspect.signature(triangle_area_list).parameters
""",
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> type(triangle_area_dict) == types.FunctionType
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(param)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(triangle_area_dict({1: (0,0), 2: (1,0), 3: (0,2)}), 1.)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(triangle_area_dict({1: (0,0), 2: (2,1), 3: (0,3)}), 3.)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(triangle_area_dict({1: (0,0), 2: (1,0), 3: (0,1)}), 0.5)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': """
import numpy as np, inspect, types
param = inspect.signature(triangle_area_dict).parameters
""",
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
