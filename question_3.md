# Question 3:

## 1. What is Git and why is it used?
### **What is Git?**
- Git is the most commonly used distributed version control system for source code management.
- Git can record the historical version of each file, so that developers can easily track and revert previous changes.
- Git can synchronize changes among different developers and coordinate the work of the entire team.
- Git provides branching and merging functions, allowing developers to easily switch between different versions.
- Git is an open-source software, so anyone can use and modify it freely.
### **Why is it used?**  
There are many benefits to using Git, here are some reasons to use Git:

- Functionality
  - Version control: easy to track, view and revert past changes at any time, and switch between different versions
  - Collaborative development: synchronize changes among different developers, reducing conflicts and errors
  - Branching and merging: modified and tested without impacting the main version
  - Remote repository: Can access and share the repository at any time for easy collaboration and backup.
   
- Attribute
  - Free and open source
  - Fast and small file size
  - Safety and reliability: distributed, prevent data corruption and loss

Reference:
- [Git official documents](https://git-scm.com/doc)
- [What is Git: Features, Command and Workflow in Git](https://www.simplilearn.com/tutorials/git-tutorial/what-is-git)
- [What is Git and Why Should You Use it?](https://www.nobledesktop.com/learn/git/what-is-git)
- [什麼是 Git？為什麼要學習它？](https://gitbook.tw/chapters/introduction/what-is-git)


<hr/>

## 2. What is the difference between List, Dictionary, Tuple and Set in Python?

**Difference**
| Parameters | List | Tuple | Set | Dictionary |
| :--: | :---:| :----:| :--:| :--------: |
| Representation | [] | () | {} | {} |
| Data | mutable | immutable | mutable | mutable |
| Homogeneity | non-homogenous type, stores various elements | non-homogenous type, stores various elements | non-homogenous type, stores various elements | non-homogenous type, stores key-value pairs |
| Order | ordered | ordered | unordered | ordered <br/> (In Python 3.6 and earlier, dictionaries are unordered) |
| Duplicate elements | allow | allow | not allow | not allow duplicate keys |
| Function for Creation | list() | tuple() | set() | dict() |

\[Note\] <br/>
**Only for List and Tuple**
> **Similarity:**
> - They are used for storing objects (Store multiple items under a single variable)
> - That data can be of any type (They can contain mix of different data types, duplicate items and values can be repeated)
> - They are ordered (Their items can be accessed by their index)
> - They support unpacking <br />

> **Difference:**
>| Parameters | List | Tuple |
>| :--: | :---:| :----:|
>| Iterations | time-consuming | faster |
>| Memory | consume more memory | consumes less memory |
> | Security | unexpected change or error is more likely to occur | changes and errors don't usually occur
* Even if there is only one item to put into the tuple, a comma should be added after it


Reference:
- [Difference Between List and Tuple in Python](https://www.simplilearn.com/difference-between-list-and-tuple-in-python-article)
- [Python有了串列(list)，為何還要有元組(tuple) ？](https://selflearningsuccess.com/python-tuple/)
- [Python Tuple VS List – What is the Difference?](https://www.freecodecamp.org/news/python-tuple-vs-list-what-is-the-difference/)
- [List Vs. Tuple Vs. Set Vs. Dictionary: Know the Difference Between List, Tuple, Set, and Dictionary in Python](https://byjus.com/gate/difference-between-list-tuple-set-and-dictionary-in-python/)
- [Differences and Applications of List, Tuple, Set and Dictionary in Python](https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/)
