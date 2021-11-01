#!/usr/bin/python3
schema = {
    'string_with_quotes': {
        'required': True,
        'type': 'string'
    }
    # 'metrics': {
    #     'required': True,
    #     'type': 'dict',
    #     'schema': {
    #         'percentage': {
    #             'required': True,
    #             'type': 'dict',
    #             'schema': {
    #                 'value': {
    #                     'required': True,
    #                     'type': 'number',
    #                     'min': 0,
    #                     'max': 100
    #                 },
    #                 'trend': {
    #                     'type': 'string',
    #                     'nullable': True,
    #                     'regex': '^(?i)(down|equal|up)$'
    #                 }
    #             }
    #         }
    #     }
    #}
}

import checker_common as C
import sys
if __name__ == "__main__":
    C.checker(schema, sys.argv[1])