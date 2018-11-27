test = {
  'name': 'question 7.5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(string1) == str
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(string1) 
          123
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> type(word_is_in_text) == list
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>>  word_is_in_text == [True, False, False, True]
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> type(string2) == str
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(string2) 
          115
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 'the' in string2 
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> string2[31:34] == string2[74:77] == string2[89:92] == string2[100:103] == ' a '
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> type(string3) == str
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(string3) 
          98
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> string3[60] == '_' 
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> string3[68:75] == ' the im'
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}