[//]: # (Kevin Chen)
[//]: # (Assignment 3)
[//]: # (CS 475)

# CS-475-Assignment-3
Enigma Machine with variations



## Configuration
The encryption/decryption is reliant on keys being specified in the keys.json file alongside the rest of the files.
- key1: 36-Character string used to define the plugboard
- key2: 36-Character string used to define the reflector
- key3: 3-Charcacter string used to define the initial rotations of the wheels. For example, 'ABC' rotates the left wheel 0 positions, the middle wheel 1 position, and the right wheel 2 positions.

The supported characters, wheel wirings, and wheel rotation rates can be specified in config.py. By default, they're set to the values given in the assignment.



## Usage
Ensuring that all files, including keys.json, are in working directory, run driver.py from the command line.
  ```bash
    python3 driver.py
  ```

This starts a read-eval-print loop to encrypt or decrypt messages. You should be greeted with the following to get started:
  ```text
    Enigma... Press Ctrl+D to stop
    Commands:
        encrypt <message>
        decrypt <message>
    >
  ```
  
Example:
  ```text
    > encrypt HELLO
    8CXKA
    > decrypt 8CXKA
    HELLO
  ```
  
Note: Any lowercase input will be converted to uppercase
