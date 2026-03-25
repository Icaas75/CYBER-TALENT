Week-2 Day-1
 
1. Linux File Structure

Linux uses a hierarchical (tree-like) structure starting from root `/`.

Important Directories

    | Directory | Purpose                |
    | --------- | ---------------------- |
    | `/`       | Root directory         |
    | `/home`   | User files             |
    | `/etc`    | Configuration files    |
    | `/bin`    | Essential commands     |
    | `/var`    | Logs and variable data |
    | `/tmp`    | Temporary files        |

Useful Commands

    pwd            # show current directory
    ls             # list files
    ls -la         # detailed list (hidden files too)
    cd /path       # change directory
    cd ..          # go one level up
    mkdir test     # create folder
    touch file.txt # create file
    rm file.txt    # delete file

2. Grep (Search Tool)

Used to search text inside files.

Basic Usage

    grep "text" file.txt

Important Options

      grep -i "text" file.txt     # ignore case
      grep -r "text" .            # search recursively
      grep -o "pattern" file.txt  # show only matched part
      grep -n "text" file.txt     # show line number

Special Patterns

    	grep -o "flag{.*}" file.txt
      
* `flag{}` → pattern we are looking for
* `.` → any character
* `*` → repeat many times


3. Nano Editor

Simple terminal text editor.

Openening File
	nano file.txt

Shortcuts
| Action   | Shortcut |
| -------- | -------- |
| Save     | Ctrl + O |
| Exit     | Ctrl + X |
| Cut line | Ctrl + K |
| Paste    | Ctrl + U |
| Search   | Ctrl + W |


4. Vim Editor

Advanced and powerful editor.

Opening File

    vim file.txt

Modes
* Normal mode (default)
* Insert mode (press `i`)
* Command mode (press `:`)

Basic Commands

    i        # enter insert mode
    Esc      # go back to normal mode
    :w       # save
    :q       # quit
    :wq      # save and quit
    :q!      # quit without saving


5. Steganography

Technique of hiding data inside files (image, audio, etc).

1. strings
   
    	strings file.png
    	strings file.png | grep -i flag

3. steghide

	    steghide extract -sf image.jpg

5. binwalk

    	binwalk file.png
    	binwalk -e file.png

7. zsteg (for PNG)

	    zsteg file.png

9. exiftool

       exiftool file.jpg

Typical Workflow

    file image.png
    strings image.png | grep flag
    exiftool image.png
    binwalk image.png
    binwalk -e image.png
    zsteg image.png
    steghide extract -sf image.png
