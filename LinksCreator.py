nazwy = open("nazwy.txt", 'r')
open("linkigłówne.txt", 'r')

for nazwa in nazwy:
    link = 'https://www.instagram.com/'+nazwa
    linkigłówne.write(link)
    linkigłówne.write('\n')
    
