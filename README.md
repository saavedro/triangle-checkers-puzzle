Checkers puzzle
===============

This is a repository for gathering different computational experiments around
little puzzle game:

[[image]]


### Board model
```
           0
         /   \
        1     2
       /  \ /  \
      3    4    5
    /  \ /   \ / \
   6 -  7  -  8 - 9
  /    / \   / \   \
10 - 11 -  12 - 13 -14
```

Following tripples are available:
- [0,2,5]
- [2,5,9]
- [5,9,14]
- [1,4,8]
- [4,8,13]
- [3,7,12]
- [0,1,3]
- [1,3,6],
- [3,6,10]
- [2,4,7],
- [4,7,11],
- [5,8,12],
- [3,4,5],
- [6,7,8]
- [7,8,9]
- [10,11,12]
- [11,12,13]
- [12,13,14]

0 - means empty spot, 1 - means pin in the spot
move is possible if:
[1,1,0] -> [0,0,1]
[0,1,1] -> [1,0,0]

