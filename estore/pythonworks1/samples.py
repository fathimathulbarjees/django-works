framework={"name":"django","rating":4,"language":"python"}

if "rating" in framework:
    framework["rating"]+=1
else:
    framework["rating"]=1


framework["architecture"]="mvt"
print(framework)