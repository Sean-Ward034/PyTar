import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import tarfile
import os

def pack_files():
    file_paths = filedialog.askopenfilenames(title="Select files to add to the tar archive")
    if not file_paths:
        messagebox.showinfo("Information", "No files selected.")
        return

    output_filename = filedialog.asksaveasfilename(defaultextension=".tar", filetypes=[("tar files", "*.tar")], title="Save tar file as...")
    if not output_filename:
        messagebox.showinfo("Information", "No output file specified.")
        return

    try:
        with tarfile.open(output_filename, 'w') as tar:
            for file_path in file_paths:
                if not (file_path.endswith('.h') or file_path.endswith('.cpp')):
                    continue
                
                arcname = os.path.basename(file_path)
                tar.add(file_path, arcname=arcname)

        messagebox.showinfo("Success", f"Successfully created {output_filename}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def extract_tar():
    tar_filename = filedialog.askopenfilename(title="Select the tar file to extract", filetypes=[("tar files", "*.tar")])
    if not tar_filename:
        messagebox.showinfo("Information", "No tar file selected.")
        return

    extract_directory = filedialog.askdirectory(title="Select the extraction directory")
    if not extract_directory:
        messagebox.showinfo("Information", "No extraction directory selected.")
        return

    try:
        with tarfile.open(tar_filename, 'r') as tar:
            tar.extractall(path=extract_directory)
            messagebox.showinfo("Success", f"Successfully extracted to {extract_directory}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def main():
    root = tk.Tk()
    root.title("Tar Utility")

    pack_button = tk.Button(root, text="Pack files into a tar archive", command=pack_files)
    pack_button.pack(pady=10)

    extract_button = tk.Button(root, text="Extract tar archive", command=extract_tar)
    extract_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()