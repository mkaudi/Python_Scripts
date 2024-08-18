country_population = {
    "Afghanistan": 12345,
    "Albania" : 32455,
    "Algeria": 9854,
    "Andora": 987645
    }


large_pop = 0
cntry = ""

for i, j in country_population.items():
    if j > 0:
        large_pop = j
        cntry = i

print("The largest country is" , cntry, "with a population of", large_pop)


