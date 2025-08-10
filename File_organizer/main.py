from organize_files import check_files
import customtkinter as ctk

root = ctk.CTk()
root.geometry("500x400")
ctk.set_appearance_mode("dark")

# Everything is obvious (:

label = ctk.CTkLabel(root ,text="Enter Your Folder Path That You Want To Organize", font=("Arial", 15, "bold"))
label.place(relx=0.5, rely=0.4, anchor="center")

entry = ctk.CTkEntry(root, width=250)
entry.place(relx=0.5, rely=0.5, anchor="center")

btn = ctk.CTkButton(root, text="Organize Files", command=lambda:check_files(entry.get()), fg_color="green", hover_color="#006400", font=("Arial", 12, "bold"))
btn.place(relx=0.5, rely=0.6, anchor="center")

root.mainloop()