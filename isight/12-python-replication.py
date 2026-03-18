# -*- coding: utf-8 -*-
"""
copy_with_batch.py

"""

import os
import shutil
import sys
import importlib.util
import re

SRC_DIR = 'D:\Work_Directory_new'
DST_ROOT = 'E:\work_new_cundang'
CONFIG_FILE = 'bianliang.txt'
PARAM_NAME = 'kuan'
COUNTER_FILE = os.path.join(DST_ROOT, '.counter')
# ====================================

def extract_param_from_py(file_path, param_name):
    pattern = re.compile(
        r'^\s*' + re.escape(param_name) +
        r'\s*=\s*('
        r'-?\d+(?:\.\d+)?|'          
        r'["\'].*?["\']'              
        r')',
        re.MULTILINE
    )
    with open(file_path, encoding='utf-8') as f:
        content = f.read()
    m = pattern.search(content)
    if not m:
        raise ValueError(f'在 {file_path} not found：{param_name}')

    raw = m.group(1).strip()
    if raw[0] in {'"', "'"} and raw[-1] == raw[0]:
        return raw[1:-1]
    try:
        return int(raw)
    except ValueError:
        return float(raw)

def get_next_batch_id():
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, 'r', encoding='utf-8') as f:
            count = int(f.read().strip())
    else:
        count = 0
    next_count = count + 1
    with open(COUNTER_FILE, 'w', encoding='utf-8') as f:
        f.write(str(next_count))
    return count

def copy_files():
    config_path = os.path.join(SRC_DIR, CONFIG_FILE)
    if not os.path.isfile(config_path):
        sys.exit(f'not found：{config_path}')
    param = extract_param_from_py(config_path, PARAM_NAME)

    batch_id = get_next_batch_id()
    dst_dir = os.path.join(DST_ROOT, f'batch{batch_id}_{param}')
    os.makedirs(dst_dir, exist_ok=True)

    for fname in os.listdir(SRC_DIR):
        src_file = os.path.join(SRC_DIR, fname)
        if os.path.isfile(src_file):
            shutil.copy2(src_file, dst_dir)
    print(f'done：{dst_dir}')

    for fname in os.listdir(SRC_DIR):
        if fname.startswith('diyingli') or fname.startswith('Job-1'):
            f_path = os.path.join(SRC_DIR, fname)
            if os.path.isfile(f_path):
                os.remove(f_path)
                print(f'deleted：{f_path}')

if __name__ == '__main__':
    copy_files()