#ExtractLattes
"""
Essa função recebe uma imagem e o dataframe com os símbolos 
do captcha que iremos quebrar.
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from BreakingCaptcha import *
from PIL import Image
from io import BytesIO
import base64
import os
import logging
import pandas as pd
import time

start_time = time.time()

logging.basicConfig(filename='./extract_lattes.log',level=logging.INFO)

logging.info('START TIME:'+str(start_time))

root_page   =  "http://buscatextual.cnpq.br/buscatextual/download.do?metodo=apresentar&idcnpq="
lista_cv    = list(pd.read_csv('lista_cv_matematica.csv',header=None,dtype=str,skiprows=1,usecols=[1])[1])
lista_cv    = lista_cv[0:2]

def Get_Captcha(ele_captcha,outputname):
    # get the captcha as a base64 string
    img_captcha_base64 = driver.execute_async_script("""
        var ele = arguments[0], callback = arguments[1];
        ele.addEventListener('load', function fn(){
          ele.removeEventListener('load', fn, false);
          var cnv = document.createElement('canvas');
          cnv.width = this.width; cnv.height = this.height;
          cnv.getContext('2d').drawImage(this, 0, 0);
          callback(cnv.toDataURL('image/jpeg').substring(22));
        }, false);
        ele.dispatchEvent(new Event('load'));
        """, ele_captcha)

    # save the captcha to a file
    with open(outputname, 'wb') as f:
        f.write(base64.b64decode(img_captcha_base64))




options = Options()
# options.headless = True

profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) # custom location
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', '/home/davi/Dropbox/FGV/EMAp/DataScience/BreakingCaptcha/cvs/')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')

driver = webdriver.Firefox(profile,options=options)
driver.set_script_timeout(10)

for cod_cv in lista_cv:
    url = root_page + cod_cv
    driver.get(url)
    for i in range(0,10):
        ele_captcha = driver.find_element_by_xpath("//img[contains(./@src, 'getImagemCaptcha')]")
        outputname = './captcha_correct/captcha_'+cod_cv+'.jpg'
        Get_Captcha(ele_captcha,outputname)
        previsao = BreakCaptcha(outputname)
        inputElement = driver.find_element_by_id("informado")
        try:
	        inputElement.send_keys(previsao)
	        driver.find_element_by_id('btn_validar_captcha').click()
        except:
        	time.sleep(1)
        check_download = os.path.isfile('./cvs/{}.zip'.format(cod_cv))
        print(check_download)
        if check_download == True:
            logging.info('{}:SUCESSO'.format(cod_cv))
            break
        if i == 9:
            logging.warning("{}:FALHOU".format(cod_cv))
        time.sleep(1+i/10)
driver.quit()

logging.info('DURATION:'+str(start_time - time.time()))



