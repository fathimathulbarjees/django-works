from json import load
with open("countrydata.json",encoding="UTF-8") as f:
    data=load(f)
#print(len(data))

country_names=[c.get("name")for c in data]
#print(country_names)

def get_country_details(name):
   #for c in data:
       # if c.get("name")==name:
           # return c
             #or
   return [c for c in data if c.get("name")==name][0]


def get_country_capital(name):
    c_data=get_country_details(name)
    if c_data:
        return c_data.get("capital")

def get_country_population(name):
    c_data=get_country_details(name)
    if c_data:
        return c_data.get("population")

def get_country_currecyname(name):
    #c_data=get_country_details(name)
    #if c_data:
        #return c_data.get("currencies")[0].get("name")
                #or
    return [c.get("currencies")[0].get("name")for c in data if c.get("name")==name]

def country_border_list_names(name):
    c_data=get_country_details(name)
    border_list=c_data.get("borders")
    b_name=[c.get("name")for c in data if c.get("alpha3Code")in border_list]
    return b_name
def get_maxpopulated_country():
    c_data=max(data,key=lambda c:c.get("population"))
    return c_data.get("name")
#print(get_maxpopulated_country())

def get_minpopulated_country():
    c_data=min(data,key=lambda c:c.get("population"))
    return c_data.get("name")


def get_country_language(name):
    c_data=get_country_details(name)
    return[l.get("name")for l in c_data.get("languages")]
print(get_country_language("India"))
#print(get_minpopulated_country())
#print(country_border_list_names("Sri Lanka"))


#print(get_country_currecyname("India"))


#print(get_country_population("India"))
##details=get_country_details("Afghanistan")
#print(details)





