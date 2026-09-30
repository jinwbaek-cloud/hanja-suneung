// 독서·비문학 시범 퀴즈 9문항 전용 데이터
// (정립 항목은 사전 원문 직접 대조 미완료에 따라 출제 보류되어 총 9문항으로 구성됨)
// 기존 기출 DB(js/data.js) 및 고전 시범 데이터와 분리하여 독립적으로 관리됩니다.
window.READING_PILOT_QUIZ_DATA = [
  {
    id: "reading-pilot-1",
    word: "규범",
    hanja: "規範",
    hun: "법 규(規), 법/본보기 범(範)",
    type: "blank",
    typeLabel: "빈칸형",
    sourceLabel: "학습용 창작 예문",
    question: "다음 글의 빈칸에 들어갈 가장 적절한 어휘를 고르시오.",
    passage: "사회 현상을 있는 그대로 관찰하여 설명하는 것만으로는 사람들이 어떻게 행동해야 하는지 알려 주기 어렵다. 실제로 일어난 사실을 다루는 영역과 달리, 사람들이 마땅히 따르고 지켜야 할 행동의 기준이나 규칙을 다루는 영역을 [　　]의 영역이라고 한다.",
    options: [
      { id: "rp1-opt-1", text: "규범", isCorrect: true },
      { id: "rp1-opt-2", text: "전제", isCorrect: false },
      { id: "rp1-opt-3", text: "관례", isCorrect: false },
      { id: "rp1-opt-4", text: "가설", isCorrect: false }
    ],
    definition: "인간이 행동하거나 판단할 때에 마땅히 따르고 지켜야 할 가치 판단의 기준.",
    explanation: "‘실제로 일어난 사실을 다루는 영역과 달리’, ‘사람들이 마땅히 따르고 지켜야 할 행동의 기준이나 규칙’이라는 설명이 단서입니다. 관례는 이전부터 해 오던 방식에 초점이 있고, 이 문맥은 마땅히 지켜야 할 기준을 강조하므로 규범이 가장 적절합니다.",
    hanjaExplanation: "規(법 규)와 範(법/본보기 범)이 결합하여, 행동이나 판단의 본보기가 되는 기준과 법칙을 가리킵니다."
  },
  {
    id: "reading-pilot-2",
    word: "괴리",
    hanja: "乖離",
    hun: "어그러질 괴(乖), 떠날 리(離)",
    type: "blank",
    typeLabel: "빈칸형",
    sourceLabel: "학습용 창작 예문",
    question: "다음 글의 빈칸에 들어갈 가장 적절한 어휘를 고르시오.",
    passage: "공식 발표에서는 생활 여건이 좋아졌다고 하지만, 사람들이 실제로 느끼는 살림살이는 여전히 팍팍했다. 이처럼 겉으로 드러난 수치와 실제 생활 감각이 서로 들어맞지 않고 크게 동떨어져 있는 [　　] 상태는 정책에 대한 불만을 낳기 쉽다.",
    options: [
      { id: "rp2-opt-1", text: "일치", isCorrect: false },
      { id: "rp2-opt-2", text: "괴리", isCorrect: true },
      { id: "rp2-opt-3", text: "왜곡", isCorrect: false },
      { id: "rp2-opt-4", text: "결손", isCorrect: false }
    ],
    definition: "서로 어그러져 동떨어짐.",
    explanation: "‘겉으로 드러난 수치와 실제 생활 감각이 서로 들어맞지 않고 크게 동떨어져 있는 상태’가 단서입니다. 괴리는 둘 사이가 서로 어그러져 동떨어진 상태를 뜻합니다.",
    hanjaExplanation: "乖(어그러질 괴)와 離(떠날 리)가 결합하여, 어긋나서(乖) 멀리 떨어져 있음(離)을 나타냅니다."
  },
  {
    id: "reading-pilot-3",
    word: "수렴",
    hanja: "收斂",
    hun: "거둘 수(收), 거둘 렴(斂)",
    type: "context_meaning",
    typeLabel: "문맥 속 뜻 고르기",
    sourceLabel: "학습용 창작 예문",
    question: "이 글에서 ‘수렴’의 뜻으로 가장 적절한 것은?",
    passage: "세 연구팀이 같은 현상을 서로 다른 방법으로 분석했다. 처음에는 예상 결과가 크게 달랐지만, 자료를 추가하고 계산을 보완하자 세 팀의 예상값 사이의 차이가 점차 줄어들었다. 연구자들은 예상값이 비슷한 수준으로 수렴하고 있다고 설명했다.",
    options: [
      { id: "rp3-opt-1", text: "여러 사람의 요구를 빠짐없이 수집함", isCorrect: false },
      { id: "rp3-opt-2", text: "서로 달랐던 값들이 비슷한 수준으로 모여듦", isCorrect: true },
      { id: "rp3-opt-3", text: "모아 둔 자료를 여러 집단에 나누어 전달함", isCorrect: false },
      { id: "rp3-opt-4", text: "이미 얻은 결과를 검토 대상에서 제외함", isCorrect: false }
    ],
    definition: "여러 갈래로 나뉘어 있던 의견이나 생각, 요소 등이 하나로 모아짐.",
    explanation: "처음에는 달랐던 예상값 사이의 차이가 점차 줄어들었다는 것이 단서입니다. 이 문맥에서 수렴은 서로 달랐던 값들이 비슷한 수준으로 모여드는 것을 뜻합니다.",
    hanjaExplanation: "收(거둘 수)와 斂(거둘 렴)이 결합한 말로, 흩어져 있던 값들이 한곳으로 거두어져 모여든다는 의미를 담고 있습니다."
  },
  {
    id: "reading-pilot-4",
    word: "매개",
    hanja: "媒介",
    hun: "중매 매(媒), 낄 개(介)",
    type: "context_meaning",
    typeLabel: "문맥 속 뜻 고르기",
    sourceLabel: "학습용 창작 예문",
    question: "다음 제시문의 밑줄 친 매개의 문맥적 의미로 가장 적절한 것은?",
    passage: "우리는 외부의 사물을 직접 만지지 않고도 눈이나 귀와 같은 감각 기관을 통해 사물의 색깔과 소리를 알게 된다. 이처럼 감각 기관의 작용을 매개로 하여 사람과 사물 사이의 관찰과 인식이 이루어진다.",
    options: [
      { id: "rp4-opt-1", text: "혼인할 남녀의 집안 사이를 주선하여 이어 주는 일", isCorrect: false },
      { id: "rp4-opt-2", text: "병원균이나 유해 물질을 다른 생물체로 옮겨 퍼뜨리는 일", isCorrect: false },
      { id: "rp4-opt-3", text: "둘 사이에서 양편의 관계나 작용을 이어 주는 일", isCorrect: true },
      { id: "rp4-opt-4", text: "어떤 일의 직접적인 원인이 되어 결과를 낳는 일", isCorrect: false }
    ],
    definition: "둘 사이에서 양편의 관계를 맺어 줌.",
    explanation: "감각 기관을 통해 ‘사람과 사물 사이의 관찰과 인식이 이루어진다’는 설명이 단서입니다. 매개는 둘 사이의 중간에서 양편의 관계나 작용을 이어 주는 일을 뜻합니다.",
    hanjaExplanation: "媒(중매 매)와 介(낄 개)가 결합하여, 사이에 끼어들어(介) 양쪽을 연결해 준다(媒)는 뜻입니다."
  },
  {
    id: "reading-pilot-5",
    word: "담보",
    hanja: "擔保",
    hun: "멜 담(擔), 지킬 보(保)",
    type: "context_meaning",
    typeLabel: "문맥 속 뜻 고르기",
    sourceLabel: "학습용 창작 예문",
    question: "이 글에서 ‘담보’의 역할이나 의미로 가장 적절한 것은?",
    passage: "은행은 기업에 사업 자금을 대출해 주면서, 기업이 빚을 제때 갚지 못할 위험에 대비해 공장 건물을 담보로 잡았다. 만약 기업이 약속대로 돈을 갚지 못하면, 은행은 해당 건물을 처분한 대금에서 다른 일반 채권자보다 먼저 빌려준 돈을 돌려받을 수 있는 법적 권리를 행사하게 된다.",
    options: [
      { id: "rp5-opt-1", text: "빌려준 돈을 돌려받지 못할 위험에 대비하는 수단", isCorrect: true },
      { id: "rp5-opt-2", text: "거래 상대의 신용만을 믿고 아무런 권리 설정 없이 자금을 대출해 주는 방식", isCorrect: false },
      { id: "rp5-opt-3", text: "대출 기간 동안 채무자의 건물을 은행이 직접 넘겨받아 보관하는 조치", isCorrect: false },
      { id: "rp5-opt-4", text: "사업이 실패하더라도 어떤 상황에서든 빌려준 돈 전액의 회수를 무조건 보장하는 장치", isCorrect: false }
    ],
    definition: "채권자가 채무 불이행에 대비하여 채권의 회수를 확보하기 위해 마련하는 수단.",
    explanation: "은행이 기업에 사업 자금을 대출해 주며 빚을 갚지 못할 위험에 대비해 공장 건물을 담보로 잡았다는 상황이 단서입니다. 이 사례처럼 부동산에 권리를 설정할 때 건물을 은행이 직접 넘겨받아 보관하는 것이 아니며, 담보물 처분 대금이 모자라면 전액 회수가 불가능할 수도 있으므로 무조건적인 전액 회수를 보장하는 것은 아닙니다.",
    hanjaExplanation: "擔(멜 담)과 保(지킬 보)가 결합하여, 책임을 지고(擔) 안전하게 지킨다(保)는 뜻을 나타냅니다."
  },
  {
    id: "reading-pilot-6",
    word: "투영",
    hanja: "投影",
    hun: "던질 투(投), 그림자 영(影)",
    type: "situation_term",
    typeLabel: "상황에 맞는 용어 고르기",
    sourceLabel: "학습용 창작 예문",
    question: "이 과정을 가리키는 어휘는?",
    passage: "화면에 입체적인 건물을 그릴 때, 공간에 있는 건물의 모습을 평평한 종이나 화면 위에 빛을 비추듯 옮겨 나타내야 한다. 이처럼 입체적인 대상의 형태를 평면 위에 상이나 그림자로 맺히게 나타내는 과정이 필요하다.",
    options: [
      { id: "rp6-opt-1", text: "굴절", isCorrect: false },
      { id: "rp6-opt-2", text: "산란", isCorrect: false },
      { id: "rp6-opt-3", text: "투영", isCorrect: true },
      { id: "rp6-opt-4", text: "투과", isCorrect: false }
    ],
    definition: "물체의 그림자를 어떤 평면에 비춤.",
    explanation: "‘입체적인 대상의 형태를 평면 위에 상이나 그림자로 맺히게 나타내는 과정’이 단서입니다. 투영은 공간의 물체나 형상을 평면에 비추어 상이나 그림자로 맺히게 하는 것을 뜻합니다.",
    hanjaExplanation: "投(던질 투)와 影(그림자 영)이 결합하여, 빛이나 상을 던져(投) 그림자나 형상(影)을 맺히게 한다는 뜻입니다."
  },
  {
    id: "reading-pilot-7",
    word: "태환",
    hanja: "兌換",
    hun: "바꿀 태(兌), 바꿀 환(換)",
    type: "situation_term",
    typeLabel: "상황에 맞는 용어 고르기",
    sourceLabel: "학습용 창작 예문",
    question: "상인이 지폐를 금으로 바꾼 행위를 가리키는 가장 적절한 용어는?",
    passage: "어떤 나라에서는 사람들이 은행에 지폐를 가져오면 미리 정한 비율에 따라 금으로 바꾸어 주기로 했다. 한 상인이 이 약속에 따라 자신이 가진 지폐를 은행에 내고 그에 해당하는 금을 받았다.",
    options: [
      { id: "rp7-opt-1", text: "송금", isCorrect: false },
      { id: "rp7-opt-2", text: "태환", isCorrect: true },
      { id: "rp7-opt-3", text: "결제", isCorrect: false },
      { id: "rp7-opt-4", text: "차입", isCorrect: false }
    ],
    definition: "지폐를 정화(正貨), 곧 금이나 은 따위의 본위 화폐와 바꿈.",
    explanation: "지폐를 은행에 내고 정해진 비율에 따라 금을 받았다는 것이 단서입니다. 태환은 지폐를 금이나 은 따위의 본위 화폐와 바꾸는 일을 뜻합니다.",
    hanjaExplanation: "兌(바꿀 태)와 換(바꿀 환)이 결합하여, 지폐와 본위 화폐를 서로 맞바꾼다는 뜻입니다."
  },
  {
    id: "reading-pilot-8",
    word: "이상치",
    hanja: "異常値",
    hun: "다를 이(異), 항상/보통 상(常), 값 치(値)",
    type: "situation_term",
    typeLabel: "상황에 맞는 용어 고르기",
    sourceLabel: "학습용 창작 예문",
    question: "이처럼 다른 관측값들과 크게 동떨어진 값을 가리키는 어휘는?",
    passage: "한 자료에서 관측값 대부분은 10에서 15 사이에 모여 있었지만, 일부 값은 100을 넘었다. 분석자는 다른 값들과 크게 동떨어진 이 값들에 표시를 한 뒤, 측정 오류인지 실제로 드문 현상이 나타난 것인지 확인하기로 했다.",
    options: [
      { id: "rp8-opt-1", text: "결측치", isCorrect: false },
      { id: "rp8-opt-2", text: "최빈값", isCorrect: false },
      { id: "rp8-opt-3", text: "평균값", isCorrect: false },
      { id: "rp8-opt-4", text: "이상치", isCorrect: true }
    ],
    definition: "관측된 데이터의 정상 범위를 벗어난 비정상적인 값.",
    explanation: "다른 관측값들이 모인 범위에서 크게 벗어나 있다는 것이 단서입니다. 이상치는 다른 관측값들과 크게 동떨어진 값입니다. 측정 오류일 수도 있지만 실제로 드문 현상을 관측한 값일 수도 있으므로, 무조건 삭제하지 않고 원인을 확인해야 합니다.",
    hanjaExplanation: "異(다를 이), 常(항상/보통 상), 値(값 치)가 결합하여, 일반적인 보통 상태와 크게 다른 값을 뜻합니다."
  },
  {
    id: "reading-pilot-9",
    word: "탄력성",
    hanja: "彈力性",
    hun: "튕길 탄(彈), 힘 력(力), 성품 성(性)",
    type: "blank",
    typeLabel: "빈칸형",
    sourceLabel: "학습용 창작 예문",
    question: "다음 글의 빈칸에 들어갈 가장 적절한 어휘를 고르시오.",
    passage: "다른 조건이 같을 때 두 상품 A와 B의 가격이 각각 10% 올랐다고 하자. 이때 A 상품의 구매량은 2% 줄어든 반면, B 상품의 구매량은 20% 줄어들었다. 이처럼 같은 가격 변화율에 대해 구매량의 변화율이 더 큰 쪽이 가격 변화에 더 민감하게 반응한다고 볼 수 있다. 경제학에서는 가격 변동이라는 자극에 대해 수요량이 얼마나 민감하게 반응하는가를 수요의 [　　]이라고 부른다.",
    options: [
      { id: "rp9-opt-1", text: "수익성", isCorrect: false },
      { id: "rp9-opt-2", text: "유동성", isCorrect: false },
      { id: "rp9-opt-3", text: "탄력성", isCorrect: true },
      { id: "rp9-opt-4", text: "안정성", isCorrect: false }
    ],
    definition: "용수철처럼 튀어 오르는 힘을 가진 성질. 경제학에서는 독립변수의 변화율에 대한 종속변수의 변화율의 비.",
    explanation: "가격 변화에 더 민감하게 반응하여 구매량 변화율이 더 큰 B 상품이 A 상품보다 수요의 가격 탄력성이 더 큽니다. 탄력성의 크기는 절댓값을 기준으로 비교합니다. 오답인 유동성은 자산을 필요할 때 큰 가치 손실 없이 현금으로 바꾸기 쉬운 정도를 뜻합니다.",
    hanjaExplanation: "彈(튕길 탄), 力(힘 력), 性(성품 성)의 결합으로 본래는 외부 충격에 튕겨 움직이는 성질을 뜻하나, 경제학에서는 가격 변화에 따른 수요량의 민감한 변동 비율이라는 전문적 의미로 사용됩니다."
  }
];
