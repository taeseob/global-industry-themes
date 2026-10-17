FONT = "'Noto Sans KR','Noto Sans CJK KR','Apple SD Gothic Neo','Malgun Gothic',sans-serif"
P = dict(sub='#EEEDFE', node='#CECBF6', stroke='#534AB7', text='#26215C')
B = dict(sub='#E6F1FB', node='#B5D4F4', stroke='#185FA5', text='#042C53')
T = dict(sub='#E1F5EE', node='#9FE1CB', stroke='#0F6E56', text='#04342C')
A = dict(sub='#FAEEDA', node='#FAC775', stroke='#854F0B', text='#412402')
W, H = 1100, 610
o = []
o.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}" role="img">')
o.append('<title>산업 테마 4층 구조</title><desc>사회 변화, 수요 테마, 핵심 부품, 기반의 4개 층과 층 사이의 수요 흐름</desc>')
o.append('<defs>')
for name, c in (('p', P), ('b', B), ('t', T), ('a', A)):
    o.append(f'<marker id="m{name}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M1 1L9 5L1 9z" fill="{c["stroke"]}"/></marker>')
o.append('</defs>')
o.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="16" fill="#FFFFFF"/>')

def layer_rect(x, y, w, h, c):
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{c["sub"]}" stroke="{c["stroke"]}" stroke-width="2"/>')

def label(x, y, c, lines):
    dy = 0
    for i, (txt, size, weight) in enumerate(lines):
        o.append(f'<text x="{x}" y="{y+dy}" font-size="{size}" font-weight="{weight}" fill="{c["text"]}">{txt}</text>')
        dy += size + 6

def node(x, y, w, c, txt, h=44, dashed=False, sub=None):
    fill = c['sub'] if dashed else c['node']
    da = ' stroke-dasharray="6 4"' if dashed else ''
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{c["stroke"]}" stroke-width="1.8"{da}/>')
    cx = x + w / 2
    if sub:
        o.append(f'<text x="{cx}" y="{y+h/2-3}" text-anchor="middle" font-size="15" font-weight="500" fill="{c["text"]}">{txt}</text>')
        o.append(f'<text x="{cx}" y="{y+h/2+13}" text-anchor="middle" font-size="12" fill="{c["text"]}">{sub}</text>')
    else:
        o.append(f'<text x="{cx}" y="{y+h/2}" dy="0.35em" text-anchor="middle" font-size="15" font-weight="500" fill="{c["text"]}">{txt}</text>')

# layer 1 (ㄱ shape)
o.append(f'<path d="M32 20 H1068 Q1080 20 1080 32 V308 Q1080 320 1068 320 H852 Q840 320 840 308 V136 Q840 124 828 124 H32 Q20 124 20 112 V32 Q20 20 32 20 Z" fill="{P["sub"]}" stroke="{P["stroke"]}" stroke-width="2"/>')
label(32, 48, P, [("1층 · 사회 변화", 16, 700), ("왜 돈이 움직이는가", 13, 400)])
o.append(f'<text x="858" y="150" font-size="13" font-weight="700" fill="{P["text"]}">에너지·기후</text>')
# layer 2
layer_rect(20, 150, 804, 170, B)
label(32, 178, B, [("2층 · 수요 테마", 16, 700), ("최종 수요가", 13, 400), ("생기는 곳", 13, 400)])
# layer 3
layer_rect(20, 350, 1060, 100, T)
label(32, 378, T, [("3층 · 핵심 부품", 16, 700), ("여러 수요 테마에", 13, 400), ("공급하는 부품", 13, 400)])
# layer 4
layer_rect(20, 480, 1060, 108, A)
label(32, 508, A, [("4층 · 기반", 16, 700), ("가장 아래의 병목", 13, 400)])

# edges first (under nodes)
def line(pts, c, dashed=False, mk=None):
    d = 'M' + ' L'.join(f'{x} {y}' for x, y in pts)
    da = ' stroke-dasharray="7 5"' if dashed else ''
    o.append(f'<path d="{d}" fill="none" stroke="{c["stroke"]}" stroke-width="{2.2 if dashed else 2.6}" stroke-linejoin="round"{da} marker-end="url(#m{mk})"/>')

def curve(p0, c, p1, col, mk):
    o.append(f'<path d="M{p0[0]} {p0[1]} Q{c[0]} {c[1]} {p1[0]} {p1[1]}" fill="none" stroke="{col["stroke"]}" stroke-width="2.6" marker-end="url(#m{mk})"/>')

# AI 묶음 테두리
o.append(f'<rect x="158" y="190" width="144" height="124" rx="10" fill="#D6E6F7" stroke="{B["stroke"]}" stroke-width="1.2"/>')
o.append(f'<text x="310" y="292" font-size="12" font-weight="700" fill="{B["text"]}">← AI 묶음</text>')

# purple (1층에서 출발)
line([(250,106),(232,194)], P, mk='p')          # 지능의 자동화 → AI 모델·서비스
line([(300,106),(345,194)], P, mk='p')          # 지능의 자동화 → 사이버보안
line([(335,106),(620,194)], P, True, 'p')       # 지능의 자동화 → 로봇(관찰)
line([(480,106),(450,194)], P, mk='p')          # 지정학 → 방산·우주
line([(515,106),(540,194)], P, mk='p')          # 지정학 → 조선·해운
line([(685,106),(665,194)], P, True, 'p')       # 인구 구조 → 로봇(관찰)
line([(740,106),(768,194)], P, mk='p')          # 인구 구조 → 바이오헬스
line([(1020,196),(1052,196),(1052,506)], P, mk='p')  # 기후 → 전력
line([(950,276),(950,506)], P, mk='p')               # 전기화 → 전력
line([(890,276),(890,402),(776,402)], P, mk='p')     # 전기화 → 배터리
# blue (2층에서 출발)
line([(230,244),(230,262)], B, mk='b')          # AI 모델·서비스 → AI 컴퓨팅 인프라 (AI 묶음 안의 전용 공급망)
line([(215,306),(225,376)], B, mk='b')          # AI 컴퓨팅 → 범용·전력 반도체
curve((280,306),(560,520),(796,520), B, 'b')     # AI 컴퓨팅 → 전력: 배터리와 간격을 두고 전력 상자 왼쪽으로 들어가는 곡선
line([(470,244),(668,376)], B, mk='b')          # 방산 → 배터리
line([(655,244),(694,376)], B, True, 'b')       # 로봇 → 배터리
line([(420,244),(420,506)], B, mk='b')          # 방산 → 핵심광물
# green (3층에서 출발)
line([(300,424),(372,506)], T, mk='t')
line([(682,424),(472,506)], T, mk='t')
# amber (4층 안)
line([(800,534),(486,534)], A, mk='a')

# nodes
node(200, 62, 140, P, '지능의 자동화')
node(430, 62, 130, P, '지정학·안보')
node(660, 62, 110, P, '인구 구조')
node(860, 174, 160, P, '기후의 물리적 변화')
node(860, 232, 140, P, '전기화·탈탄소')
node(165, 200, 130, B, 'AI 모델·서비스')
node(165, 266, 130, B, 'AI 컴퓨팅 인프라', h=40)
node(305, 200, 88, B, '사이버보안')
node(401, 200, 90, B, '방산·우주')
node(499, 200, 90, B, '조선·해운')
node(597, 200, 120, B, '로봇·휴머노이드', dashed=True, sub='관찰 테마')
node(725, 200, 92, B, '바이오헬스')
node(165, 380, 170, T, '범용·전력 반도체')
node(650, 380, 122, T, '배터리')
node(340, 510, 140, A, '핵심광물')
node(800, 510, 260, A, '전력·에너지 인프라')
o.append('</svg>')
open(__import__('os').path.join(__import__('os').path.dirname(__file__), 'layer-map.svg'), 'w', encoding='utf-8').write('\n'.join(o))
print('written')
