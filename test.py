import vk_api

def captcha_handler(captcha):
  print("Enter captcha code " + captcha.get_url())
#   return captcha.try_again(key)

vk_session = vk_api.VkApi('instagram.man1373@gmail.com', '(11a12b13c14d15e16F)', captcha_handler = captcha_handler)
vk_session.auth()
vk = vk_session.get_api()
# try:

# except vk_api.AuthError as error_msg:
#   print(error_msg)
