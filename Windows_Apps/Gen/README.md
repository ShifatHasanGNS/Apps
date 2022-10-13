# Gen (Generator)

---

It can **create** and **build** only **C++** source files. 😅
**But, still it's useful, if you don't want to type long commands over and over again.**
it can be used for **quick testing** purpose.

---

| #     |                Commands                               |                                 What it does?                                  |
|-------|-------------------------------------------------------|--------------------------------------------------------------------------------|
| **1** | `./gen` **or** `./gen -h` **or** `./gen help`         | Shows this table                                                               |
| **2** | `./gen -n <filename>` **or** `./gen new <filename>`   | Creates a new new file named `<filename>.cpp` and writes some boilerplate code |
| **3** | `./gen -t <filename>` **or** `./gen test <filename>`  | **Runs:** `g++ -std=c++20 -Wall -g -o0 <filename>.cpp -o test`                 |
| **3** | `./gen -b <filename>` **or** `./gen build <filename>` | **Runs:** `g++ -std=c++20 -Wall -g0 -o2 <filename>.cpp -o <filename>`          |
