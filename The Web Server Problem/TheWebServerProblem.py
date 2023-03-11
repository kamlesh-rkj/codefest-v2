import time
f=open("data.txt","r")
mspeed = 2
mloadtime = 60
def serve_chunk(data_size):
    chunk_size = 2.5 if data_size <= 5 else 4
    num_chunks = data_size / chunk_size
    for i in range(int(num_chunks)):
        time.sleep(chunk_size / mspeed)
        print(f"Serving  {i+1} of {num_chunks} ({chunk_size} MB)...")

websites = []
wb=1
for i in f.readlines():
    nl=i.split()
    print(nl)
    web={
        
        "name": f"Website {wb}",
        "homepage_text_size": int(nl[0]),
        "homepage_image_size":int(nl[1]),
        "homepage_form_size":int(nl[2])
    }
    wb+=1
    websites.append(web)


# Iterate over each website and serve its pages
for website in websites:
    print(f"Serving {website['name']}...")
    
    # Serve the homepage text content
    serve_chunk(website["homepage_text_size"])
    
    # Serve the homepage images
    serve_chunk(website["homepage_image_size"])
    
    
    # Check if the website has loaded within the maximum load time
    total_load_time = (website["homepage_text_size"] + website["homepage_image_size"]) / mspeed
    if total_load_time > mloadtime:
        print(f"{website['name']} took too long to load!")
    else:
        print(f"{website['name']} loaded successfully within {total_load_time} seconds.")

