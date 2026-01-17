import tkinter as tk

root = tk.Tk()
root.title("ตารางเปลี่ยนสี 5 x 5")

selected_color = "red"

# ฟังก์ชันเปลี่ยนสีที่เลือก
def set_color(color):
    global selected_color
    selected_color = color
    color_info.config(bg=selected_color)  # อัปเดต label สี

# ฟังก์ชันเปลี่ยนสีปุ่มใน grid
def change_color(btn):
    btn.config(bg=selected_color)

# ฟังก์ชันล้างสี
def clear_grid():
    for row in buttons:
        for btn in row:
            btn.config(bg="white")

# Top frame สำหรับปุ่มสี
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

btn_r = tk.Button(frame_top, text='R', bg="red", width=5, command=lambda: set_color("red"))
btn_r.pack(side="left", padx=5)
btn_g = tk.Button(frame_top, text='G', bg="green", width=5, command=lambda: set_color("green"))
btn_g.pack(side="left", padx=5)
btn_b = tk.Button(frame_top, text='B', bg="blue", width=5, command=lambda: set_color("blue"))
btn_b.pack(side="left", padx=5)

# Label แสดงสีที่เลือก
color_info = tk.Label(root, text="", bg=selected_color, width=10, height=2, relief="ridge")
color_info.pack(pady=5)

# Frame สำหรับ grid ปุ่ม
frame_grid = tk.Frame(root)
frame_grid.pack()

buttons = []
for i in range(5):
    row = []
    for j in range(5):
        btn = tk.Button(frame_grid, width=6, height=3, bg="white")
        btn.grid(row=i, column=j, padx=2, pady=2)
        btn.config(command=lambda b=btn: change_color(b))
        row.append(btn)
    buttons.append(row)

# Bottom frame สำหรับปุ่ม Clear
frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=10)

btn_clear = tk.Button(frame_bottom, text="Clear", command=clear_grid, width=10)
btn_clear.pack()

root.mainloop()
