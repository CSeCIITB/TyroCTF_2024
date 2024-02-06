# PDFCrypt

> FLAG: tyroCTF{G4lp_Brut3_str3ngth_1s_all_it_n33d3d}

### Problem Statement
- There are some good chances that the key nyancat gets from this pdf file gives additional access to a secret server. But it is password protected. What to do, and what not to do?

### Solution
- The PDF file is password protected, so use pdftojohn to have password hash.
- Use john to crack the password of the hash found. Use rockyou.txt as wordlist.
- PASSWORD: winniethepooh 
