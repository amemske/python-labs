from typing import List, Tuple

#example list where each element is a tuple of intergers
#the : colon means type hinting, i.e the example_list should be a tuple of ints
example_list: List[Tuple[int]] = [(1,2), (3,4), (5.6)]

#accessing the first tuple from the list
first_tuple: Tuple[int] = example_list[0]

#accessing the first element of the first tuple
first_element_of_first_tuple: int = first_tuple[0]

#printing the results
print(example_list)
print(first_tuple)
print(first_element_of_first_tuple)