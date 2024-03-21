# TAR Utility GUI

## Introduction
The TAR Utility GUI is a Python-based graphical user interface application designed to simplify the process of packing files into TAR archives and extracting files from TAR archives. This application is built using the Tkinter library, making it accessible and easy to use for both beginners and advanced users who need to manage TAR files without using command-line tools.

## Features
- **Pack Files:** Select multiple files to pack into a TAR archive with options to filter specific file types (.h and .cpp files).
- **Extract Archive:** Extract the contents of a TAR archive to a specified directory.
- **Graphical User Interface:** A simple and intuitive GUI for easy operation without command-line interactions.

## Installation

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually comes with Python installation)

### Setup
1. Clone this repository to your local machine using `git clone`.
2. No additional packages are required since the application uses Tkinter, which is included with Python.

## Usage

To run the application, navigate to the cloned repository's directory in your terminal and execute the following command:

```bash
python PyTar.py
```

Upon launching, the application presents a straightforward interface with two main options:
- **Pack files into a tar archive:** Opens a dialog to select files for packing and then specify the TAR archive's save location.
- **Extract tar archive:** Opens a dialog to select a TAR file to extract and the destination directory.

## Contributions

Contributions are welcome! If you have suggestions for improvements or encounter any issues, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Enjoy using TAR Utility GUI for all your TAR packing and extracting needs!
