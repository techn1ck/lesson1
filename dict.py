test_dict = {
    "city" : "St. Petersburg",
    "temp" : "15"
}
print (test_dict["city"])

test_dict["temp"] = int(test_dict["temp"])-10
print (test_dict)

print(test_dict.get("country", "Russia"))
print (test_dict)

test_dict["date"] = "27.05.2019"
print (test_dict)
print (len(test_dict))
