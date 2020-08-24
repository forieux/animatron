import os
from pathlib import Path

tree = [(Path("./demos"), [])]
for path in sorted(tree[0][0].iterdir()):
    if path.is_file() and path.suffix == ".py":
        tree[0][1].append(path)
    elif path.is_dir():
        tree.append((path, []))
        for pathb in path.iterdir():
            if pathb.is_file() and pathb.suffix == ".py":
                tree[-1][1].append(pathb)

tree = [t for t in tree if len(t[1]) != 0]

# print(list(path.parents)[:-2])
# # for par in list(path.parents):
# #     tree[par].append(path)

# tree.extend(list(path.parents)[:-2])
# if len(path.parts[2:]) > 1:
#     for part in path.parts[2:-1]:
#         tree["part"] = {}
#         print(part)


for e in tree:
    print(e[0], e[1])
# print(sorted(set([t.stem for t in tree])))

# def insert_tree(tree, key, subdirs, filelist):
#     if subdirs == []:
#         tree[key] = filelist
#     else:
#         for sdir in subdirs:
#             insert_tree(tree, Path(sdir).stem,

# tree = {}
# for name, subdirs, files in os.walk("./demos"):
#     if subdirs == []
#     tree["."] = files
#     for sdir in subdirs:
#         tree[sdir] = {}
