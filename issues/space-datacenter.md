# 교차 이슈: 우주 데이터센터와 위성 인프라

> 기준일: 2026-10-23 · 단계: 레이더 · 점검 주기: 반기(주요 발사·시험 결과 시 수시) · 투자 권유가 아닌 산업 정리 문서입니다

| 걸치는 테마 | 연결 방식 |
|---|---|
| [AI 컴퓨팅](../themes/demand/ai-compute.md) | 땅 위 데이터센터의 전력·부지·용수 제약을 우회하려는 시도 |
| [방산·우주](../themes/demand/defense-space.md) | 발사체, 위성 제작, 위성 간 레이저 통신(스타링크와 같은 기술 기반) |
| [전력·에너지 인프라](../themes/foundation/power-energy.md) | 우주 태양광으로 전력 문제를 피한다는 발상 |

## 무엇인가

AI 데이터센터를 땅이 아니라 궤도 위 위성에 올리자는 구상입니다. 우주에서는 태양광을 거의 끊김 없이 받을 수 있고, 땅 위의 전력망 연결 대기, 부지 반발, 용수 문제를 피할 수 있다는 논리입니다. 위성끼리는 레이저로 연결하고, 지상과도 레이저나 전파로 데이터를 주고받습니다. 스타링크가 이미 위성 간 레이저 통신을 대규모로 운영하고 있어서, 위성통신망과 우주 연산이 같은 기술 기반 위에 놓여 있습니다.

## 현재 상태

| 시점 | 사건 | 출처 |
|---|---|---|
| 2025년 11월 | 스타트업 스타클라우드가 엔비디아 H100 칩을 실은 위성(스타클라우드-1)을 발사. 회사는 12월 우주에서 AI 모델을 실행·학습했다고 발표 | 스타클라우드, 엔비디아 |
| 2026년 3월 | 스타클라우드, 기업가치 11억 달러로 1억 7천만 달러 투자 유치 | 스타클라우드 |
| 2026년 5월 | 스타클라우드, 위성 간 연결에 스페이스X 스타링크의 소형 레이저 통신 장비를 쓰기로 발표 | 스타클라우드 |
| 2026년 8월 | 스타클라우드, 기업가치 23억 달러로 2억 5천만 달러 추가 유치(엔비디아 등 참여) | 스타클라우드 |
| 2026년 9월 28일 | 스페이스X 스타십이 처음 궤도에 올라 스타링크 V3 위성 26기 배치 | 스페이스X |
| 2026년 10월 1일 | 구글이 프로젝트 선캐처 시제품 위성 발사(TPU 탑재, 플래닛과 공동 개발, 스페이스X 공동 발사 임무). 궤도에서 방사선·진동·온도 조건을 시험하며, 2027년 위성 2기를 더 올려 서로 연결하는 시험을 할 계획 | 구글 |
| 2028년(목표) | 스페이스X가 증권신고서에서 이르면 2028년 궤도 AI 연산 위성 배치를 시작할 것으로 예상 | 스페이스X |

구글은 선캐처를 "연구 문샷"이라고 부릅니다. 구글 연구진은 발사 가격이 2030년대 중반 kg당 200달러 아래로 떨어지면, 우주 데이터센터를 쏘아 올리고 운영하는 비용이 같은 규모 지상 데이터센터의 전기요금과 비슷해질 수 있다고 분석했습니다. 거꾸로 말하면, 발사 가격이 그만큼 내려오기 전까지는 경제성이 없다는 뜻입니다.

## 병목과 쟁점

- **열 방출:** 우주에는 공기도 물도 없어서 칩의 열을 방열판으로만 내보내야 합니다. 방열판은 무겁고, 무게는 곧 발사비입니다.
- **방사선:** 우주 방사선이 칩 오작동과 수명 단축을 일으킬 수 있습니다.
- **발사비:** 경제성의 핵심 변수입니다. 대형 재사용 로켓(스타십)의 상용화가 전제 조건에 가깝습니다.
- **수리 불가:** 고장 난 칩을 사람이 교체할 수 없습니다.
- **통신 대역:** 지상 데이터센터 한 곳의 연산을 대신하려면 위성이 아주 많이 필요하고, 위성 간·지상 간 통신 속도가 제약이 됩니다.
- **환경:** 발사 배출과 수명이 다한 위성의 대기권 재진입 오염 문제가 제기됩니다.

## 지켜볼 신호

| 신호 | 의미 |
|---|---|
| 선캐처 시제품의 1년 운영 결과(열·방사선 데이터) | 기술적 가능성의 첫 검증 |
| 스타십 상용 발사 횟수와 발사 단가 | 경제성의 전제 조건(2026년 9월 첫 궤도 비행 성공) |
| 첫 유료 고객 계약 | 레이더 → 관찰 승격의 핵심 신호. 투자 유치는 활발하지만(스타클라우드 2026년 누적 4억 달러 이상) 유료 고객 계약은 아직 공개되지 않음 |
| 스페이스X 궤도 AI 연산 위성 실제 배치 | 대규모 사업화 여부 |

## 승격·종료 조건

- **관찰 승격:** 관찰 테마 진입 조건 3개 중 2개 충족. 예를 들어 첫 유료 고객 계약과 위성·부품 전용 공급사 등장이 함께 확인되는 경우
- **목록 제외:** 시제품 시험에서 열·방사선 문제가 해결되기 어렵다는 결과가 나오고 주요 업체가 계획을 철회하는 경우

## 출처

- 구글, 프로젝트 선캐처 소개 ("연구 문샷"): https://blog.google/innovation-and-ai/technology/research/google-project-suncatcher/
- 구글 리서치, 우주 기반 AI 인프라 설계 연구(발사 가격 분석): https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/
- 구글, 선캐처 시제품 위성 궤도 진입 (2026-10-01): https://blog.google/innovation-and-ai/models-and-research/google-research/project-suncatcher-prototype/
- 플래닛, 선캐처 위성 제작·운영 발표: https://www.planet.com/pulse/planet-to-build-and-operate-advanced-space-platform-for-project-suncatcher-moonshot/
- 스타클라우드, 스타클라우드-1 소개: https://www.starcloud.com/starcloud-1
- 엔비디아, 스타클라우드와 우주 데이터센터: https://blogs.nvidia.com/blog/starcloud/
- 스타클라우드, 시리즈 A 1억 7천만 달러 (2026-03-30): https://www.businesswire.com/news/home/20260330024111/en/Starcloud-Raises-$170M-Series-A-at-$1.1bn-Valuation-Led-by-Benchmark-and-EQT-Ventures
- 스타클라우드, 스타링크 소형 레이저 채택 (2026-05-26): https://www.businesswire.com/news/home/20260526670395/en/Starcloud-to-Integrate-SpaceXs-Starlink-Mini-Lasers-Into-Its-Orbital-Data-Center-Constellation
- 스타클라우드, 2억 5천만 달러 추가 유치 (2026-08-21): https://www.businesswire.com/news/home/20260821884035/en/Starcloud-Raises-$250-Million-at-$2.3-Billion-Valuation-to-Scale-AI-with-Orbital-Data-Centers
- 스페이스X, 2026년 3분기 실적(스타십 첫 궤도 비행): https://ir.spacex.com/files/content_files/SpaceX-Reports-Third-Quarter-2026-Results.pdf
- 스페이스X, 증권신고서(S-1, 궤도 AI 연산 위성 계획): https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/spaceexplorationtechnologi.htm
