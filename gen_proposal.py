#encoding=utf-8
import os

base_dir = './proposal/'
files = os.listdir(base_dir)
md_files = filter(lambda x : x.endswith('.md') and x[0].isdigit(), files)

out = open(base_dir + 'proposal.md', 'w')
for md_file in md_files:
    fobj = open(base_dir + md_file, 'r')
    for line in fobj:
        line = line.decode('utf-8').encode('utf-8')
        out.write(line)
    out.write('\n\n\n')
    fobj.close()

out.close()

