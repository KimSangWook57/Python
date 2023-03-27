# IQR 용어
# Q1: 제1사분위수
# Q3: 제3사분위수
# IQR: 제3사분위수에서 제1사분위수를 뺀 값으로서 데이터의 중간 50% 범위를 나타내는 값

# 이상치의 조건
# 일반적으로 Q1 - 1.5 * IQR 보다 작거나 Q3 + 1.5 * IQR 보다 큰 값을 가지는 데이터로 판단

# 방법
# 제1사분위수(Q1)와 제3사분위수(Q3)를 구합니다.
# IQR을 구합니다. (IQR = Q3 - Q1)
# 이상치의 상한과 하한을 구합니다.
# 이상치의 하한: Q1 - 1.5 * IQR
# 이상치의 상한: Q3 + 1.5 * IQR
# 이상치 데이터를 골라냅니다. (하한보다 작거나 상한보다 큰 값)

import pandas as pd

# 데이터 파일 경로
data_path = '일별평균대기오염도_2022.csv'

# CSV 파일 읽기
df = pd.read_csv(data_path, encoding='cp949')

# 필요한 필드 추출
df = df[['측정일시', '측정소명', '미세먼지농도(㎍/㎥)', '초미세먼지농도(㎍/㎥)']]

# 결측치 처리
df = df.dropna()

# 측정일시 컬럼의 데이터 타입을 datetime으로 변경
df['측정일시'] = pd.to_datetime(df['측정일시'], format='%Y%m%d')

# 이상치를 모아서 result.csv 파일로 저장
# 1사분위
q1_pm10 = df['미세먼지농도(㎍/㎥)'].quantile(0.25)
# 3사분위
q3_pm10 = df['미세먼지농도(㎍/㎥)'].quantile(0.75)
iqr_pm10 = q3_pm10 - q1_pm10
# 1사분위
q1_pm25 = df['초미세먼지농도(㎍/㎥)'].quantile(0.25)
# 3사분위
q3_pm25 = df['초미세먼지농도(㎍/㎥)'].quantile(0.75)
iqr_pm25 = q3_pm25 - q1_pm25
# 조건에 해당하는 행 뽑아내기.
outlier_df = df[((df['미세먼지농도(㎍/㎥)'] < q1_pm10 - 1.5 * iqr_pm10) | (df['미세먼지농도(㎍/㎥)'] > q3_pm10 + 1.5 * iqr_pm10))
                &
                ((df['초미세먼지농도(㎍/㎥)'] < q1_pm25 - 1.5 * iqr_pm25) | (df['초미세먼지농도(㎍/㎥)'] > q3_pm25 + 1.5 * iqr_pm25))]

outlier_df.to_csv('result.csv', index=False, encoding='utf-8-sig')



