#!/usr/bin/env python3

import pathlib, os
import shutil

if __name__ == '__main__':
    pwd = os.getcwd()
    files = [f for f in os.listdir(pwd) if os.path.isfile(os.path.join(pwd, f))]
    md_files = [f for f in files if f[-2:] == 'md']
    md_basenames = [f[0:f.find('.')] for f in md_files]
    for (md_file, basename) in zip(md_files, md_basenames):
        dst = os.path.join(pwd, basename)
        dst_file = os.path.join(dst, 'index.md')
        src = os.path.join(pwd, md_file)
        os.makedirs(os.path.join(pwd, basename), exist_ok=True)
        shutil.move(src, dst_file)
        # print(f"will create {dst_file} and move {src} there")
