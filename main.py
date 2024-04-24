from collections import namedtuple

# # 1
# Kitob = namedtuple('Kitob', 'nomi muallif nashriyot')
# kitob1 = Kitob('Python dasturlash', 'John Smith', 'Oxford')
# print(kitob1)

# 2
# Shaxs = namedtuple('Shaxs', 'ism familiya yosh')
# shaxs1 = Shaxs._make(['Ali', 'Valiyev', 25])
# print(shaxs1)
# shaxs2 = shaxs1._replace(ism='Hasan')
# print(shaxs2)
# print(Shaxs._fields)

# 3
#
# Mashina = namedtuple('Mashina', 'turi rang yili')
# mashina1 = Mashina._make(['Sedan', 'Qora', 2020])
# print(mashina1)
# mashina2 = mashina1._replace(rang='Oq')
# print(mashina2)
# print(Mashina._fields)

# 4
# Kitob = namedtuple('Kitob', 'nomi muallif nashriyot')
# kitob1 = Kitob._make(['Python dasturlash', 'John Smith', 'Oxford'])
# print(kitob1)
# kitob2 = kitob1._replace(muallif='Jane Doe')
# print(kitob2)
# print(Kitob._fields)

# 5
#
#
# from collections import namedtuple
# Talaba = namedtuple('Talaba', 'ism familiya kurs')
# talaba1 = Talaba._make(['Hasan', 'Karimov', 3])
# print(talaba1)
# talaba2 = talaba1._replace(kurs=4)
# print(talaba2)
# print(Talaba._fields)





