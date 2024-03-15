import os
from tree_to_data import *

# create parsed tree data file
TREE = parse_tree(os.path.join('..', 'data', 'tree.csv'))

# leaf node list
LEAF_NODES = list(map(lambda x: x['path_num'], list(filter(lambda x: x['last'], TREE))))

# all full paths
ALL_PATHS = list(map(lambda x: x['path'], TREE))

# method to look for items in a tree
def find_by(by, value):
    result = list(filter(lambda x: x[by]==value, TREE))
    return result[0] if len(result) == 1 else None if len(result) == 0 else result

# correct path definitions
CORRECT_PATHS = {
    1: list(map(lambda x: find_by('path', x)['path_num'],['trending', 'trending->popular-articles'])),
    2: list(map(lambda x: find_by('path', x)['path_num'],['entertainment', 'entertainment->films', 'entertainment->films->genres', 'entertainment->films->genres->comedy'])),
    3: list(map(lambda x: find_by('path', x)['path_num'],['entertainment', 'entertainment->cinema', 'entertainment->cinema->cinemas-near-you'])),
    4: list(map(lambda x: find_by('path', x)['path_num'],['hobbies', 'hobbies->sports', 'hobbies->sports->individual-sports', 'hobbies->sports->individual-sports->boxing'])),
    5: list(map(lambda x: find_by('path', x)['path_num'],['hobbies', 'hobbies->food', 'hobbies->food->regional-cuisine', 'hobbies->food->regional-cuisine->mexican-cuisine'])), 
    6: list(map(lambda x: find_by('path', x)['path_num'],['culture', 'culture->fashion', 'culture->fashion->new-collections'])),
    7: list(map(lambda x: find_by('path', x)['path_num'],['culture', 'culture->history', 'culture->history->medieval'])),
    8: list(map(lambda x: find_by('path', x)['path_num'],['science', 'science->technology', 'science->technology->computers-and-internet'])),
    9: list(map(lambda x: find_by('path', x)['path_num'],['science', 'science->nature', 'science->nature->animals'])),
    10: list(map(lambda x: find_by('path', x)['path_num'],['society', 'society->health', 'society->health->health-issues'])),
    11: list(map(lambda x: find_by('path', x)['path_num'],['society', 'society->family-and-relationships', 'society->family-and-relationships->parenting'])),
}