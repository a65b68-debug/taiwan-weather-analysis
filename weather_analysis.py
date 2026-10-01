# 台灣天氣資料分析系統
# Version 1：溫度基本分析

# 台北連續 7 天的氣溫資料（攝氏）
temperatures = [26, 28, 29, 27, 30, 31, 28]

# 計算平均溫度
average_temp = sum(temperatures) / len(temperatures)

# 找出最高與最低溫度
highest_temp = max(temperatures)
lowest_temp = min(temperatures)

# 顯示分析結果
print("=== 台灣天氣資料分析 ===")
print("觀測地區：台北")
print("7天溫度：", temperatures)
print("平均溫度：", round(average_temp, 1), "°C")
print("最高溫度：", highest_temp, "°C")
print("最低溫度：", lowest_temp, "°C")
