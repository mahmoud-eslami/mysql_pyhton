import requests

def sed_sms():
    my_api_key = '2B617032736638466D3858592B7538444F335652764E45677A76323373********'
    url = 'https://api.kavenegar.com/v1/%s/sms/send.json' % my_api_key
    mydata = {'receptor': '09115198888','message': 'تست سرویس پیامکی دبستان'}
    req = requests.post(url,data=mydata)
    print(req.text)

sed_sms()