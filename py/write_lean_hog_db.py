from os import listdir
from os.path import isfile, join

import hog_parser

# after generating the db files, run "lean --make db_test_main.lean "

# the invariants should have the same order as in the input file
# in particular, the last invariant is used in parsing as a terminating condition

ids = ['0-8', '9-11', '12-19', '20-21', '22', '23', '24', '25-26', '27', '28', '29', 
       '30-regular', '30-nonregular-1', '30-nonregular-2',
       '31-33', '34', '35-41', '42-43', '44-49', '50-99',
       '100-149', '150-189', '190-209', '210-']
files = list(map(lambda x: (f'etc/hog-order-{x}-inv.txt', f'etc/hog-order-{x}-g6.txt'), ids))

settings = {
    'structure_path': 'py/hog_invariants.json',
    'inputs': files,
    'output_path': 'src/hog/out',
    'db_name': 'db_test',
    'write_floats': False,
    'total_graphs': 99999, # use for estimating the number of files needed
    'graphs_per_file': 1000,
    'graphs_per_line': 10,
    'limit': 0
    # before 2D list, limit: 2690
}

hog = hog_parser.HoGParser(settings)

# hog.write_lean_structure()
hog.write_lean_files()