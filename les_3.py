# # pe 3_1
# def som(getal1,getal2,getal3):
#   som=getal1+getal1+getal3
#   return som
#
# print(som(1,2,3))

##pe 3_2
# def som(lijst):
#   som=sum(lijst)
#   return som
#
# print(som([1,2,3]))

# pe 3_3
# def lang_genoeg(lengte):
#     if lengte >=120:
#         return 'Je bent lang genoeg voor de attractie!'
#     else:
#         return 'Sorry, je bent te klein!'
#
# print(lang_genoeg(12))
# print(lang_genoeg(120))


# # pe 3_4
# def new_password(oldpassword,newpassword):
#         # bevatcijfer=False
#         for ch in newpassword:
#             if ch in '0123456789':
#                     return True
#         return False
#
#     bevatcijfer=False
#     if oldpassword!=newpassword and len(newpassword)>=6 and metcijfer(newpassword):
#         return True
#     else:
#         return False
# print(new_password('beeeee','beeeel'))

# pe 3_5
def kwadratensom(lijst):
    terugkeerwaarde=0
    for getal in lijst:
        terugkeerwaarde+=getal**2
    return terugkeerwaarde
print(kwadratensom([1,2]))
