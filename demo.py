from instabot import Bot
from kcu import kjson

# bot = Bot()
# bot.login(username='lofi_dealer', password='kkrisi200')
# user_id = bot.get_user_id_from_username('pubity')

# kjson.save('test.json', bot.get_user_related_profiles(user_id))


import hashlib, hmac

key = '10484'

url = 'https://www.instagram.com/graphql/query/?variables={"user_id":"1431724849","include_chaining":true,"include_reel":true,"include_suggested_users":false,"include_logged_out_extras":false,"include_highlight_reels":true,"include_live_status":true}'

query = '{"user_id":"1431724849","include_chaining":true,"include_reel":true,"include_suggested_users":false,"include_logged_out_extras":false,"include_highlight_reels":true,"include_live_status":true}'

print(hmac.new(key.encode("utf-8"), query.encode("utf-8"), hashlib.md5).hexdigest())
print(hmac.new(query.encode("utf-8"), key.encode("utf-8"), hashlib.md5).hexdigest())
print(hmac.new(key.encode("utf-8"), url.encode("utf-8"), hashlib.md5).hexdigest())
print(hmac.new(url.encode("utf-8"), key.encode("utf-8"), hashlib.md5).hexdigest())


print('d4d88dc1500312af6f937f7b804c68c3')