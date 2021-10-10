#coding=utf-8
from selenium import webdriver
import time
import re
from selenium.webdriver.common.keys import Keys 
from urllib.request import urlopen
import getpass
import wmi
import os
import re
import sys
import winreg
import zipfile
from pathlib import Path
import requests
import random

class seting():
    def get_chrome_version():
        version_re = re.compile(r'^[1-9]\d*\.\d*.\d*')
        """通过注册表查询Chrome版本信息: HKEY_CURRENT_USER\SOFTWARE\Google\Chrome\BLBeacon: version"""
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'SOFTWARE\Google\Chrome\BLBeacon')
            value = winreg.QueryValueEx(key, 'version')[0]
            return version_re.findall(value)[0]
        except WindowsError as e:
            return '0.0.0'  # 没有安装Chrome浏览器
    def get_chrome_driver_version():
        try:
            result = os.popen('chromedriver.exe --version').read()
            version = result.split(' ')[1]
            return '.'.join(version.split('.')[:-1])
        except Exception as e:
            return '0.0.0'  # 没有安装ChromeDriver
    def get_latest_chrome_driver(chrome_version):
        python_root = Path(sys.executable).parent
        base_url = 'http://npm.taobao.org/mirrors/chromedriver/'
        url = f'{base_url}LATEST_RELEASE_{chrome_version}'
        latest_version = requests.get(url).text
        download_url = f'{base_url}{latest_version}/chromedriver_win32.zip'
        # 下载chromedriver zip文件
        response = requests.get(download_url)
        local_file = python_root / 'chromedriver.zip'
        with open(local_file, 'wb') as zip_file:
            zip_file.write(response.content)

        # 解压缩zip文件到python安装目录
        f = zipfile.ZipFile(local_file, 'r')
        for file in f.namelist():
            f.extract(file, python_root)
        f.close()

        local_file.unlink()  # 解压缩完成后删除zip文件
    def check_chrome_driver_update():
        chrome_version = seting.get_chrome_version()
        driver_version = seting.get_chrome_driver_version()
        if chrome_version == driver_version:
            print('不需要更新')
        else:
            try:
                seting.get_latest_chrome_driver(chrome_version)
            except Exception as e:
                print(f'更新失败: {e}')
    def pb(str):
        for i in range(1, 101):
            print("\r", end="")
            print(' '+str+"{}%: ".format(i), "▋" * (i //2), end="")
            sys.stdout.flush()
            j=random.randint(1,10 )
            if(j==5):
                time.sleep(1)
            time.sleep((random.randint(1, 10)/50))
    
def ip(net):
    # Obtain network adaptors configurations
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

    # First network adaptor
    nic = nic_configs[0]

    # IP address, subnetmask and gateway values should be unicode objects
    ip = ('192.168.'+str(net)+'.101')
    subnetmask = u'255.255.255.0'
    gateway = ('192.168.'+str(net)+'.1')

    # Set IP address, subnetmask and default gateway
    # Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
    nic.EnableStatic(IPAddress=[ip],SubnetMask=[subnetmask])
    nic.SetGateways(DefaultIPGateway=[gateway])

def tool():
    while(1):
        print("""
        {:<}
        {:<}
        {:<}
        """.format('1.ip设置','2.dhcp服务','3.激活'))
        mode=input('输入操作\n')
        if(mode=='3'):
            ip(2)
        elif(mode=='1'):
            ip(1)
        elif(mode=='2'):
            dhcp()
        elif(mode=='4'):
            print('1')
        elif(mode=='5'):
            set_m()
        elif(mode=='6'):
            set_5g()
        elif(mode=='7'):
            set_2g()
        elif(mode=='8'):
            creak()
        else:
            print('输入错误')

def cod():
    while(1):
        
        try:
            if(open('c:/windows/pass','r').read()=='1'):
                tool()
           
        except:
            while True:
                while True:
                    try:
                        url = 'https://baidu.com/'
                        resp = urlopen(url)
                        code = resp.getcode()
                        if(resp.getcode()==200):
                            break
                    except:
                        time.sleep(1)
                        print("\r", end="")
                        print("等待联网。。。",end="")
                        sys.stdout.flush()
                pa=getpass.getpass("\npassword:")
                if(pa=='hhd123456'):
                    open('c:/windows/pass','w').write('1')
                    break
                else:
                    print('错误')
                    continue
            
def set_wifi():
    opt = webdriver.ChromeOptions()   #创建浏览
    #opt.set_headless() #无窗口模式
    

    driver = webdriver.Chrome(options=opt)  #创建浏览器对象
    driver.minimize_window()
    driver.maximize_window()
    driver.get('http://melogin.cn/') #打开网页
      
    time.sleep(2)   
    
    
    driver.find_element_by_xpath("//ul[@id='selOptsUlnetModeSel']/li[@class='option'][1]").click()
    time.sleep(1)
    accunt=input("请输入账号（IP156...):\n")
    pwd=input('请输入宽带密码：\n')
    time.sleep(1)
    driver.find_element_by_xpath("//input[@id='pppoeAccount']").send_keys(Keys.CONTROL,'a')
    driver.find_element_by_xpath("//input[@id='pppoeAccount']").send_keys(Keys.BACKSPACE)
    driver.find_element_by_xpath("//input[@id='pppoeAccount']").send_keys(accunt)
    time.sleep(1)
    driver.find_element_by_xpath("//input[@id='pppoePasswd']").send_keys(Keys.CONTROL,'a')
    driver.find_element_by_xpath("//input[@id='pppoePasswd']").send_keys(Keys.BACKSPACE)
    driver.find_element_by_xpath("//input[@id='pppoePasswd']").send_keys(pwd)
    time.sleep(1)
    driver.find_elements_by_xpath("//i[@class='btnR']").click()
    seting.pb('正在拨号')
    print('{:*^50}'.format('连接成功，请继续操作'))
    ssd=input('输入wifi名称： ')
    pwd=input('输入密码： ')
    time.sleep(0.1)
    print("\r", end="")
    print(" 正在强制修改中{}%: ".format(20), "▋" * (20 //2), end="")
    sys.stdout.flush()
    driver.find_element_by_xpath("//input[@id='wzdWirelessName2G']").send_keys(Keys.CONTROL,'a')
    driver.find_element_by_xpath("//input[@id='wzdWirelessName2G']").send_keys(Keys.BACKSPACE)
    driver.find_element_by_xpath("//input[@id='wzdWirelessName2G']").send_keys(ssd)
    time.sleep(1)
    print("\r", end="")
    print(" 正在强制修改中{}%: ".format(40), "▋" * (40 //2), end="")
    sys.stdout.flush()
    driver.find_element_by_xpath("//input[@id='wzdWirelessPwd2G']").send_keys(Keys.CONTROL,'a')
    driver.find_element_by_xpath("//input[@id='wzdWirelessPwd2G']").send_keys(Keys.BACKSPACE)
    driver.find_element_by_xpath("//input[@id='wzdWirelessPwd2G']").send_keys(pwd)
    time.sleep(1)
    print("\r", end="")
    print(" 正在强制修改中{}%: ".format(60), "▋" * (60 //2), end="")
    sys.stdout.flush()
    driver.find_element_by_xpath("//input[@id='wzdWirelessName5G']").send_keys(Keys.CONTROL,'a')
    driver.find_element_by_xpath("//input[@id='wzdWirelessName5G']").send_keys(Keys.BACKSPACE)
    driver.find_element_by_xpath("//input[@id='wzdWirelessName5G']").send_keys(ssd,'-5G')
    time.sleep(1)
    print("\r", end="")
    print(" 正在强制修改中{}%: ".format(80), "▋" * (80 //2), end="")
    sys.stdout.flush()
    if(driver.find_elements_by_xpath("//input[@id='samePwd']").is_selected()==False):
        driver.find_elements_by_xpath("//input[@id='samePwd']").click()
    time.sleep(1)
    driver.find_elements_by_xpath("//i[@class='btnR']").click()
    print("\r", end="")
    print(" 正在强制修改中{}%: ".format(100), "▋" * (100 //2), end="")
    sys.stdout.flush()
    print('修改成功！！请手动连接wifi')

def dhcp():
    while True:
        try:
            url = 'http://mlogin.cn/'
            resp = urlopen(url)
            code = resp.getcode()
        except:
            print('路由器连接错误')
            continue    
    opt = webdriver.ChromeOptions()   #创建浏览
    #opt.set_headless() #无窗口模式
    driver = webdriver.Chrome(options=opt)  #创建浏览器对象
    driver.minimize_window()
    driver.get('http://melogin.cn/') #打开网页
      
    time.sleep(2)    
    
    driver.find_element_by_id('lgPwd').send_keys("123456") 
    driver.find_element_by_id('loginSub').send_keys(Keys.ENTER)
    time.sleep(3)
    driver.find_element_by_xpath("//div/div[@id='head']/ul[@id='headFunc']/li[2]").click()
    driver.maximize_window() 
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[@id='Con']/div[@id='highSetCon']/div[@id='hcCon']/div[@id='hsMenu']/div[@id='highSetMenu']/ul[@class='menuUl'][1]/li[@id='netWorkData_menu3']").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[@id='Con']/div[@id='highSetCon']/div[@id='hcCon']/fieldset[@class='hsFieldset']/div[@id='hcDetail']/div[@id='hcCo']/div[@class='title titleA']/div[@id='switchCon']/i[@class='switchBg']").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[@id='Con']/div[@id='highSetCon']/div[@id='hcCon']/fieldset[@class='hsFieldset']/div[@id='hcDetail']/div[@id='hcCo']/div[@class='block']/div[@class='blockFuncA']/span[@id='save']/i[@class='subBtnLg']]").click()
    time.sleep(10)

    url = 'http://melogin.cn/'
    resp = urlopen(url)
    code = resp.getcode()
    while(1):
        if(resp.getcode()==200):
            break;

if __name__=="__main__":
    seting.check_chrome_driver_update()
    cod()
    
        
