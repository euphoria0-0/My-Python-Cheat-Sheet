N = 3000
w = 2

node = pd.read_csv(f2) # 지역 코드와 x,y좌표, 지역 
data = pd.read_csv(f1) # 출발, 도착, value
data = data.sort_values(["value"], ascending=[False])[:N]

# 베이스 지도
m = folium.Map(
location=[37.57,127],
zoom_start=11.5
)

# 매핑
for i, r in df.iterrows():
	start = tuple(node[node['code'] == r['출발지']][['y','x']].iloc[0])
	end = tuple(node[node['code'] == r['도착지']][['y','x']].iloc[0])
	
	# 포인트
	for p in [start, end]:
		folium.Circle(
			location=p, radius=30, color='white', weight=0.5, 
			fill_opacity=0.4, fill_color='red', fill=True,
			popup=str(node[node['code'] == r['출발지']]['지역이름']) # 인코딩 확인 필요
		).add_to(m)
	
	# 경로
	folium.PolyLine(
		locations=[start, end],
		weight = r['value']/100*w,
		color='blue',
		opacity=0.5,
	).add_to(m)
	
now=datetime.now().isoformat()[5:-10].replace('-','').replace(':','')
m.save(f+now+'.html')
