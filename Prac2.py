set1 = set()
set2 = set()
while True:
 print("1. Add element to set 1\n2. Add element to set 2\n3. Remove element from set 1\n4. Remove element from set 2")
 print("5. Search if element in collection\n6. Number of Elements and Elements in collection\n7. Intersection\n8. Union")
 print("9. Difference\n10. Subset\n11. Exit\n")
 choice = int(input("Enter operation you want to perform: "))
 if choice == 1:
 inputSet1 = input("Enter element to add: ")
 set1.add(inputSet1)
 elif choice == 2:
 inputSet2 = input("Enter element to add: ")
 set2.add(inputSet2)
 elif choice == 3:
 remove1 = input("Enter element to remove: ")
 set1.discard(remove1)
 elif choice == 4:
 remove2 = input("Enter element to remove: ")
 set2.discard(remove2)
 elif choice == 5:
 search1 = input("Enter element to search :")
 for ele in set1:
 if ele == search1:
 print("Element found.\n")
 break
 else:
 print("Element not found.\n")
 elif choice == 6:
 count = 0
 for ele in set1:
 count += 1
 print(f"Total elements in collection: {count}")
 for ele1 in set1:
 print(ele1, " ",end="")
 print("\n")
 elif choice == 7:
 temp = set1.intersection(set2)
 print(temp)
 elif choice == 8:
 temp = set1.union(set2)
 print(temp)
 elif choice == 9:
 temp = set1.difference(set2)
 elif choice == 10:
 temp = set2.issubset(set1)
 if temp == True:
 print("Set2 is subset of Set1.\n")
 else:
 print("Set2 in not subset of Set1.\n")
 elif choice == 11:
 print("GoodBye!\n")
 break
 else:
 print("Invalid choice. Enter Valid choice.\n")
