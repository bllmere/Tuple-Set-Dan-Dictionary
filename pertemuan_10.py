# Program 10.1 Tuples dan sets

# LIST
# menggunakan kurung siku
data_list = [10,2,4,3,2]
print (data_list)

# tuples
data_tuples = (7,8,10,11)
print (data_tuples)
print (data_tuples[1])

# tidak bisa dilakukan 
# data_tuples[1] = "gabb"
# data_tuples.append(1)

# sets (himpunan)
data_sets = {10,4,3,2,7,6,5}
print (data_sets)


# Program 10.2 Dictionary

# list -> array, mengakses dengan menggunakan index

data_list = ['gabb','hasym','maoll']
print (data_list[0])

# dictionary (dict) -> associative array
# identifier -> key

data_dict = {
    'key' : 'value',
    'gb'  : 'gabb',
    'hs'  : 'hasym',
    'mo'  : 'maoll',
    'nmbr': '7',
    'list': data_list
}
print (data_dict['gb'])
print (data_dict['nmbr'])
print (data_dict['list'])


# Program 10.3 Operasi Dictionary

## ---Operasi Dictionary---

data_dict = {
    "cal" : "ical paical",
    "pras": "pras gupras",
    "ray" : "ray maray"
}

# panjang dicitionary
LENDICT = len(data_dict)
print (f"panjang dictionary : {LENDICT}")

# mengecek key exist atau tidak
KEY = "cal"
CHECKKEY = KEY in data_dict
print (f"apakah {KEY} ada di data_dict : {CHECKKEY}")

# mengakses value (read) dengan get
print (data_dict["cal"])
print (data_dict.get("cal"))
print (data_dict.get("kis","key tidak ditemukan")) # check key dengan massage

# mengaupdate data 
data_dict["cal"] = "ical si ganteng"
print (data_dict)
data_dict["piw"] = "piw si piwuu"
print (data_dict)

data_dict.update ({"cal" : "ical paical"})
print (data_dict)
data_dict.update ({"blmere" : "blmere keren"}) # akan ditambah jika tidak ada
print (data_dict)


# Program 10.4 Looping Dictionary

## ---Looping Dictionary---

teman_teman = {
    "git" : "git sigit",
    "guh" : "guh teguh",
    "met" : "met slamet",
    "jo"  : "jo bejo"
}

# looping first try ( yang keluar hanya key)

for teman in teman_teman :
    print (teman)

# operator untuk mengambil item

keys = teman_teman.keys()
print (keys)

for keys in teman_teman.keys() :
    print (teman_teman.get(keys))

values = teman_teman.values()
print (values)

for values in teman_teman.values() :
    print (values)

items = teman_teman.items()
print (items)

for item in teman_teman.items() :
    print(items)

for keys,values in teman_teman.items() :
    print (f"keys = {keys}, values = {values}")