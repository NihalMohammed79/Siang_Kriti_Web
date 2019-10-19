from django import template
import urllib.parse
register = template.Library()
import random

@register.filter
def remove_us(value):
	return (" ".join(value.split("_"))).title()

@register.filter
def urlencode(value):
	return urllib.parse.quote_plus(value)

@register.filter
def map_enum(value):
	dic = {'pr_team':'PR Team', 'another_techrep':'Another Techrep', 'media':'Social Media', 'friend_at_IITG':'Friend At IITG', 'already_knew':'Already Knew' , 'raspberry_pi':'Raspberry Pi' , 'ml_ai':'ML AI' , 'android_appdev':'Android App', 'stock_market':'Stock Market' , 'auto_ic':'Auto IC', 'game_dev':'Game Dev' , 'bridge_design': 'Bridge Design' , 'sixth_sense_robotics':'Sixth Sense Robotics' , 'ethical_hacking':'Ethical ethical_hacking' , 'social_media_seo':'Social Media Seo'}
	if value in dic.keys():
		return dic[value]
	return (" ".join(value.split("_"))).title()

@register.simple_tag
def random_loader():
	li = ["Please Wait… Activating your internet superpowers","280K has got to be enough for everyone!","Please Wait… You Have Gotten Better At Loading! (15)","Please Wait… Teaching Hindi to our A.I.","Please Wait… PS- Does Anyone Actually Read This?","Please Wait… Going the distance","Loading the Loading message","Load failed. retrying with --prayer…","Water detected on drive C: , Please wait. Spin dry commencing.","Yes there really are magic elves with an abacus working frantically in here!","Please Wait… Charging drone batteries","Please Wait… Setting up Business Conference","Please Wait… Getting lectures ready","Please Wait… Sacrificing a resistor to the machine gods","Please Wait… Locating the required gigapixels to render","Please Wait… The bits are flowing slowly today","Please Wait… BB8 is communicating with the servers","Please Wait… Time is an illusion. Loading time doubly so","Please Wait… Entering cheat codes","Preparing to host you, please wait…","Bringing the future to you, please wait…","Hold up… Getting rid of your FOMO","Satisfying our sponsors… Please wait"]
	return random.choice(li)

@register.filter
def get_attr(obj,value):
	return getattr(obj,value)

@register.filter
def get_amount(obj):
    return obj.amount_new()