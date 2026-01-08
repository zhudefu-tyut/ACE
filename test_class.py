from abaqus import *
from odbAccess import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
import displayGroupOdbToolset as dgo
from time import time
import os

def ICE_Main(modelName,partName,CreatPart,NewPartName,Addtype,fileName,PickEleFace=[]):
    if CreatPart == 'no' and Addtype == 'ALL EleFace':
        non_repeat_list, elements_tuples, list_be0, edge_shouji =information_handler_AllEleFace_no(modelName,partName)
        create_newpart_no(modelName, partName, edge_shouji, non_repeat_list, list_be0)
        print('ACE Program running ends.')
    if CreatPart == 'no' and Addtype == 'select':
        non_repeat_list, elements_tuples, list_be0, edge_shouji = information_handler_select_no(PickEleFace)
        create_newpart_no(modelName, partName, edge_shouji, non_repeat_list, list_be0)
        print('ACE Program running ends.')
    if CreatPart == 'no' and Addtype == 'all geo face, form inp:':
        non_repeat_list, elements_tuples, list_be0, edge_shouji = information_handler_all_geo_face_no(fileName)
        create_newpart_no(modelName, partName, edge_shouji, non_repeat_list, list_be0)
        print('ACE Program running ends.')
    if CreatPart == 'yes' and Addtype == 'ALL EleFace':
        modelName, partName, non_repeat_list, elements_tuples, list_be0, edge_shouji = information_handler_AllEleFace_yes(
            modelName, partName , NewPartName)
        create_newpart_no(modelName, partName, edge_shouji, non_repeat_list, list_be0)
        print('ACE Program running ends.')
    if CreatPart == 'yes' and Addtype == 'select':
        modelName, partName, non_repeat_list, elements_tuples, list_be0, edge_shouji = information_handler_select_yes(
            PickEleFace, modelName, partName, NewPartName)
        create_newpart_no(modelName, partName, edge_shouji, non_repeat_list, list_be0)
        print('ACE Program running ends.')
    if CreatPart == 'yes' and Addtype == 'all geo face, form inp:':
        modelName, partName, non_repeat_list, elements_tuples, list_be0, edge_shouji = information_handler_all_geo_face_yes(
            modelName, partName, fileName, NewPartName)
        create_newpart_no(modelName, partName, edge_shouji, non_repeat_list, list_be0)
        print('ACE Program running ends.')
    return True

def information_handler_all_geo_face_no(fileName):
    non_repeat_list = collect_and_convert_node_tags(fileName)
    elements_tuples = extract_and_convert_elements(fileName)
    list_be0 = [tuple(x - 1 for x in t) for t in elements_tuples]
    edge_shouji = edge_shouji_methon(elements_tuples)
    return non_repeat_list, elements_tuples, list_be0, edge_shouji

def information_handler_all_geo_face_yes(modelName, partName,fileName,NewPartName):
    non_repeat_list = collect_and_convert_node_tags(fileName)
    elements_tuples = extract_and_convert_elements(fileName)
    list_be0 = [tuple(x - 1 for x in t) for t in elements_tuples]
    edge_shouji = edge_shouji_methon(elements_tuples)

    p = mdb.models['Model-1'].Part(name='%s' %NewPartName,
                                   objectToCopy=mdb.models['Model-1'].parts['%s' %partName])

    partName = '%s' % NewPartName
    return modelName, partName, non_repeat_list, elements_tuples, list_be0, edge_shouji

def information_handler_select_no(PickEleFace):
    a = PickEleFace
    elements_tuples = []
    unique_nodes = set()

    for edge in a:
        nodes = edge.getNodes()
        node_tuple = (nodes[0].label, nodes[1].label)
        elements_tuples.append(node_tuple)
        unique_nodes.update(node_tuple)
    non_repeat_list = sorted(list(unique_nodes))
    list_be0 = [tuple(x - 1 for x in t) for t in elements_tuples]
    edge_shouji = edge_shouji_methon(elements_tuples)
    return non_repeat_list,elements_tuples,list_be0, edge_shouji

def information_handler_select_yes(PickEleFace, modelName,partName,NewPartName):
    model = mdb.models['%s' % modelName]
    part = model.parts['%s' % partName]

    a = PickEleFace
    elements_tuples = []
    unique_nodes = set()

    for edge in a:
        nodes = edge.getNodes()
        node_tuple = (nodes[0].label, nodes[1].label)
        elements_tuples.append(node_tuple)
        unique_nodes.update(node_tuple)
    non_repeat_list = sorted(list(unique_nodes))
    list_be0 = [tuple(x - 1 for x in t) for t in elements_tuples]
    edge_shouji = edge_shouji_methon(elements_tuples)

    part.PartFromMesh(name='%s' % NewPartName, copySets=True)
    partName = '%s' % NewPartName
    return modelName,partName,non_repeat_list,elements_tuples,list_be0, edge_shouji

def information_handler_AllEleFace_yes(modelName,partName,NewPartName):
    model = mdb.models['%s' % modelName]
    part = model.parts['%s' % partName]
    unique_nodes = set()

    a = part.edges[:]
    elements_tuples_boundary = []
    for edge in a:
        nodes = edge.getNodes()
        for i in range(len(nodes)-1):
            node_tuple = (nodes[i].label, nodes[i+1].label)
            elements_tuples_boundary.append(node_tuple)

    a = part.elementEdges[:]
    elements_tuples_all = []
    for edge in a:
        nodes = edge.getNodes()
        node_tuple = (nodes[0].label, nodes[1].label)
        elements_tuples_all.append(node_tuple)

    set1 = {tuple(sorted(t)) for t in elements_tuples_boundary}
    elements_tuples = [t for t in elements_tuples_all if tuple(sorted(t)) not in set1]
    for nodetup in elements_tuples:
        unique_nodes.update(nodetup)
    non_repeat_list = sorted(list(unique_nodes))
    list_be0 = [tuple(x - 1 for x in t) for t in elements_tuples]
    edge_shouji = edge_shouji_methon(elements_tuples)

    part.PartFromMesh(name='%s' %NewPartName, copySets=True)
    partName = '%s' %NewPartName
    return modelName,partName,non_repeat_list,elements_tuples,list_be0, edge_shouji

def information_handler_AllEleFace_no(modelName,partName):
    model = mdb.models['%s' % modelName]
    part = model.parts['%s' % partName]
    unique_nodes = set()

    a = part.elements.getExteriorEdges()
    elements_tuples_boundary = []
    for edge in a:
        nodes = edge.getNodes()
        for i in range(len(nodes) - 1):
            node_tuple = (nodes[i].label, nodes[i + 1].label)
            elements_tuples_boundary.append(node_tuple)

    a = part.elementEdges[:]
    elements_tuples_all = []
    for edge in a:
        nodes = edge.getNodes()
        node_tuple = (nodes[0].label, nodes[1].label)
        elements_tuples_all.append(node_tuple)

    set1 = {tuple(sorted(t)) for t in elements_tuples_boundary}
    elements_tuples = [t for t in elements_tuples_all if tuple(sorted(t)) not in set1]
    print(elements_tuples_boundary)
    for nodetup in elements_tuples:
        unique_nodes.update(nodetup)
    non_repeat_list = sorted(list(unique_nodes))
    list_be0 = [tuple(x - 1 for x in t) for t in elements_tuples]
    edge_shouji = edge_shouji_methon(elements_tuples)
    return non_repeat_list,elements_tuples,list_be0, edge_shouji

def collect_and_convert_node_tags(file_path):
    non_repeat_list = []
    node_tags_geted_list = []
    int_list_1 = []
    seen = set()
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

    for s in node_tags_geted_list:
        s = s.strip().rstrip(',')
        split_strings = s.split(',')
        int_list_1.extend([int(item) for item in split_strings])
    int_list_1.sort()

    for x in int_list_1:
        if x not in seen:
            seen.add(x)
            non_repeat_list.append(x)

    return non_repeat_list

def extract_and_convert_elements(file_path):
    elements_tuples = []
    start_extracting = False

    with open(file_path, 'r') as file:
        lines = file.readlines()
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
                elements_tuples.append(tuple_1)
            except ValueError:
                continue
        if not line or line.startswith('*ELSET'):
            start_extracting = False

    return elements_tuples

def edge_shouji_methon(elements_tuples):
    edge_shouji = {}

    for tup in elements_tuples:
        for num in tup:
            if num not in edge_shouji:
                edge_shouji[num] = []
            py_0 = tuple(number - 1 for number in tup)
            edge_shouji[num].append(py_0)
    return edge_shouji

def create_newpart_no(modelName, partName, edge_shouji, non_repeat_list, list_be0):
    dict2, dict3, element_coonectivity_modify = create_nodes(modelName, partName, edge_shouji, non_repeat_list,
                                                             list_be0)
    result_list = create_coelement(dict2, dict3)
    modify_and_create_element(modelName, partName,element_coonectivity_modify, result_list)
    return None

def create_newpart_yes(modelName, partName, NewPartName):
    print(modelName)
    print(partName)
    print(NewPartName)

def create_nodes(modelName,partName, edge_shouji,non_repeat_list,list_be0):
    model = mdb.models['%s' % modelName]
    part = model.parts['%s' % partName]

    int_1 = -1
    infomation = {}
    element_coonectivity_modify = {}
    dict2 = {tup: {} for tup in list_be0}
    dict3 = {}
    for i in non_repeat_list:
        i_1 = i-1
        element_coonectivity = {}
        infomation[i]= {}
        element_near = part.nodes[i_1].getElements()
        infomation[i]['abaqus_elements'] = element_near
        for ele in infomation[i]['abaqus_elements']:
            if ele.label not in element_coonectivity_modify:
                element_coonectivity_modify[ele.label] = ele.connectivity
        for ele in infomation[i]['abaqus_elements']:
            element_coonectivity[ele.label] = ele.connectivity

        edge_yuanzu = edge_shouji[i]
        unique_numbers = set()
        for tup in edge_yuanzu:
            for num in tup:
                unique_numbers.add(num)
        unique_numbers_list = list(unique_numbers)
        list3 = process_dict_and_list(element_coonectivity, unique_numbers_list)
        list4 = merge_common_tuples(list3)
        node_created = []
        node_created.append(i_1)
        count_num = len(list4)-1
        for num_a in range(count_num):
            coord = part.nodes[i_1].coordinates
            node = part.Node(coordinates=coord)
            node_created.append(node.label-1)
        dict_from_lists = {num: tup for num, tup in zip(node_created, list4)}
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
        for value in list_be0:
            for dict1_key, dict1_value in element_coonectivity.items():
                dict1_value_tuple = tuple(dict1_value)
                if all(x in dict1_value_tuple for x in value):
                    new_tuples = [(dict1_value[i], dict1_value[(i + 1) % len(dict1_value)]) for i in
                                    range(len(dict1_value))]
                    for new_tuple in new_tuples:
                        for val2 in list_be0:
                            if new_tuple == val2:
                                if value not in dict3:
                                    dict3[value] = {'b': dict1_key}
                                else:
                                    dict3[value]['b'] = dict1_key
                                break
    return dict2,dict3,element_coonectivity_modify

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

    return list3

def merge_common_tuples(list3):
    num_to_indices = {}
    for index, tup in enumerate(list3):
        for num in tup:
            if num not in num_to_indices:
                num_to_indices[num] = []
            num_to_indices[num].append(index)
    merged_indices = set()
    result = []
    for index, tup in enumerate(list3):
        if index in merged_indices:
            continue
        common_nums = [num for num in tup if len(num_to_indices[num]) > 1]
        if common_nums:
            merged_tuple = set(tup)
            for num in common_nums:
                for i in num_to_indices[num]:
                    if i != index and i not in merged_indices:
                        merged_tuple.update(list3[i])
                        merged_indices.add(i)
            result.append(tuple(merged_tuple))
        else:
            result.append(tup)
            merged_indices.add(index)

    return result

def create_coelement(dict2,dict3):
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
    return result_list

def modify_and_create_element(modelName,partName,element_coonectivity_modify,result_list):
    model = mdb.models['%s' % modelName]
    part = model.parts['%s' % partName]
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

