# Dynamic Connectivity

*Dynamic Connectivity* is a data structure that dynamically maintains information about the connected components of a graph.

## Requirements & Assumptions
Given a set of *N* objects, the algorithm must

* connect two objects (union opertation)
* determine if there is a path connecting two objects (find/connected query)

Assume *"is connected to"* is an equivalance relation.

| Propery    | Description |
| ---------- | ----------- |
| Reflexive  | _p_ is connected to _p_ |
| Symmetric  | if _p_ is connected to _q_, then _q_ is connected to _p_ |
| Transitive | if _p_ is connected to _q_ and _q_ is connected to _r_, then _p_ is connected to _r_ |


Typical applications include

* Computers in a network
* Friends in a social network
* Transistors in a computer chip


## Implementation


### [Quick-find](../../src/dynamic_connectivity/quick_find.py) (Eager Approach)


Given two items _p_ and _q_
* change all entries with id[p] to id[q] to perform a union operation
* are connected if `id[p] == id[q]`


**QuickFindUF Class**

| Operation | Description | Complexity |
| ----------| ----------- | ---------- |
| `QuickFindUF(n)` | Initialize quick-find data structure with *N* objects | N |
| `union(p, q)` | Add connections between _p_ and _q_ | N |
| `boolean connected(p, q)` | Check id[_p_] and id[_q_] have same values | 1 |

Quick-find union is **too expensive**! Takes *N<sup>2</sup>* array accesses to process sequence of *N* union commands 
on *N* objects. 

For *10<sup>9</sup>* objects, it would take *10<sup>9</sup>* union commands. Hence it would take
*10<sup>18</sup>* operations or over 30 years for the fastest computer on this planet to complete the computation.


### [Quick-union](../../src/dynamic_connectivity/quick_find.py) (Lazy Approach)

Given two items _p_ and _q_
* take the root of the component containing the first item and make that child of the root of the component containing
the second item (Union Operation)

**QuickUnionUF Class**

| Operation | Description | Complexity |
| ----------| ----------- | ---------- |
| `QuickUnionUF(n)` | Initialize Quick-union data structure with *N* objects | N |
| `union(p, q)` | Change root of _p_ to point to root of _q_ | N (Worst Case) |
| `boolean connected(p, q)` | Check _p_ and _q_ have same root | N (Worst Case) |

Quick-union is also **too slow** for cases when the tree get's really tall (Worst Case). Operation to find the root of
the item is too expensive and could potentially require _N_ array accesses.


### [Weighted Quick-union with Path Compression](../../src/dynamic_connectivity/weighted_quick_union.py) (Optimal Approach)

Given two items _p_ and _q_
* keep track of number of objects in each tree and maintain balance by ensuring we link the root of the smaller tree to
the root of the larger tree (i.e. guarentees that no item is not too far from the root)

**WeightedUnionUF Class**

| Operation | Description | Complexity |
| ----------| ----------- | ---------- |
| `WeightedQuickUnionUF(n)` | Initialize Weighted Quick-union data structure with *N* objects | N |
| `void union(p, q)` | Change root of _p_ to point to root of _q_ | lg N |
| `boolean connected(p, q)` | Check _p_ and _q_ have same root | lg N |

Quick Union-find with compression is the **ideal** approach. For *10<sup>9</sup>* unions/finds for *10<sup>9</sup>* 
objects, Weighted Quick-union with compression reduces time to 6 seconds from 30 years required for the Quick-find.