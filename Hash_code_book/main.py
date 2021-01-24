from Problem import Problem

PA = Problem("./Hash_code_book/problems/a_example.txt")
PA.read()

print(PA.libraries[0].books_sorted_by_score)