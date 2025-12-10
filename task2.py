# Логическая функция F задаётся выражением (x ∨ y) → (z ≡ x)
# № 14688
# ∨ -> or
# ∧ -> and
# → -> <=
# ≡ -> ==
# ¬ -> not
# print("x y z")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if not((x or y) <= (z == x)):
#                 print(x,y,z)

# (x ∧ ¬y) ∨ (y ≡ z) ∨ ¬w
# № 15618
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((x and not(y)) or (y == z) or not(w)):
#                     print(x,y,z,w)

# (z ∧ y) ∨ ((x → z ) ≡ (y → w))
# № 15939
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((z and y) or ((x <= z) == (y <=w))):
#                     print(x,y,z,w)

# ((x → y) ≡ (y → z)) ∧ (y ∨ w)
# № 16377
# print ("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (((x <= y) == (y <= z)) and (y or w)):
#                     print(x,y,z,w)


# ((y → w) ≡ (x → ¬z)) ∧ (x ∨ w)
# № 18483
# print("x y w z")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not(((y <= w) == (x <= (not(z)))) and (x or w)):
#                     print(x,y,w,z)
# print("-------_____________")
# print("x y w z")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (((y <= w) == (x <= (not(z)))) and (x or w)):
#                     print(x,y,w,z)

# F1  =  (x ∨¬ y) → (w ≡ z)
# F2  =  (x ∨¬ y) ≡ (w → z)
# print("x y w z")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f1 = (x or not(y)) <= (w == z)
#                 f2 = (x or not(y)) == (w <= z)
#                 if f1 == False and f2 == False:
#                     print(x,y,w,z)
# print("___________________")
# print("x y w z")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f1 = (x or not(y)) <= (w == z)
#                 f2 = (x or not(y)) == (w <= z)
#                 if f1 == False:
#                     print(x,y,w,z)
# print("___________________")
# print("x y w z")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f1 = (x or not(y)) <= (w == z)
#                 f2 = (x or not(y)) == (w <= z)
#                 if f2 == False:
#                     print(x,y,w,z)

# (¬x ≡ z) → (y ≡ (w ∨ x))
# 16805
# print("x y w z")
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 if not(((not(x)) == z) <= (y == (w or x))):
#                     print(x,y,w,z)

# (x ≡ (y → z)) ∧ (y ≡ ¬(z → w))
# 73828
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x == (y <= z)) and (y == (not(z <= w)))):
#                     print(x,y,z,w)

# print("___________")

# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((x == (y <= z)) and (y == (not(z <= w)))):
#                     print(x,y,z,w)

# F1  =  (x ∨¬ y) → (w ≡ z)
# F2  =  (x ∨¬ y) ≡ (w → z)
# №58469
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f1 = (x or not(y)) <= (w == z)
#                 f2 = (x or not(y)) == (w <= z)
#                 if f1 == False and f2 == False:
#                     print(x,y,z,w)

# print("______________")

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f1 = (x or not(y)) <= (w == z)
#                 f2 = (x or not(y)) == (w <= z)
#                 if f1 == False:
#                     print(x,y,z,w)

# print ("_____________")

# print("x y z w ")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f1 = (x or not(y)) <= (w == z)
#                 f2 = (x or not(y)) == (w <= z)
#                 if f2 == False:
#                     print(x,y,z,w)
        
# (x ∨ ¬y) ∧ ¬(y ≡ z) ∧ ¬w
# № 57409
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (x or not(y)) and not(y == z) and not(w):
#                     print(x,y,z,w) 

# (x ∧ y ∧¬z) ≡ (y ∨ z ∨ ¬w)
# № 27001
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (x and y and not(z)) == (y or z or not(w)):
#                     print(x,y,z,w)
                    
# F = (y → x) ∧ ¬z ∧ w
# print("x y z w")
# for x in range(2):
#      for y in range(2):
#          for z in range(2):
#              for w in range(2):
#                  if (y <= x) and not(z) and w:
#                      print(x,y,z,w)

# w ∧ (y ≡ (z → (x ∨ y)))
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if w and (y == (z <= (x or y))):
#                     print(x,y,z,w,)

# F = ¬(w → x) ∨ (y → z) ∨ ¬y
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not(not(w <= x) or (y <= z) or not(y)):
#                     print(x,y,z,w)

# (z ≡ ¬y) ∧ (¬x ∨ y) ∧ w
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (z == (not(y))) and (not(x) or y) and w:
#                     print(x,y,z,w)

# (х → y) ∨ ¬(w → z)
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((x <= y) or not(w <= z)):
#                     print(x,y,z,w)

# F = (x ∧ ¬y) ∨ (y ≡ z) ∨ ¬w
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((x and not(y)) or (y == z) or not(w)):
#                     print(x,y,z,w)

# (x ∧ y) ∨ ((z ≡ y) ∧ w)
# print("x y z w")
# for x in range(2):
#      for y in range(2):
#          for z in range(2):
#              for w in range(2):
#                 if not((x and y) or ((z == y) and w)):
#                     print(x,y,z,w)
                
# print("______________")

# print("x y z w")
# for x in range(2):
#      for y in range(2):
#          for z in range(2):
#              for w in range(2):
#                 if (x and y) or ((z == y) and w):
#                     print(x,y,z,w)

# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (w <= (y == z)) and (y == (z <= x)) == 0:
#                     print(x,y,z,w) 

# print('x y w z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((x and (not(y))) or (x == z) or w) :
#                     print(x, y, w, z)