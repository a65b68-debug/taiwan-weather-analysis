# 台灣天氣資料分析系統
# Version 4：中央氣象署 Open Data API
# 功能：取得臺北測站即時氣象觀測資料

import requests
import matplotlib.pyplot as plt

# =========================================
# API 設定
# =========================================

# 請使用自己的中央氣象署 API 授權碼
# 為避免洩漏個人 API Key，本專案不公開實際授權碼
API_KEY = "YOUR_CWA_API_KEY"

url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0001-001"

params = {
    "Authorization": API_KEY,
    "format": "JSON"
}

# =========================================
# 取得中央氣象署 Open Data
# =========================================

response = requests.get(url, params=params)

if response.status_code != 200:
    print("API 連線失敗：", response.status_code)
    raise SystemExit

data = response.json()

stations = data["records"]["Station"]

print("取得測站數量：", len(stations))

# =========================================
# 尋找臺北測站
# =========================================

taipei_station = None

for station in stations:
    if station["StationName"] == "臺北":
        taipei_station = station
        break

if taipei_station is None:
    print("找不到臺北測站")
    raise SystemExit

# =========================================
# 解析氣象資料
# =========================================

weather = taipei_station["WeatherElement"]

temperature = float(weather["AirTemperature"])
humidity = float(weather["RelativeHumidity"])
wind_speed = float(weather["WindSpeed"])

observation_time = taipei_station["ObsTime"]["DateTime"]

print("=== 臺北即時氣象資料 ===")
print("測站名稱：", taipei_station["StationName"])
print("測站代碼：", taipei_station["StationId"])
print("觀測時間：", observation_time)
print("溫度：", temperature, "°C")
print("相對濕度：", humidity, "%")
print("風速：", wind_speed, "m/s")

# =========================================
# 即時氣象資訊卡
# =========================================

plt.figure(figsize=(9, 7))
plt.axis("off")

plt.text(
    0.5, 0.92,
    "Taipei Real-Time Weather",
    ha="center",
    fontsize=22,
    fontweight="bold"
)

plt.text(
    0.20, 0.68,
    f"{temperature:.1f} °C\nTemperature",
    ha="center",
    fontsize=18
)

plt.text(
    0.50, 0.68,
    f"{humidity:.0f} %\nHumidity",
    ha="center",
    fontsize=18
)

plt.text(
    0.80, 0.68,
    f"{wind_speed:.1f} m/s\nWind Speed",
    ha="center",
    fontsize=18
)

plt.text(
    0.5, 0.42,
    f"Observation Time\n{observation_time}",
    ha="center",
    fontsize=14
)

plt.text(
    0.5, 0.20,
    "Data Source\nCentral Weather Administration Open Data",
    ha="center",
    fontsize=12
)

plt.savefig(
    "taipei_weather_card.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()
