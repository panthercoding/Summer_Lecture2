"""sets of students in various classes """

english = {"Tom","Cora","William","Jenny"}
physics = {"Tom","William","Jason","Claire","Janice"}
math = {"Cora","Jenny","Benedict","Martin"}
business = {"Jenny","Maggie","Leo"}

english_and_physics = english.intersection(physics)
print(english_and_physics) #{'Tom', 'William'}

physics_and_business = physics.intersection(business)
print(physics_and_business) #set() -> empty

physics_or_math = physics.union(math)
print(physics_or_math)
#{'Janice', 'Benedict', 'William', 'Jason', 'Claire', 'Tom', 'Jenny', 'Cora', 'Martin'}

physics_but_not_math = physics.difference(math)
print(physics_but_not_math) #{'Janice', 'William', 'Jason', 'Claire', 'Tom'}

english.add("Tiffany")
print(english) #{'Tiffany', 'William', 'Tom', 'Jenny', 'Cora'}