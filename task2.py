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
print("x y w z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = (x or not(y)) <= (w == z)
                f2 = (x or not(y)) == (w <= z)
                if f1 == False and f2 == False:
                    print(x,y,w,z)
print("___________________")
print("x y w z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = (x or not(y)) <= (w == z)
                f2 = (x or not(y)) == (w <= z)
                if f1 == False:
                    print(x,y,w,z)
print("___________________")
print("x y w z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = (x or not(y)) <= (w == z)
                f2 = (x or not(y)) == (w <= z)
                if f2 == False:
                    print(x,y,w,z)