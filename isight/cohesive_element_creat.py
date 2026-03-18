# -*- coding: utf-8 -*-
from abaqus import *
from abaqusConstants import *
import re

model = mdb.models['Model-1']
part = model.parts['PART-1']

file_path = "D:\Work_Directory_new\information.inp"
node_tags_geted_list = []
collecting = False

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith("*NSET,NSET=line"):
            collecting = True
            continue
        if collecting and not line.startswith('*'):
            node_tags_geted_list.append(line)
        if collecting and line.startswith('*'):
            collecting = False

int_list = []
for s in node_tags_geted_list:
    s = s.strip().rstrip(',')
    split_strings = s.split(',')
    int_list.extend([int(item) for item in split_strings])

int_list.sort()

seen = set()
non_repeat_list = []
for x in int_list:
    if x not in seen:
        seen.add(x)
        non_repeat_list.append(x)

with open('D:\Work_Directory_new\information.inp', 'r') as file:
    lines = file.readlines()
tuples_list = []
start_extracting = False
for line in lines:
    line = line.strip()
    if line.startswith('*'):
        if line.startswith('*ELEMENT'):
            start_extracting = True
        continue
    if start_extracting and line:
        try:
            pianduan = line.split(',')
            tuple_1 = tuple(map(int, pianduan[1:]))
            tuples_list.append(tuple_1)
        except ValueError:
            continue
    if not line or line.startswith('*ELSET'):
        start_extracting = False
#print(tuples_list)
new_list = [tuple(x - 1 for x in t) for t in tuples_list]

def process_dict_and_list(data_dict, target_list):
    list2 = []
    list3 = []

    for key1, value1 in data_dict.items():
        if key1 in list2:
            continue

        for key2, value2 in data_dict.items():
            if key1 != key2:
                intersection = set(value1) & set(value2)

                if intersection and not intersection.issubset(set(target_list)):
                    if key1 not in list2:
                        list2.append(key1)
                    if key2 not in list2:
                        list2.append(key2)
                    tuple_to_add = (key1, key2) if (key1, key2) not in list3 else None
                    if tuple_to_add is not None:
                        list3.append(tuple_to_add)
                    break

        if key1 not in list2:
            repeated_numbers = set(value1) & set(target_list)
            if repeated_numbers.issubset(set(target_list)):
                list2.append(key1)
                tuple_to_add = (key1,)
                if not any(key1 in t for t in list3):
                    list3.append(tuple_to_add)

    return list2, list3

def merge_common_tuples(tuples_list):
    num_to_indices = {}
    for index, tup in enumerate(tuples_list):
        for num in tup:
            if num not in num_to_indices:
                num_to_indices[num] = []
            num_to_indices[num].append(index)

    merged_indices = set()
    result = []

    for index, tup in enumerate(tuples_list):
        if index in merged_indices:
            continue

        common_nums = [num for num in tup if len(num_to_indices[num]) > 1]
        if common_nums:
            merged_tuple = set(tup)
            for num in common_nums:
                for i in num_to_indices[num]:
                    if i != index and i not in merged_indices:
                        merged_tuple.update(tuples_list[i])
                        merged_indices.add(i)
            result.append(tuple(merged_tuple))
        else:
            result.append(tup)
            merged_indices.add(index)

    return result


edge_shouji={}

for tup in tuples_list:
    for num in tup:
        if num not in edge_shouji:
            edge_shouji[num] = []
        py_0 = tuple(number - 1 for number in tup)
        edge_shouji[num].append(py_0)

#print(edge_shouji)
int_1 = -1
constructed_strings = []
infomation = {}
element_coonectivity_modify = {}
dict3 = {}
dict2 = {tup: {} for tup in new_list}
for i in non_repeat_list:
    i_1 = i-1
    element_coonectivity = {}
    infomation[i]= {}
    #constructed_string = "mdb.models['Model-1'].parts['PART-1'].nodes[%s]" % str(i_1)
    #constructed_strings.append(constructed_string)
    #infomation[i]['abaqus_node'] = constructed_string
    element_near = part.nodes[i_1].getElements()
    infomation[i]['abaqus_elements'] = element_near
    for ele in infomation[i]['abaqus_elements']:
        if ele.label not in element_coonectivity_modify:
            element_coonectivity_modify[ele.label] = ele.connectivity
    for ele in infomation[i]['abaqus_elements']:
        element_coonectivity[ele.label] = ele.connectivity
    #print(element_coonectivity)
    edge_yuanzu = edge_shouji[i]
    unique_numbers = set()
    for tup in edge_yuanzu:
        for num in tup:
            unique_numbers.add(num)
    unique_numbers_list = list(unique_numbers)
    #print(unique_numbers_list)
    list2, list3 = process_dict_and_list(element_coonectivity, unique_numbers_list)
    #print("List2:", list2)
    #print("List3:", list3)
    list4 = merge_common_tuples(list3)
    #print(list4)
    node_created = []
    node_created.append(i_1)
    count_num = len(list4)-1
    #print(count_num)
    for num_a in range(count_num):
        coord = part.nodes[i_1].coordinates
        node = part.Node(coordinates=coord)
        node_created.append(node.label-1)
    #print(node_created)
    dict_from_lists = {num: tup for num, tup in zip(node_created, list4)}
    #print(dict_from_lists)
    for key1, value1 in dict_from_lists.items():
        for a in value1:
            if a in element_coonectivity_modify:
                element_coonectivity_modify[a] = tuple(key1 if x == i_1 else x for x in element_coonectivity_modify[a])
    for tup in edge_shouji[i]:
        if tup in dict2:
            for key1, value in element_coonectivity.items():
                if all(num in value for num in tup):
                    if key1:
                        key2 = [k for k, v in dict_from_lists.items() if key1 in v]
                        if key2:
                            if key1 not in dict2[tup]:
                                dict2[tup][key1] = []
                            dict2[tup][key1].append(key2)
    for value in new_list:
        for dict1_key, dict1_value in element_coonectivity.items():
            dict1_value_tuple = tuple(dict1_value)
            if all(x in dict1_value_tuple for x in value):
                new_tuples = [(dict1_value[i], dict1_value[(i + 1) % len(dict1_value)]) for i in
                                range(len(dict1_value))]
                for new_tuple in new_tuples:
                    for val2 in new_list:
                        if new_tuple == val2:
                            if value not in dict3:
                                dict3[value] = {'b': dict1_key}
                            else:
                                dict3[value]['b'] = dict1_key
                            break

result_list = []
for key, subdict in dict2.items():
    priority_key = dict3[key]['b']
    result = []
    if priority_key in subdict:
        result.extend(subdict[priority_key][1])
        result.extend(subdict[priority_key][0])
    for subkey in sorted(subdict.keys()):
        if subkey != priority_key:
            result.extend(subdict[subkey][0])
            result.extend(subdict[subkey][1])
    result_list.append(tuple(result))


for key, subdict in element_coonectivity_modify.items():
    value_list = list(subdict)
    if len(value_list) == 4:
        ele_delete = part.elements.getFromLabel(label=key)
        part.deleteElement(ele_delete)
        KNODE_2 = []
        for a in value_list:
            node1 = part.nodes[a]
            KNODE_2.append(node1)
        part.Element(nodes=KNODE_2, elemShape=QUAD4)
    if len(value_list) == 3:
        ele_delete = part.elements.getFromLabel(label=key)
        part.deleteElement(ele_delete)
        KNODE_1 = []
        for a in value_list:
            node1 = part.nodes[a]
            KNODE_1.append(node1)
        part.Element(nodes=KNODE_1, elemShape=TRI3)
cohesiveEleLabel = []
for tup in result_list:
    value_list = list(tup)
    KNODE_3 = []
    for a in value_list:
        node1 = part.nodes[a]
        KNODE_3.append(node1)
    ele = part.Element(nodes=KNODE_3, elemShape=QUAD4)
    cohesiveEleLabel.append(ele.label)
    part.Set(elements=part.elements.sequenceFromLabels(cohesiveEleLabel), name='Set-cohesive')

#print(dict3)
#print(dict2)
#print(infomation)
#print(element_coonectivity_modify)


