import csv, json

def get_order(row):
    for i, s in enumerate(row):
        if(s != ''):
            return i
        
def parse_tree(file_path, create_file=False):
    contents = []

    with open(file_path) as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            contents.append(row)

    contents = contents[1:]

    data = []

    r0 = -1
    r1 = -1
    r2 = -1
    r3 = -1

    r0_str = ''
    r1_str = ''
    r2_str = ''
    r3_str = ''

    for index, row in enumerate(contents):
        order = get_order(row)
        row_id = row[order].lower().replace(' ', '-')
        num_path = ''
        id_path = ''

        if(order == 0):
            r0, r1, r2, r3 = r0+1, -1, -1, -1
            r0_str = row_id
            num_path = str(r0)
            id_path = r0_str
        if(order == 1):
            r1, r2, r3 = r1+1, -1, -1
            r1_str = row_id
            num_path = str(r0) + '-' + str(r1)
            id_path = r0_str + '->' + r1_str
        if(order == 2):
            r2, r3 = r2+1, -1
            r2_str = row_id
            num_path = str(r0) + '-' + str(r1) + '-' + str(r2)
            id_path = r0_str + '->' + r1_str + '->' + r2_str
        if(order == 3):
            r3 = r3+1
            r3_str = row_id
            num_path = str(r0) + '-' + str(r1) + '-' + str(r2)+ '-' + str(r3)
            id_path = r0_str + '->' + r1_str + '->' + r2_str + '->' + r3_str

        data.append({
            'id': index,
            'name_path': row_id,
            'path': id_path,
            'path_num': num_path,
            'name': row[order],
            'last': index == len(contents)-1 or get_order(contents[index+1]) <= order
        })

    if(create_file):
        with open('parsed-tree.json', 'w') as file:
            file.write(json.dumps(data))
    
    return data