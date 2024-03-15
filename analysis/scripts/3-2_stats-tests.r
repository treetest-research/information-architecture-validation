print("-----------------")
print("Tree test - individual task success differences.")
print("-----------------")

print(fisher.test(matrix(c(7, 23, 7, 23, 7, 23), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(12, 18, 10, 20, 10, 20), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(8, 22, 5, 25, 7, 23), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(30.0, 0.0, 23.0, 7.0, 28.0, 2.0),
                         nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(22, 8, 21, 9, 23, 7), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(6, 24, 6, 24, 6, 24), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(11, 19, 6, 24, 8, 22), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(13, 17, 10, 20, 6, 24), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(23, 7, 24, 6, 23, 7), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(5.0, 25.0, 0.0, 30.0, 6.0, 24.0),
                         nrow = 2, ncol = 3)))

print("-----------------")
print("Tree test - individual task direct success differences.")
print("-----------------")

print(fisher.test(matrix(c(10, 20, 9, 21, 12, 18), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(23, 7, 20, 10, 24, 6), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(25, 5, 24, 6, 26, 4), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(30.0, 0.0, 29.0, 1.0, 30.0, 0.0),
                         nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(27.0, 3.0, 30.0, 0.0, 26.0, 4.0),
                         nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(15, 15, 14, 16, 17, 13), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(28, 2, 20, 10, 28, 2), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(23, 7, 19, 11, 22, 8), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(29.0, 1.0, 30.0, 0.0, 28.0, 2.0),
                         nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(23, 7, 21, 9, 24, 6), nrow = 2, ncol = 3)))

print("-----------------")
print("Tree test - individual task directness differences.")
print("-----------------")

print(fisher.test(matrix(c(4, 26, 3, 27, 6, 24), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(17, 13, 14, 16, 20, 10), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(24, 6, 24, 6, 26, 4), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(20, 10, 24, 6, 24, 6), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(23, 7, 26, 4, 21, 9), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(11, 19, 11, 19, 14, 16), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(27, 3, 20, 10, 27, 3), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(20, 10, 16, 14, 21, 9), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(17, 13, 17, 13, 18, 12), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(21, 9, 21, 9, 23, 7), nrow = 2, ncol = 3)))

print("-----------------")
print("TT respondents' internet and magazine usage test.")
print("-----------------")

# internet usage
print(fisher.test(
                  matrix(c(15, 19, 15, 13, 11, 15, 2, 0, 0),
                         nrow = 3, ncol = 3, byrow = TRUE)))

# magazine visits
print(fisher.test(
                  matrix(c(11, 12, 5, 2, 14, 12, 2, 2, 11, 12, 1, 6),
                         nrow = 4, ncol = 3)))

print("-----------------")
print("WT respondents' internet and magazine usage test.")
print("-----------------")

# internet usage
print(fisher.test(
                  matrix(c(14, 16, 15, 16, 13, 14, 0, 1, 1),
                         nrow = 3, ncol = 3, byrow = TRUE)))

# magazine visits
print(fisher.test(
                  matrix(c(11, 8, 7, 4, 12, 13, 1, 4, 8, 8, 5, 9),
                         nrow = 4, ncol = 3)))

print("-----------------")
print("All respondents' internet and magazine usage test.")
print("-----------------")

# internet usage
print(fisher.test(matrix(c(15, 19, 15, 14, 16, 15, 13, 11, 15,
                           16, 13, 14, 2, 0, 0, 0, 1, 1),
                         nrow = 3, ncol = 6, byrow = TRUE)))

# magazine visits
print(fisher.test(matrix(c(11, 12, 5, 2, 14, 12, 2, 2, 11, 12, 1, 6,
                           11, 8, 7, 4, 12, 13, 1, 4, 8, 8, 5, 9),
                         nrow = 4, ncol = 6), simulate.p.value = TRUE, B = 1e7))

print("-----------------")
print("Web test - individual task success differences.")
print("-----------------")

print(fisher.test(matrix(c(8, 22, 4, 26, 4, 26), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(14, 16, 7, 23, 7, 23), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(7, 23, 6, 24, 3, 27), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(23, 7, 24, 6, 24, 6), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(24, 6, 22, 8, 20, 10), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(6, 24, 3, 27, 6, 24), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(3, 27, 9, 21, 6, 24), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(9, 21, 2, 28, 4, 26), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(23, 7, 19, 11, 19, 11), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(4, 26, 0, 30, 3, 27), nrow = 2, ncol = 3)))

print("-----------------")
print("Web test - individual task direct success differences.")
print("-----------------")

print(fisher.test(matrix(c(13, 22, 17, 26, 8, 26), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(24, 16, 21, 23, 24, 23), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(25, 23, 27, 24, 26, 27), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(30, 7, 30, 6, 29, 6), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(29, 6, 27, 8, 28, 10), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(17, 24, 14, 27, 20, 24), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(25, 27, 27, 21, 24, 24), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(27, 21, 23, 28, 26, 26), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(30, 7, 28, 11, 30, 11), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(27, 26, 28, 30, 23, 27), nrow = 2, ncol = 3)))

print("-----------------")
print("Web test - individual task directness differences.")
print("-----------------")

print(fisher.test(matrix(c(8, 22, 15, 26, 5, 26), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(17, 16, 17, 23, 20, 23), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(22, 23, 25, 24, 26, 27), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(22, 7, 22, 6, 20, 6), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(24, 6, 23, 8, 20, 10), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(14, 24, 11, 27, 18, 24), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(24, 27, 25, 21, 23, 24), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(24, 21, 21, 28, 26, 26), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(21, 7, 21, 11, 25, 11), nrow = 2, ncol = 3)))
print(fisher.test(matrix(c(25, 26, 28, 30, 23, 27), nrow = 2, ncol = 3)))