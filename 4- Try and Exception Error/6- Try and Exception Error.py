import requests

find_admin_page = ''

try:
    find_admin_page = requests.get('https://salamatiyeshoma.com')
# except requests:
#     print('your cannection is lost')
except:
    print('ConnectionError')
    
print(find_admin_page)


