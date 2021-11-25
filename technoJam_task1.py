my_list = []

sample_url = "http://google.com"

for i in sample_url:
    my_list.append(i)

reverse_url = sample_url[::-1]

top_level_doamin = sample_url[-4:]

ommiting = sample_url[7:]

ommiting_again = sample_url = [7:-4]

lst = sample_list[::-1]

print(reverse_url) # Reverse the url
print(top_level_domain) # Get the top level domain
print(ommiting) # Print the url without the http://
print(ommiting_again) # Print the url without the http:// or the top level domain
print() #list[start:end:stop]
