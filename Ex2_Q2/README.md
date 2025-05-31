# Motif Counter

This program find all possible motifs of given size n and then counts their accourance in the given diracted graph.

## Requirements

- Python 3.6 or higher
- NetworkX library


## How to run the code

1.Save your input graph file in edge-list format.
    Each line should contain two integers representing a directed edge (source and target vertex).
    For example:
```
1 2
2 3
1 4
```

2. Run the program:
```bash
python motif_counter.py
```

3. After you run the program you need to enter your input:
   - Enter the value of n (the size of subgraphs to look for)
   - Enter the path to your graph file

## Output Format

The program will output:
- n=... (the size of subgraphs)
- count=... (total number of different motifs found)
- For each motif:
  - #k (where k is the motif number)
  - count=m (where m is the number of times this motif appears)
  - List of edges in the motif

## Example

For input n=2 and a graph file containing:
```
1 2
2 3
1 4
```

The output will look like:
```
n=3
count=14
Count of existing motifs: 2
Count of non-existing motifs: 12

--------Existing motifs--------
#1
count=1
1 2
1 3

#2
count=1
1 2
2 3

--------Non-existing motifs--------
#3
count=0
1 2
2 1

#4
count=0
1 2
3 2

#5
count=0
1 2
1 3
2 1

#6
count=0
1 2
1 3
2 3

#7
count=0
1 2
2 1
3 1

#8
count=0
1 2
2 3
3 1

#9
count=0
1 2
1 3
2 1
2 3

#10
count=0
1 2
1 3
2 1
3 1

#11
count=0
1 2
1 3
2 1
3 2

#12
count=0
1 2
1 3
2 3
3 2

#13
count=0
1 2
1 3
2 1
2 3
3 1

#14
count=0
1 2
1 3
2 1
2 3
3 1
3 2

``` 