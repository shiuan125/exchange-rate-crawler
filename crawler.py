import requests
from bs4 import BeautifulSoup

# 設定匯率頁面 URL
url = 'https://www.cathaybk.com.tw/cathaybk/personal/product/deposit/currency-billboard/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

# 發送請求
response = requests.get(url, headers=headers)
if response.status_code == 200:
    # 解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 先找到所有幣別卡片
    currency_cards = soup.find_all('div', class_='cubre-o-rateCard')
    
    # 遍歷卡片找到美元USD
    for card in currency_cards:
        # 檢查是否為美元USD卡片
        currency_name = card.find('div', class_='cubre-m-currency__name')
        if currency_name and '美元USD' in currency_name.text:
            # 在這個卡片中尋找數位通路優惠匯率
            rows = card.find_all('tr')
            for row in rows:
                name_cell = row.find('div', class_='cubre-m-rateTable__name')
                if name_cell and '數位通路優惠匯率' in name_cell.text:
                    # 獲取該行中的所有數值
                    rates = row.find_all('div')
                    # 第二個和第三個div包含買進和賣出價格
                    buy_rate = rates[1].text.strip()
                    sell_rate = rates[2].text.strip()
                    print(f"美元USD 數位通路優惠匯率 - 銀行買進: {buy_rate}, 銀行賣出: {sell_rate}")
                    
        elif  currency_name and '日圓JPY' in currency_name.text: 
            # 在這個卡片中尋找數位通路優惠匯率
            rows = card.find_all('tr')
            for row in rows:
                name_cell = row.find('div', class_='cubre-m-rateTable__name')
                if name_cell and '數位通路優惠匯率' in name_cell.text:
                    # 獲取該行中的所有數值
                    rates = row.find_all('div')
                    # 第二個和第三個div包含買進和賣出價格
                    buy_rate = rates[1].text.strip()
                    sell_rate = rates[2].text.strip()
                    print(f"日圓JPY 數位通路優惠匯率 - 銀行買進: {buy_rate}, 銀行賣出: {sell_rate}")
else:
    print("無法取得匯率頁面。")
    
input("按 Enter 鍵退出...")
