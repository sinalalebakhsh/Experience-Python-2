import requests



list_exp = ['https://salamatiyeshoma.com', 'https://salamatiyeshoma.com/admin']


for find_admin_page in list_exp:
    try:
        number_response = requests.get(find_admin_page).status_code
        if number_response in range(0,1000):
            print(f'{find_admin_page} = {number_response}')
    except:
        print('ConnectionError')




