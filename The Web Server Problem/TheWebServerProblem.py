import time
from functools import lru_cache


f=open("./data.txt","r")
mspeed = 2
mloadtime = 60
@lru_cache(maxsize=None)
def serve_chunk(data_size):
    chunk_size = 2.5 if data_size <= 5 else 4
    num_chunks = data_size / chunk_size
    for i in range(int(num_chunks)):
        time.sleep(chunk_size / mspeed)
    

websites = []
wb=1
for i in f.readlines():
    nl=i.split()
    # print(nl)
    web={
        
        "name": f"Website {wb}",
        "homepage_text_size": int(nl[0]),
        "homepage_image_size":int(nl[1]),
        "homepage_form_size":int(nl[2])
    }
    wb+=1
    websites.append(web)

for website in websites:
    
   
    serve_chunk(website["homepage_text_size"])
    

    serve_chunk(website["homepage_image_size"])

    serve_chunk(website["homepage_form_size"])


    # Check if the website has loaded within the maximum load time
    total_load_time = (website["homepage_text_size"] + website["homepage_image_size"]+website["homepage_form_size"]) / mspeed
    print(str(website["homepage_text_size"] / mspeed)+","+ str(website["homepage_image_size"] / mspeed)+","+str(website["homepage_form_size"] / mspeed))
    if total_load_time > mloadtime:
        print(f"{website['name']} took too long to load!")
    else:
        pass


