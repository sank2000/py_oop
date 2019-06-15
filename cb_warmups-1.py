def sleep_in(weekday, vacation):
  if weekday and not vacation:
    return False
  if not weekday or vacation:
    return True

def monkey_trouble(a_smile, b_smile):
  if not a_smile and not b_smile:
    return True
  if a_smile and b_smile:
    return True
  else:
    return False

def sum_double(a, b):
  sum = a + b
  if a == b:
   return sum*2
  else:
    return sum

def diff21(n):
    diff = 21 - n
    diff = abs (diff)
    if n > 21:
      return diff*2
    else:
      return diff

 def parrot_trouble(talking, hour):
  if talking and hour > 20:
    return True
  if talking and hour < 7:
    return True
  else:
    return False

def makes10(a, b):
  if a == 10 or b == 10 or a+b == 10:
    return True
  else:
    return False

def near_hundred(n):
  val = abs (100 - n)
  val2 = abs (200 - n)
  if val <=10 or val2 <=10:
    return True
  else:
    return False

def pos_neg(a, b, negative):
  if a < 0 and b < 0 and negative:
    return True
  if a < 0 and b < 0 and not negative:
    return False
  if a < 0 or b < 0 and not negative:
    return True
  if negative and a < 0 or b < 0:
    return False
  else:
    return False

def not_string(str):
  if str[:3] == 'not':
    return str
  else:
    return 'not ' + str

def missing_char(str, n):
  i=0
  op = ''
  for alp in str:
    if i == n:
      i = i+1
      continue
    op = op + str [i]
    i+=1
  return op

 def front_back(str):
  if len(str)<=1:
    return str
  else:
   return str [-1] + str [1:-1] + str [0]

def front3(str):
  if len(str) >= 3:
    return str[:3]*3
  else:
    return str*3

#for questions, refer https://codingbat.com/python/
