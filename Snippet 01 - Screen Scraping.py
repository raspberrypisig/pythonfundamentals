from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://www.melbpc.org.au/interest-groups-resources/sig-list/')
sig_elements = browser.find_elements_by_xpath(
    '(//table//tr/td)[.//text() = "SIG"]/following-sibling::td')
#unique_sigs = set('')
#for e in sig_elements:
#    unique_sigs.add(e.text)
unique_sigs = set([e.text for e in sig_elements])
sortedsigs = list(unique_sigs)
sortedsigs.sort()
for sig in sortedsigs:
    print(sig)
print('The number of SIGs at melbpc: ', len(unique_sigs))
browser.close()
