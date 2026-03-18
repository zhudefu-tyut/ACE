import re

with open('information1.inp', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'^\*NSET\s*,\s*NSET\s*=\s*dingbian\s*$', text, flags=re.M | re.I)

block = text[m.end():]
block = re.split(r'^\*', block, flags=re.M)[0]

initial_tags_ding = [int(n) for n in re.findall(r'\d+', block)]

m = re.search(r'^\*NSET\s*,\s*NSET\s*=\s*dibian\s*$', text, flags=re.M | re.I)

block = text[m.end():]
block = re.split(r'^\*', block, flags=re.M)[0]

initial_tags_di = [int(n) for n in re.findall(r'\d+', block)]

tags_ding = set(initial_tags_ding)
coord_ding = []
tags_di = set(initial_tags_di)
coord_di= []

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []

in_node_section = False
in_cps3_section = False

inp_file = ("gai.inp")
with open(inp_file, 'r', encoding='utf-8') as f:
    for raw in f:
        line = raw.strip()
        if not line or line.startswith('**'):
            continue

        if line.upper().startswith('*NODE'):
            in_node_section = True
            in_cps3_section = False
            continue

        if line.upper().startswith('*ELEMENT, TYPE=CPS3'):
            in_node_section = False
            in_cps3_section = True
            continue

        if line.upper().startswith('*ELEMENT, TYPE=CPS4R'):
            in_cps3_section = False

        if in_node_section:
            parts = [p.strip() for p in line.split(',')]
            if len(parts) < 3:
                continue
            try:
                node_id = int(parts[0])
                x = float(parts[1])
                y = float(parts[2])

                if node_id in tags_di and len(coord_di) < len(initial_tags_di):
                    coord_di.append((x, y))

                if node_id in tags_ding and len(coord_ding) < len(initial_tags_ding):
                    coord_ding.append((x, y))

                if len(coord_ding) == len(initial_tags_ding):
                    if (x, y) in coord_ding:
                        tags_ding.add(node_id)

                if len(coord_di) == len(initial_tags_di):
                    if (x, y) in coord_di:
                        tags_di.add(node_id)

            except ValueError:
                continue

        if in_cps3_section:
            parts = [p.strip() for p in line.split(',')]
            if len(parts) < 4:
                continue
            try:
                elem_id = int(parts[0])
                n1 = int(parts[1])
                n2 = int(parts[2])
                n3 = int(parts[3])

                match1 = n1 in tags_ding
                match2 = n2 in tags_ding
                match3 = n3 in tags_ding
                match4 = n1 in tags_di
                match5 = n2 in tags_di
                match6 = n3 in tags_di

                match_count1 = match1 + match2 + match3
                match_count2 = match4 + match5 + match6
                if match_count1 >= 2:
                    if match1 and match2:
                        list1.append(elem_id)
                    if match2 and match3:
                        list2.append(elem_id)
                    if match1 and match3:
                        list3.append(elem_id)
                if match_count2 >= 2:
                    if match4 and match5:
                        list4.append(elem_id)
                    if match5 and match6:
                        list5.append(elem_id)
                    if match4 and match6:
                        list6.append(elem_id)
            except ValueError:
                continue

with open('gai.inp', 'r', encoding='utf-8') as f:
    lines = f.readlines()

end_part_idx = None
for idx, line in enumerate(lines):
    if line.strip().upper() == '*END PART':
        end_part_idx = idx
        break
if end_part_idx is None:
    raise ValueError('no found')

def format_line(nums):
    nums = list(map(str, nums))
    chunks = [nums[i:i+16] for i in range(0, len(nums), 16)]
    return '\n'.join(', '.join(chunk) for chunk in chunks)

insert_blocks = [
    '*Elset, elset=_Surf-q_S1, internal',
    format_line(list1),
    '*Elset, elset=_Surf-q_S2, internal',
    format_line(list2),
    '*Elset, elset=_Surf-q_S3, internal',
    format_line(list3),
    '*Surface, type=ELEMENT, name=Surf-ding',
    '_Surf-q_S1, S1',
    '_Surf-q_S2, S2',
    '_Surf-q_S3, S3',
    '*Elset, elset=_Surf-q_S4, internal',
    format_line(list4),
    '*Elset, elset=_Surf-q_S5, internal',
    format_line(list5),
    '*Elset, elset=_Surf-q_S6, internal',
    format_line(list6),
    '*Surface, type=ELEMENT, name=Surf-di',
    '_Surf-q_S4, S1',
    '_Surf-q_S5, S2',
    '_Surf-q_S6, S3'
]

new_lines = (
    lines[:end_part_idx] +
    [line + '\n' for line in insert_blocks if line] +
    lines[end_part_idx:]
)

with open('gai.inp', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)