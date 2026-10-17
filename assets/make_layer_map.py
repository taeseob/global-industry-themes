FONT = "'Noto Sans KR','Noto Sans CJK KR','Apple SD Gothic Neo','Malgun Gothic',sans-serif"
P = dict(sub='#EEEDFE', node='#CECBF6', stroke='#534AB7', text='#26215C')
B = dict(sub='#E6F1FB', node='#B5D4F4', stroke='#185FA5', text='#042C53')
T = dict(sub='#E1F5EE', node='#9FE1CB', stroke='#0F6E56', text='#04342C')
A = dict(sub='#FAEEDA', node='#FAC775', stroke='#854F0B', text='#412402')
W, H = 1100, 590
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
o.append(f'<path d="M32 20 H1068 Q1080 20 1080 32 V288 Q1080 300 1068 300 H852 Q840 300 840 288 V136 Q840 124 828 124 H32 Q20 124 20 112 V32 Q20 20 32 20 Z" fill="{P["sub"]}" stroke="{P["stroke"]}" stroke-width="2"/>')
label(32, 48, P, [("1층 · 사회 변화", 16, 700), ("왜 돈이 움직이는가", 13, 400)])
o.append(f'<text x="858" y="150" font-size="13" font-weight="700" fill="{P["text"]}">에너지·기후</text>')
# layer 2
layer_rect(20, 150, 800, 150, B)
label(32, 178, B, [("2층 · 수요 테마", 16, 700), ("최종 수요가", 13, 400), ("생기는 곳", 13, 400)])
# layer 3
layer_rect(20, 330, 1060, 100, T)
label(32, 358, T, [("3층 · 핵심 부품", 16, 700), ("여러 수요 테마에", 13, 400), ("공급하는 부품", 13, 400)])
# layer 4
layer_rect(20, 460, 1060, 108, A)
label(32, 488, A, [("4층 · 기반", 16, 700), ("가장 아래의 병목", 13, 400)])

# edges first (under nodes)
def line(pts, c, dashed=False, mk=None):
    d = 'M' + ' L'.join(f'{x} {y}' for x, y in pts)
    da = ' stroke-dasharray="7 5"' if dashed else ''
    o.append(f'<path d="{d}" fill="none" stroke="{c["stroke"]}" stroke-width="{2.2 if dashed else 2.6}" stroke-linejoin="round"{da} marker-end="url(#m{mk})"/>')

def curve(p0, c, p1, col, mk):
    o.append(f'<path d="M{p0[0]} {p0[1]} Q{c[0]} {c[1]} {p1[0]} {p1[1]}" fill="none" stroke="{col["stroke"]}" stroke-width="2.6" marker-end="url(#m{mk})"/>')

# purple
line([(240,106),(214,194)], P, mk='p')
line([(285,106),(310,194)], P, mk='p')
line([(320,106),(598,194)], P, True, 'p')
line([(450,106),(418,194)], P, mk='p')
line([(485,106),(515,194)], P, mk='p')
line([(670,106),(646,194)], P, True, 'p')
line([(725,106),(758,194)], P, mk='p')
line([(1020,196),(1052,196),(1052,486)], P, mk='p')
line([(950,276),(950,486)], P, mk='p')
line([(890,276),(890,382),(776,382)], P, mk='p')
# blue
line([(211,244),(238,354)], B, mk='b')
curve((245,244),(560,500),(796,502), B, 'b')  # AI 컴퓨팅 → 전력: 배터리와 간격을 두고, 전력 상자 왼쪽(핵심광물 화살표 약간 위)으로 들어가는 곡선
line([(440,244),(668,354)], B, mk='b')
line([(650,244),(694,354)], B, True, 'b')
line([(400,244),(418,486)], B, mk='b')
# green
line([(300,404),(372,486)], T, mk='t')
line([(682,404),(472,486)], T, mk='t')
# amber
line([(800,514),(486,514)], A, mk='a')

# nodes
node(192, 62, 140, P, '지능의 자동화')
node(401, 62, 130, P, '지정학·안보')
node(645, 62, 110, P, '인구 구조')
node(860, 174, 160, P, '기후의 물리적 변화')
node(860, 232, 140, P, '전기화·탈탄소')
node(165, 200, 92, B, 'AI 컴퓨팅')
node(267, 200, 92, B, '사이버보안')
node(369, 200, 92, B, '방산·우주')
node(471, 200, 92, B, '조선·해운')
node(573, 200, 130, B, '로봇·휴머노이드', dashed=True, sub='관찰 테마')
node(713, 200, 95, B, '바이오헬스')
node(165, 360, 170, T, '범용·전력 반도체')
node(650, 360, 122, T, '배터리')
node(340, 490, 140, A, '핵심광물')
node(800, 490, 260, A, '전력·에너지 인프라')
o.append('</svg>')
open(__import__('os').path.join(__import__('os').path.dirname(__file__), 'layer-map.svg'), 'w', encoding='utf-8').write('\n'.join(o))
print('written')
