#!/usr/bin/python


import mechanize

loginId = 'ENTER YOUR LOGIN ID HERE'
loginPass = 'ENTER YOUR LOGIN PASSWORD HERE'

browser = mechanize.Browser()
browser.open('http://172.16.16.16/24online/webpages/client.jsp?fromlogout=true')
browser.select_form(name = 'clientloginform')
try:
    browser.form['username'] = loginId
except:
    browser.form['username1'] = loginId
browser.form['password'] = loginPass
browser.submit()

