from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://jeremydomasian.github.io/supercalc_v1-4/SuperCalc-v1.html')

oneElem = browser.find_element_by_name('one')
oneElem.click()

plusElem = browser.find_element_by_name('plus')
plusElem.click()

twoElem = browser.find_element_by_name('two')
twoElem.click()

equalElem = browser.find_element_by_name('DoIt')
equalElem.click()

clearElem = browser.find_element_by_name('clear')
clearElem.click()

twoElem = browser.find_element_by_name('two')
twoElem.click()

plusElem = browser.find_element_by_name('plus')
plusElem.click()

fourElem = browser.find_element_by_name('four')
fourElem.click()

equalElem = browser.find_element_by_name('DoIt')
equalElem.click()

# if viewing area equals 6 then print test successful 
# else test fail

#valueInputElem = inputElem.get_attribute('value')

inputElem = browser.find_element_by_name('Input')
valueInputElem = inputElem.get_attribute('value')

if valueInputElem != 5: 
	print('Test Successful')
else:
	print('Fail')

fiveElem = browser.find_element_by_name('five')
fiveElem.click()

minusElem = browser.find_element_by_name('minus')
minusElem.click()

twoElem = browser.find_element_by_name('two')
twoElem.click()

equalElem = browser.find_element_by_name('DoIt')
equalElem.click()

inputElem = browser.find_element_by_name('Input')
valueInputElem = inputElem.get_attribute('value')

if valueInputElem != 5: #this worked
	print('Test Successful')
else:
	print('Fail')

clearElem = browser.find_element_by_name('clear')
clearElem.click()








