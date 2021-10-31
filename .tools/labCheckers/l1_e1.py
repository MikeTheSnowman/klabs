#!/usr/bin/python3
schema = {
    'name': {
        'required': True,
        'type': 'string'
    },
    'date': {
        'required': True,
        'type': 'date'
    },
    'metrics': {
        'required': True,
        'type': 'dict',
        'schema': {
            'percentage': {
                'required': True,
                'type': 'dict',
                'schema': {
                    'value': {
                        'required': True,
                        'type': 'number',
                        'min': 0,
                        'max': 100
                    },
                    'trend': {
                        'type': 'string',
                        'nullable': True,
                        'regex': '^(?i)(down|equal|up)$'
                    }
                }
            }
        }
    }
}

import checker_common as C
import sys

if __name__ == "__main__":
    startMsg = "Checking your work for Lab-1, Exercise-1..."
    print(startMsg)
    C.checker(schema, sys.argv[1])