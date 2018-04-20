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

