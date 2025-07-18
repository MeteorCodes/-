<h1 align="center">
  👋 实时人口数据可视化分析 🦖
</h1>

<p align="center">
  <strong>⭐ china-population-clock-visualization 😸</strong>
</p>

<p align="left">
  <strong><a href="https://cpc.meteor.qzz.io/">👉实时人口数据可视化分析</a></strong>基于中国最新人口数据，构建了一个集成式实时可视化大屏，涵盖全国人口分布、性别比例、宗教统计、人口预测和历史数据变化等多个维度。通过图形化界面，帮助用户更直观地了解中国人口的现状与未来趋势，适用于教学演示、数据分析等多种场景。
</p>

</div>
<div align="center">
<img src="https://github.com/MeteorCodes/china-population-clock-visualization/blob/main/img/1.png" alt="示例图片" width="800" height="450">
</div>

<h3 align="left">
  <strong>🌟 关键特点</strong>
</h3>

<ul align="left">
    <li><strong>🗺️ 人口分布地图：基于各省人口数量进行颜色分级，支持直观对比</li>
    <li><strong>📊 人口性别比例图：以饼图展示当前全国男女性人口占比</li>
    <li><strong>⛪ 宗教统计数据：柱状图展示主要宗教信众数量及其人口占比</li>
    <li><strong>🔮 未来人口预测：环形极坐标图预测至2085年的人口变化趋势</li>
    <li><strong>📈 中国人口历史变化：1952年至今人口与增长率的时间序列图</li>
    <li><strong>🌍 资源修改：替换官方中国地图的JS代码，不用再城市后面加“省市”等次</li>
    <li><strong>🌈 渐变色彩视觉优化：使用热力图视觉强化不同区域的人口密度对比</li>
    <li><strong>🕒 实时数据同步机制：接入实时接口可实现动态更新</li>
</ul>

<h3 align="left">
  <strong>✨ 快速开始</strong>
</h3>

> [!Note]
> 请确保 **Python** 已经安装，测试使用Python 3.12.10版本；如果没有安装，请移步<a href="https://www.python.org/">Python</a>

1. **克隆我的仓库**

   ```bash
   https://github.com/MeteorCodes/china-population-clock-visualization.git
   cd china-population-clock-visualization
   ```

2. **运行charts.py并调整适合当前分辨率的可视化配置**

   ```bash
   python charts.py
   ```

🥇 打开".\template\test.html" <br>
🥈 任意按照自己的想法摆放图表 <br>
🥉 点击左上角的 “Save Config”，下载完成“chart_config.json”之后将他移动到 template 文件夹里面 

2. **执行finish.py可生成最终的可视化大屏**

   ```powershell
   python finish.py
   ```
🎉 可视化文件在 ".\template\deshboard.html"

<h3 align="left">
  <strong>🎯 部分细节</strong>
</h3>

<div align="center">
  <img src="https://github.com/MeteorCodes/china-population-clock-visualization/blob/main/img/2.png" alt="示例图片">
</div>
<div align="center">
  <img src="https://github.com/MeteorCodes/china-population-clock-visualization/blob/main/img/3.png" alt="示例图片">
</div>
<table width="100%" align="center">
  <tr>
    <td align="left">
      <img src="https://github.com/MeteorCodes/china-population-clock-visualization/blob/main/img/5.png" alt="示例图片" width="200" height="200">
    </td>
    <td align="right">
      <img src="https://github.com/MeteorCodes/china-population-clock-visualization/blob/main/img/6.png" alt="示例图片" width="200" height="200">
    </td>
  </tr>
</table>

<div align="center">
  <img src="https://github.com/MeteorCodes/china-population-clock-visualization/blob/main/img/4.png" alt="示例图片">
</div>

<h3 align="left">
  <strong>📁 目录结构</strong>
</h3>

```
|   charts.py
|   finish.py
|   get_data.py
|   main.py
|   structure.txt
|   upload_table.py
|   
+---data
|       hongheiku_data.csv
|       population_clock_data.csv
|       population_forecast_histort.csv
|       population_histort.csv
|       religion_table.csv
|       
\---template
    |   chart_config.json
    |   deshboard.html
    |   test.html
    |   
    \---static
        \---js
            |   echarts.min.js
            |   jquery-ui.min.js
            |   jquery.min.js
            |   ResizeSensor.js
            |   
            \---maps
                    china.js
                    
```
<h3 align="left">
  <strong>🚩 至此结束啦！动动手为我的项目点个 ⭐star⭐ 吧</strong>
</h3>

<p align="left">
  <strong><a href="https://0meteor0.pythonanywhere.com/">👉 Meteor官网</a></strong>
  <br>
  <strong><a href="https://hzuzowss.ap-northeast-1.clawcloudrun.com/">👉 Meteor博客</a></strong>
</p>
