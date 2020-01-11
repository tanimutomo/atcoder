def get_init(n):
  init_list = [str(i) for i in range(1, n+1)]
  end_list = reversed(init_list)
  init = ''.join(init_list)
  end = ''.join(end_list)
  return int(init), int(end)


def comp_perm(init, end):
  perm = list(init)
  i = 0
  while True:
    init + i
    



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
  init, end = get_init(n)
  print(init, end)
  perm = comp_perm(init, end)
  print(perm)