#Reverse keys and values in a dictionary.
dic={
     "harsh":85,"prince":75,"jay":80
}
reversed_dic={value:key for key,value in dic.items()}
print(reversed_dic)
