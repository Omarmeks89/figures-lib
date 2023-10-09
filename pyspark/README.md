## Pyspark task

So, no DF found in task, i implement my own
DF-s. Final DF return as pair of <product><category>
where product without category is NULL.

Output contains two DF, because i`ve made
two (a little diferent) queries, depend on
situation we can choose between them.

Output:

```bash
+-------+--------+                                                              
|product|category|
+-------+--------+
|  prod1|       A|
|  prod1|       B|
|  prod1|       C|
|  prod1|       D|
|  prod2|       A|
|  prod2|       B|
|  prod2|       D|
|  prod3|       A|
|  prod3|       C|
|  prod3|       D|
|  prod3|       E|
|  prod4|    NULL|
+-------+--------+

+-------+--------+
|product|category|
+-------+--------+
|  prod1|       D|
|  prod1|       C|
|  prod1|       B|
|  prod1|       A|
|  prod2|       D|
|  prod2|       B|
|  prod2|       A|
|  prod3|       E|
|  prod3|       D|
|  prod3|       C|
|  prod3|       A|
|  prod4|    NULL|
+-------+--------+
```
