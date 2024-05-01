e, s, m = map(int, input().split())
year = 1
jun_year = [1,1,1]

while True:
    if [e,s,m] == jun_year:
        print(year)
        break
    jun_year = list(map(lambda x:x+1, jun_year))
    if jun_year[2] == 20:
        jun_year[2] = 1
    if jun_year[1] == 29:
        jun_year[1] = 1
    if jun_year[0] == 16:
        jun_year[0] = 1
    year += 1
