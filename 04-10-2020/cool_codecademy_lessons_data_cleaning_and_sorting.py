highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, \
Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, \
The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, \
Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, \
Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(',')

highlighted_poems_stripped = []
for poem in highlighted_poems_list:
    highlighted_poems_stripped.append(poem.strip())

highlighted_poems_details = []
for item in highlighted_poems_stripped:
    highlighted_poems_details.append(item.split(':'))

titles = []
poets = []
dates = []

for details in highlighted_poems_details:
    place = 0
    for item in details:

        if place == 0:
            titles.append(item[0:])
            place += 1
        elif place == 1:
            poets.append(item[0:])
            place += 1
        elif place == 2:
            dates.append(item[0:])

for i in range(len(titles[0:])):
    print(f'The poem {titles[i]} was published by {poets[i]} in {dates[i]}.')

print(titles)
print(poets)
print(dates)
print(highlighted_poems_details)
