def calc_order(nums):
  n = len(nums)
  order = 1
  ls = sorted(nums)
  for i, v in enumerate(nums[:-1]):
    c = (ls.index(v) - 1) * level_mat(n) // level_mat(n, i+1)
    order += c
    ls.remove(v)
  return order


def level_mat(n, m=None):
  if m is None:
    m = n
  assert n >= m

  if m == 0:
    return 1
  if n == 1:
    return 1
  else:
    return n * level_mat(n-1, m-1)


if __name__ == '__main__':
  n = int(input())
  ps = [int(i) for i in input().split()]
  qs = [int(i) for i in input().split()]
  print(abs(calc_order(ps) - calc_order(qs)))