# 台灣天氣資料分析系統
# Version 3：溫度、雨量與趨勢圖分析

import matplotlib.pyplot as plt

# 台北連續 7 天的氣象資料
days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]

temperatures = [26, 28, 29, 27, 30, 31, 28]
rainfall = [0, 5.5, 12, 0, 3.5, 25, 8]

# --------------------
# 溫度資料分析
# --------------------

average_temp = sum(temperatures) / len(temperatures)
highest_temp = max(temperatures)
lowest_temp = min(temperatures)

# --------------------
# 雨量資料分析
# --------------------

total_rainfall = sum(rainfall)
average_rainfall = sum(rainfall) / len(rainfall)
highest_rainfall = max(rainfall)

# --------------------
# 顯示分析結果
# --------------------

print("=== 台灣天氣資料分析 ===")
print("觀測地區：台北")

print("\n--- 溫度分析 ---")
print("7天溫度：", temperatures)
print("平均溫度：", round(average_temp, 1), "°C")
print("最高溫度：", highest_temp, "°C")
print("最低溫度：", lowest_temp, "°C")

print("\n--- 雨量分析 ---")
print("7天雨量：", rainfall)
print("總雨量：", total_rainfall, "mm")
print("平均雨量：", round(average_rainfall, 1), "mm")
print("最大單日雨量：", highest_rainfall, "mm")

# --------------------
# 圖表 1：溫度趨勢圖
# --------------------

plt.figure(figsize=(9, 5))

plt.plot(
    days,
    temperatures,
    marker="o"
)

plt.title("Taipei 7-Day Temperature Trend")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.tight_layout()
plt.savefig("temperature_trend.png")
plt.show()

# --------------------
# 圖表 2：每日雨量圖
# --------------------

plt.figure(figsize=(9, 5))

plt.bar(
    days,
    rainfall
)

plt.title("Taipei 7-Day Rainfall")
plt.xlabel("Day")
plt.ylabel("Rainfall (mm)")

plt.tight_layout()
plt.savefig("rainfall_chart.png")
plt.show()
