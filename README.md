# LNK File Analysis

This quick script provides basic information about an MS LNK file. It will show:

- The original command / target
- A tidied up version of the command / target
- Any decsription associated with the LNK
- Machine identifier (if present)

These can be used to obtain IOCs / Intel from the suspect LNK file.

## Usage

Edit the file to add the filename of the LNK file and execute from the command line or IDE. Note: Windows will not display the .lnk extension even if 'show file extenstions' is enabled. I'll make this better soon...

## Requirements

The following Python package is required:

- LnkParse3 https://pypi.org/project/LnkParse3/

```pip install LnkParse3```

Tested on Windows 10 using Pycharm (Community).

## Caution

Always use a clean, isolated VM when testing or examining suspicious or potentionaly malicious files.

## Thanks

Thanks to the Internet and everyone who shares their knowledge and expertise freely :-)
