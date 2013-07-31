'''
Efforts on monitor the price of a product at Amazon
'''
import os
import urllib2
import lxml.html as lh
from lxml.html.clean import clean_html
from lxml import etree
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#from bs4 import BeautifulSoup

#productUrl = "http://www.amazon.com/gp/product/B00C2F2AC2/ref=s9_simh_gw_p147_d38_i3?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=center-5&pf_rd_r=1SEYP9NA2Y0JM00XKFQQ&pf_rd_t=101&pf_rd_p=470938731&pf_rd_i=507846"
#productUrl="http://www.amazon.com/gp/product/B009AO6GZ0/ref=s9_al_gw_g200_ir03?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=center-2&pf_rd_r=1ECH01METX37AEYMFVD9&pf_rd_t=101&pf_rd_p=1564450042&pf_rd_i=507846"
#productUrl="http://www.amazon.com/gp/product/B007OZNZG0/ref=kin_dev_gw_dual_c?ie=UTF8&nav_sdd=aps&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=center-1&pf_rd_r=0S7FHM2254HN8SHS1DPX&pf_rd_t=101&pf_rd_p=1566092482&pf_rd_i=507846"
#productUrl="http://www.amazon.com/Sperry-Top-Sider-Authentic-Original-Sahara/dp/B000EPC4XW/ref=sr_1_1?s=shoes&ie=UTF8&qid=1371767099&sr=1-1"
#productUrl="http://www.amazon.com/Kingston-Digital-DataTraveler-101-Generation/dp/B004TS1J1I/ref=sr_1_1?ie=UTF8&qid=1371767147&sr=8-1&keywords=usb"
productUrl="http://www.amazon.com/dp/B007NLW3C2/ref=pe_309540_26725410_item"
source = lh.document_fromstring(urllib2.urlopen(productUrl).read())
#a= source.get_element_by_id('actualPriceValue')
price_list=source.find_class('priceLarge')
for price in price_list:
	print price.text

