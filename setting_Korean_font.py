## For Colab Notebooks
#참고: https://colab.research.google.com/github/nicewook/datascience_exercise/blob/master/korean_font_on_matplotlib.ipynb#scrollTo=nzZ6wGntXBrP
# 1. 나눔고딕 인스톨
!apt-get update -qq
!apt-get install fonts-nanum* -qq
# 2. 라이브러리 인스톨
from PIL import Image
import platform
import matplotlib as mpl  # 기본 설정 만지는 용도
import matplotlib.pyplot as plt  # 그래프 그리는 용도
import matplotlib.font_manager as fm  # 폰트 관련 용도
# 3. 글꼴 설정
# 글꼴 경로 가져오기
path = '/usr/share/fonts/truetype/nanum/NanumSquareR.ttf'  # font 나눔스퀘어 for Colab Notebooks
path = 'C:/Windows/Fonts/malgun.ttf' # font 맑은 고딕 for Windows
font_name = fm.FontProperties(fname=path, size=10).get_name()
print(font_name)
plt.rc('font', family=font_name)
# 4. 추가 설치된 폰트 인식 및 마이너스 기호 설정
fm._rebuild()
mpl.rcParams['axes.unicode_minus'] = False
