# DOC-Mania


### Problem Statement
- Someone said, hey nyancat, please investigate this DOCX file I found, it has some hidden text which is running some weird python script in my laptop. You might even find the key to unlock the door if you are lucky.

### Solution
- Open the docx in MS word, and click on show hidden text. Hidden text in base58 encoded form will be shown to you, decode and store it.
- The file type of newly stored file is "JFIF" which is an image file.
- Use steghide tool to extract data from it, but it requires password. The password is in the MACRO of the docs file in base64 form. Base64 decode it and get the password.
- Use The password to get the flag.txt file from the image file using steghide tool
