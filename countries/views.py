from json import load
with open("country.json",encoding="UTF=8") as  f:
    data=load(f)
print(len(data))
country_name=[c.get("name") for c in data]
print(country_name)

def get_country_details(name):
    return [c for  c in data if c.get("name")==name][0]
details=get_country_details("India")
print(details)



def get_country_details(name):
    return [c for  c in data if c.get("name")==name][0]
details=get_country_details("India")
print(details)

def country_capital(name):
    c_data=get_country_details(name)
    if c_data:
        return c_data.get("capital")


print(get_country_details("Pakistan"))


def country_population(name):
    c_data=get_country_details(name)
    if c_data:
        return c_data.get("population")


print(get_country_details("India"))



def country_currencyname(name):
    c_data=get_country_details(name)
    if c_data:
        return c_data.get("currencies")[0].get("name")
print(country_currencyname("India"))

def country_currency(name):
    return [c.get("currencies")[0].get("name")for c in data if c.get("name")==name]



def country_bordername(name):
    c_data=get_country_details(name)
    borders_list=c_data.get("borders")
    b_names=[c.get("name") for c in data if c.get("alpha3Code") in borders_list]
    return (b_names)


print(country_bordername("Sri Lanka"))



def maxpopulated_country():
    c_data=max(data,key=lambda c:c.get("population"))
    return c_data.get("name")

print(maxpopulated_country())




def minpopulated_country():
    c_data=min(data,key=lambda c:c.get("population"))
    return c_data.get("name")

print(minpopulated_country())


def country_language(name):
    c_data = get_country_details(name)
    return [l.get("name")for l in c_data.get("languages")]
print(country_language("India")




