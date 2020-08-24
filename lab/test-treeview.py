import tkinter as tk
from tkinter import ttk

def itemClicked(val):
    print(val.widget.selection())
    print(tree.item(val.widget.selection())['text'])

master = tk.Tk()

tree = ttk.Treeview(master)

tree.heading("#0", text="Name", anchor=tk.W)

# Inserted at the root, program chooses id:
tree.insert('', 'end', 'widgets', text='Widget Tour')

# Same thing, but inserted as first child:
tree.insert('', 0, 'gallery', text='Applications')

# Treeview chooses the id:
id = tree.insert('', 'end', text='Tutorial')

# Inserted underneath an existing node:
tree.insert('widgets', 'end', text='Canvas')
tree.insert(id, 'end', text='Tree')

tree.bind('<<TreeviewSelect>>', itemClicked)

# tree["columns"] = ("one", "two", "three")
# tree.column("#0", width=270, minwidth=270, stretch=tk.NO)
# tree.column("one", width=150, minwidth=150, stretch=tk.NO)
# tree.column("two", width=400, minwidth=200)
# tree.column("three", width=80, minwidth=50, stretch=tk.NO)

# tree.heading("#0", text="Name", anchor=tk.W)
# tree.heading("one", text="Date modified", anchor=tk.W)
# tree.heading("two", text="Type", anchor=tk.W)
# tree.heading("three", text="Size", anchor=tk.W)

# folder1=tree.insert("", 1, "", text="Folder 1", values=("23-Jun-17 11:05","File folder",""))
# folder1 = tree.insert(
#     "", 1, "", text="Folder 1", values=("23-Jun-17 11:05", "File folder", "")
# )
# tree.insert(
#     "", 2, "", text="text_file.txt", values=("23-Jun-17 11:25", "TXT file", "1 KB")
# )
# # Level 2
# tree.insert(
#     folder1,
#     "end",
#     "",
#     text="photo1.png",
#     values=("23-Jun-17 11:28", "PNG file", "2.6 KB"),
# )
# tree.insert(
#     folder1,
#     "end",
#     "",
#     text="photo2.png",
#     values=("23-Jun-17 11:29", "PNG file", "3.2 KB"),
# )
# tree.insert(
#     folder1,
#     "end",
#     "",
#     text="photo3.png",
#     values=("23-Jun-17 11:30", "PNG file", "3.1 KB"),
# )

tree.pack(side=tk.TOP, fill=tk.X)

master.mainloop()
