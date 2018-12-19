import math
import random
import time

import turtle

t = turtle.Turtle()


# from python src
def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return v, v, v
    i = int(h*6.0) # XXX assume int() truncates!
    f = (h*6.0) - i
    p = v*(1.0 - s)
    q = v*(1.0 - s*f)
    t = v*(1.0 - s*(1.0-f))
    i = i%6
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q
    # Cannot get here


def alpha(n):
  ''' rad '''
  return (n-2) * math.pi / n


def beta(n):
  ''' deg '''
  return 360. / n 


def rhex():
  return '{:x}'.format(random.randrange(1 << 8))


def rcolor():
  return '#' + ''.join([rhex() for _ in range(3)])


def rcolor2():
  r = random.random
  rgb = hsv_to_rgb(r() * 255, 1, 255)
  print('rgb', rgb)
  int_rgb = [int(i) for i in rgb]
  print('int_rgb', int_rgb)
  hex_rgb = [hex(i)[2:] for i in int_rgb]
  print('hex_rgb', hex_rgb)
  hex2_rgb = ['{:0>2}'.format(i) for i in hex_rgb]
  print(hex2_rgb)
  return '#' + ''.join(hex2_rgb)


def rcolor3(n):
  colors = []
  for i in range(n):
    rgb = hsv_to_rgb(.5 * i / n, 1, 255)
    # print('rgb', rgb)
    int_rgb = [int(i) for i in rgb]
    # print('int_rgb', int_rgb)
    hex_rgb = [hex(i)[2:] for i in int_rgb]
    # print('hex_rgb', hex_rgb)
    hex2_rgb = ['{:0>2}'.format(i) for i in hex_rgb]
    print(hex2_rgb)
    colors.append('#' + ''.join(hex2_rgb))
  return colors


def deg2rad(deg):
  return deg * math.pi / 180.


def rad2deg(rad):
  return rad * 180. / math.pi


def epsilon(x, alp):
  num = x * math.sin(alp)
  den = 1 - x * (1 + math.cos(alp))
  return math.atan(num / den)


def b(ax, alp, eps):
  num = ax * math.sin(alp)
  return num / math.sin(eps)


def multi(t, n, a, bet):
  t.begin_fill()
  for i in range(n):
    print(i)
    t.fd(a)
    t.lt(bet)
  t.end_fill()


def mv(t, ax, alp, eps):
  t.fd(ax)
  t.lt(rad2deg(eps))


def main1():
  for i in range(3, 10):
    bet = beta(i)
    col = rcolor2()
    print('\t{} {}'.format(i, col))
    t.color(col)
    multi(t, i, 20, bet)


def main2():
  n = 3
  a = 400
  x = .01
  N = 200

  alp = alpha(n)
  bet = beta(n)
  eps = epsilon(x, alp)
  cs = rcolor3(N)

  for i in range(N):
    col = cs[i]
    print('\t{} {}'.format(i, col))
    t.color(col)
    multi(t, n, a, bet)
    ax = a * x
    mv(t, ax, alp, eps)
    a = b(ax, alp, eps)


def tests():
  for i in (0, 90, 180, 360):
    print(i, deg2rad(i))

  for i in (0, 1./3, 1./2, 2./3, 1):
    print(i, rad2deg(i * math.pi))

  for i in (1./2, 1./3):
    print(i, epsilon(.5, i * math.pi))


if __name__ == '__main__':
  random.seed(42)
  # main1()
  main2()
  # tests()
