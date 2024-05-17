# Make your own running race result page

Demo: https://laqieer.github.io/running_race/

## Guide

1. Query result on runchina and copy `timesToken`

https://www.runchina.org.cn/#/data/data-mgt/score-query

![image](https://github.com/laqieer/running_race/assets/8841957/7d034b5c-88aa-4667-92c5-925f8a791aa2)

https://www.runchina.org.cn/#/data/result-data?cardNo=`ID_CARD_NUMBER`&userName=`ID_CARD_NAME`&timesToken=`TIMES_TOKEN`

2. Config GitHub Action secrets

- `ID_CARD_NUMBER`
- `ID_CARD_NAME`
- `TIMES_TOKEN`

![image](https://github.com/laqieer/running_race/assets/8841957/8cbca29f-bb88-4c43-87e8-2a7a8191bcf0)

3. Run GutHub Action workflow

`Query results and deploy to Pages`

![image](https://github.com/laqieer/running_race/assets/8841957/0644c28e-00fc-4d74-a44b-5c0068a059b8)

Notice: If you see `成绩查询凭证已失效`, please refresh `timesToken`.
