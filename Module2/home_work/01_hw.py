# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Формат входных данных
# Вводятся 3 натуральных числа n, m и k. Точно известно, что  k ≠ n ⋅ m.
# Формат выходных данных
# Выведите «YES», если можно отломить от шоколадки ровно k долек, и «NO» иначе.


len = int(input('введите длину плитки '))
wid = int(input('введите ширину плитки '))
br = int(input('введите кол во отломленных долек '))
if len < wid and br < len:
 print('no')
elif wid < len and br < wid:
 print('no')
elif len%br==0 or wid%br==0:
 print('yes')
elif br%len==0 or br%wid==0:
 print('yes')
elif len%br!=0 or wid%b!=0:
 print('no')
elif br%len!=0 or br%wid!=0:
 print('no')
