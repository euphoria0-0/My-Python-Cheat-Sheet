N = 3000
w = 2

data = pd.read_csv(f)

date = str(date).zfill(2)
df = df.sort_values(["value"], ascending=[False])[:N]

# 베이스 지도
m = folium.Map(
location=[37.57,127],
zoom_start=11.5
)

# 매핑
for ix, row in df.iterrows():
	start = tuple(nodes[nodes['code'] == row['출발지']][['y','x']].iloc[0])
	end = tuple(nodes[nodes['code'] == row['도착지']][['y','x']].iloc[0])
	
	# 포인트
	for p in [start, end]:
		folium.Circle(
			location=p, radius=30, color='white', weight=0.5, 
			fill_opacity=0.4, fill_color='red', fill=True,
			popup=str(nodes[nodes['code'] == row['출발지']]['지역이름'])
		).add_to(m)
	
	# 경로
	folium.PolyLine(
		locations=[start, end],
		weight = row['value']/100*w,
		color='blue',
		opacity=0.5,
	).add_to(m)
	
now=datetime.now().isoformat()[5:-10].replace('-','').replace(':','')
m.save(f+now+'.html')
