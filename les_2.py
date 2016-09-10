# #pe2_1
# uur_loon=eval(input('Wat verdien je per uur: '))
# gewerkte_uren=eval(input('Hoeveel uur heb je gewerkt: '))
# print(str(uur_loon)+' uur werken levert '+str(uur_loon*gewerkte_uren)+' Euro op')


# #pe2_2
# score=eval(input('Geef je score: '))
# if score>15:
#     print('Gefeliciteerd!')
#     print('Met een score van ' +str(score) + ' ben je geslaagd!!')

# # pe2_3
# leeftijd=eval(input('Geef je leeftijd: '))
# nederlands_paspoort=input('Nederlands paspoort (ja/nee):')
#
# if leeftijd>=18 and nederlands_paspoort=='ja':
#     print('Gefeliciteerd, je mag stemmen!')

# # pe2_4
# leeftijd=eval(input('Geef je leeftijd: '))
# nederlands_paspoort=input('Nederlands paspoort (ja/nee):')
#
# if leeftijd>=18 and nederlands_paspoort=='ja':
#     print('Gefeliciteerd, je mag stemmen!')
# else:
#     print('Je mag helaas niet stemmen.')

# # pe 2_5
# str='Guido van Rossum heeft programmeertaal Python bedacht.'
# for ch in str:
#     if ch in ['a','e','i','o','u']:
#         print(ch)


# final_2
traject=['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk',
         'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "'s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
begin_station=input('Geef het beginstation: ')

if begin_station not in traject:
    print('Dit station komt niet voor in het traject.')
    begin_station=traject[0]
nr_begin_station=traject.index(begin_station)

eind_station=input('Geef het eindstation: ')
if eind_station not in traject or traject.index(eind_station)<nr_begin_station:
    print('Dit station komt niet voor in het traject na '+begin_station+'.')
    eind_station=traject[-1]
nr_eind_station=traject.index(eind_station)
print()

aantal_stations=nr_eind_station-nr_begin_station

print('Het beginstation '+begin_station+' is het '+str(nr_begin_station+1)+'e station in het traject')
print('Het eindstation '+eind_station+' is het '+str(nr_eind_station+1)+'e station in het traject')

print('De afstand bedraagt '+ str(aantal_stations)+' station(s)')
print('De prijs van het kaartje is '+str(5*aantal_stations) +' euro')
print()

print('Jij stapt in de trein in: '+str(begin_station))
for station in range(nr_begin_station+1,nr_eind_station):
    print('-'+traject[station])
print('Jij stapt uit in: '+str(eind_station))


# #2.29
#
# print(0==(1==2))
# print(2+(3==4)+5==7)
# print((1<-1)==(3>4))

# #3.18
# a,b,c=3,4,5
# if a<b:
#     print('OK 1')
#
# if b<c:
#     print('OK 2')
#
# if a+b==c:
#     print('OK 3')
#
# if a**2+b**2==c**2:
#     print('OK 4')

# #3.19
# lst=['January', 'February', 'March']
# for mnd in lst:
#     print(mnd[:3])
#
# #3.21
# lst=[2, 3, 4, 5, 6, 7, 8, 9]
# for i in lst:
#     if i%2==0:
#             print(i)

# #3.23
# for i in range(2):
#     print(i, end=' ')
# print()
# for i in range(1):
#     print(i, end=' ')
# print()
# for i in range(3,7):
#     print(i, end=' ')
# print()
# for i in range(1,2):
#     print(i, end=' ')
# print()
# for i in range(2):
#     print(i*3, end=' ')
# print()
# for i in range(5):
#     print(5+i*4, end=' ')


# # versie MV
# nrs=[2,1,3,2,1,2]
# # gaat goed met "If the length of the list is even the middle element is defined to
# # be the rightmost of the two elements in the middle of the list
# print(len(nrs)//2)
# print(nrs[len(nrs)//2])
#
# nrs.sort(reverse=True)
# # nrs.reverse()
# print(nrs)
#
# nrs.sort()
# # nrs.reverse()
# print(nrs)
# nrs.append(nrs.pop(0))
# print(nrs)

