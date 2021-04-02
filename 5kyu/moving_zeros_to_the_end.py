# https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(array):
    result = []
    for i in array.__reversed__():
        if type(i) in (float, int) and int(i) == 0:
            result.append(int(i))
        else:
            result.insert(0, i)
    return result


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
      == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
print(move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) ==
      [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(move_zeros(["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) ==
      ["a", "b", "c", "d", 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]) ==
      ["a", "b", None, "c", "d", 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(move_zeros([0, 1, None, 2, False, 1, 0]) == [1, None, 2, False, 1, 0, 0])
print(move_zeros(["a", "b"]) == ["a", "b"])
print(move_zeros(["a"]) == ["a"])
print(move_zeros([0, 0]) == [0, 0])
print(move_zeros([0]) == [0])
print(move_zeros([False]) == [False])
print(move_zeros([]) == [])
