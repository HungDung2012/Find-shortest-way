import tkinter as tk
from tkinter import scrolledtext, messagebox, font
from astar import solve_and_draw

# --- GUI helpers -------------------------------------------------
def apply_colors(text_widget):
    cfg = text_widget.tag_config
    cfg("path",  foreground="green")
    cfg("wall",  foreground="#666")
    cfg("start", foreground="orange")
    cfg("goal",  foreground="red")

def color_insert(txt, solved):
    for ch in solved:
        tag = None
        if ch == '*': tag = "path"
        elif ch == '#': tag = "wall"
        elif ch == 'S': tag = "start"
        elif ch == 'G': tag = "goal"
        pos = txt.index(tk.INSERT)
        txt.insert(tk.END, ch)
        if tag:
            txt.tag_add(tag, pos, f"{pos}+1c")
# -----------------------------------------------------------------

def on_solve():
    raw = txt_in.get("1.0", tk.END)
    grid = [list(line.rstrip()) for line in raw.splitlines() if line.strip()]
    solved, err = solve_and_draw(grid)
    txt_out.configure(state="normal")
    txt_out.delete("1.0", tk.END)
    if err:
        messagebox.showerror("Maze Bot", err)
    else:
        color_insert(txt_out, solved)
    txt_out.configure(state="disabled")

# --- Build window ------------------------------------------------
root = tk.Tk()
root.title("A* Maze Bot")

mono = font.Font(family="Consolas", size=12)

tk.Label(root, text="Paste your maze then press Solve").pack(anchor="w", padx=8, pady=(8,0))
txt_in = scrolledtext.ScrolledText(root, width=40, height=10, font=mono)
txt_in.pack(padx=8, pady=4)

btn = tk.Button(root, text="Solve", command=on_solve,
                bg="#4caf50", fg="white", width=12, font=("Segoe UI", 10, "bold"))
btn.pack(pady=4)

tk.Label(root, text="Solved maze").pack(anchor="w", padx=8)
txt_out = scrolledtext.ScrolledText(root, width=40, height=10, font=mono, state="disabled")
txt_out.pack(padx=8, pady=(0,8))
apply_colors(txt_out)

root.mainloop()
