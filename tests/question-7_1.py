test = {
  'name': 'question 7.1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(density)==dict
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(density) 
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
        'code': r"""
          >>> np.isclose(density["diamond"], 3500)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
        'code': r"""
          >>> np.isclose(density["quartz"], 2650)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
        'code': r"""
          >>> np.isclose(density["clay"], 2580)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
        'code': r"""
          >>> np.isclose(density["water"], 1000)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import numpy as np',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> type(moduli)==dict
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(moduli)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
        'code': r"""
          >>> np.allclose(moduli["diamond"], (455., 540.))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
        'code': r"""
          >>> np.allclose(moduli["quartz"], (44., 38.))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
        'code': r"""
          >>> np.allclose(moduli["clay"], (6.85, 20.9))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
        'code': r"""
          >>> np.allclose(moduli["water"], (0., 2.29))
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import numpy as np',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> np.isclose(density_average, 2432.5)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import numpy as np',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> np.isclose(shear_mod_average, 126.4625)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(bulk_mod_average, 150.29749999999999)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import numpy as np',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}