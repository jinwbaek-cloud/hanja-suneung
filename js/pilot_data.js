// 고전문학 시범 퀴즈 10문항 전용 데이터
// 기존 기출 DB(js/data.js)와 분리하여 독립적으로 관리됩니다.
window.PILOT_QUIZ_DATA = [
  {
    id: "pilot-1",
    word: "박장대소",
    hanja: "拍掌大笑",
    hun: "칠 박(拍), 손바닥 장(掌), 큰 대(大), 웃을 소(笑)",
    type: "blank",
    typeLabel: "문맥 적용형",
    isCreative: true,
    sourceLabel: "학습용 창작 예문",
    question: "다음 문장의 빈칸에 들어갈 가장 알맞은 어휘는?",
    passage: "광대의 익살스러운 몸짓을 본 구경꾼들은 손뼉을 짝짝 치며 한바탕 [ 　　 ]했다.",
    blankText: "[ 　　 ]",
    options: [
      { id: "p1-opt-1", text: "박장대소", isCorrect: true },
      { id: "p1-opt-2", text: "대성통곡", isCorrect: false },
      { id: "p1-opt-3", text: "호언장담", isCorrect: false },
      { id: "p1-opt-4", text: "노발대발", isCorrect: false }
    ],
    definition: "손뼉을 치며 크게 웃음. ≒박소.",
    explanation: "문장 속 '손뼉을 짝짝 치며', '한바탕 [ 　　 ]했다'는 구절에서 손뼉을 치면서 유쾌하게 크게 웃음을 터뜨리는 행동임을 알 수 있습니다.",
    hanjaExplanation: "‘손바닥을 치며(拍掌) 크게 웃는다(大笑)’는 뜻입니다."
  },
  {
    id: "pilot-2",
    word: "홍진",
    hanja: "紅塵",
    hun: "붉을 홍(紅), 티끌 진(塵)",
    type: "blank",
    typeLabel: "문맥 적용형",
    isCreative: true,
    sourceLabel: "학습용 창작 예문",
    question: "다음 문장의 빈칸에 들어갈 가장 알맞은 어휘는?",
    passage: "권력과 재물을 다투는 [ 　　 ]의 번잡함을 뒤로하고, 그는 깊은 산골로 들어가 맑은 시냇물과 대숲을 벗 삼아 한가롭고 편안하게 살아가기로 결심했다.",
    blankText: "[ 　　 ]",
    options: [
      { id: "p2-opt-1", text: "홍진", isCorrect: true },
      { id: "p2-opt-2", text: "선경", isCorrect: false },
      { id: "p2-opt-3", text: "향리", isCorrect: false },
      { id: "p2-opt-4", text: "비경", isCorrect: false }
    ],
    definition: "번거롭고 속된 세상을 비유적으로 이르는 말.",
    explanation: "'권력과 재물을 다투는', '번잡함'이라는 속세의 속성과, 이를 벗어나 산골에서 '한가롭고 편안하게 살아가는' 삶의 대조를 통해 번잡한 세속을 가리키는 어휘임을 알 수 있습니다.",
    hanjaExplanation: "번화한 거리에서 수레나 말이 일으키는 ‘붉은 흙먼지(紅塵)’에서 유래하여 번거롭고 속된 세상을 비유합니다."
  },
  {
    id: "pilot-3",
    word: "야인",
    hanja: "野人",
    hun: "들 야(野), 사람 인(人)",
    type: "blank",
    typeLabel: "문맥 적용형",
    isCreative: true,
    sourceLabel: "학습용 창작 예문",
    question: "다음 문장의 빈칸에 들어갈 가장 알맞은 어휘는?",
    passage: "평생 몸담았던 관직에서 미련 없이 물러난 그는, 정치 활동에서도 손을 떼고 어떠한 당파나 기관에도 속하지 않은 [ 　　 ](으)로서 평범한 일상을 보냈다.",
    blankText: "[ 　　 ]",
    options: [
      { id: "p3-opt-1", text: "야인", isCorrect: true },
      { id: "p3-opt-2", text: "관료", isCorrect: false },
      { id: "p3-opt-3", text: "정객", isCorrect: false },
      { id: "p3-opt-4", text: "각료", isCorrect: false }
    ],
    definition: "아무 곳에도 소속하지 않은 채 지내는 사람. (재야인)",
    explanation: "'관직에서 미련 없이 물러난', '정치 활동에서도 손을 떼고 어떠한 당파나 기관에도 속하지 않은'이라는 수식에서 공직과 정계를 떠나 재야에 머무는 신분 상태를 나타냅니다.",
    hanjaExplanation: "‘관직을 떠나 들판(재야)에서 머무는 사람(野人)’이라는 뜻입니다. (고전시가에서는 화자가 자신을 낮추는 시골 사람/은사 자칭으로 쓰이나, 본 문항은 표준 정의인 재야인의 뜻을 평가합니다.)"
  },
  {
    id: "pilot-4",
    word: "수중고혼",
    hanja: "水中孤魂",
    hun: "물 수(水), 가운데 중(中), 외로울 고(孤), 넋 혼(魂)",
    type: "context_meaning",
    typeLabel: "문맥 속 뜻 고르기",
    isCreative: true,
    sourceLabel: "학습용 창작 예문",
    question: "다음 글의 문맥으로 보아, ‘수중고혼’의 뜻으로 가장 알맞은 것은?",
    passage: "밤새 몰아친 폭풍우에 고깃배가 뒤집히는 참변이 일어났다. 거센 파도에 휩쓸려 차가운 바닷속에 가라앉은 뱃사람들은 끝내 돌아오지 못하고 수중고혼이 되고 말았다.",
    targetHighlight: "수중고혼",
    options: [
      { id: "p4-opt-1", text: "물에 빠져 죽은 사람의 외로운 넋", isCorrect: true },
      { id: "p4-opt-2", text: "전쟁터에서 싸우다 숨진 사람의 영혼", isCorrect: false },
      { id: "p4-opt-3", text: "옥에 갇혀 고초를 겪다가 죽은 사람의 넋", isCorrect: false },
      { id: "p4-opt-4", text: "집을 떠나 길에서 떠돌다 병들어 죽은 사람의 혼", isCorrect: false }
    ],
    definition: "물에 빠져 죽은 사람의 외로운 넋.",
    explanation: "폭풍우로 배가 전복되어 차가운 바닷속에 가라앉아 목숨을 잃은 뱃사람들의 참변 상황에서 의미를 도출할 수 있습니다.",
    hanjaExplanation: "‘물속에서(水中) 외롭게 떠도는 넋(孤魂)’이라는 뜻입니다."
  },
  {
    id: "pilot-5",
    word: "소일",
    hanja: "消日",
    hun: "사라질/보낼 소(消), 날 일(日)",
    type: "blank",
    typeLabel: "문맥 적용형",
    isCreative: true,
    sourceLabel: "학습용 창작 예문",
    question: "다음 문장의 빈칸에 들어갈 가장 알맞은 어휘는?",
    passage: "정년퇴직을 한 그는 무료한 시간을 달래기 위해, 작은 텃밭에 채소를 가꾸며 [ 　　 ]했다.",
    blankText: "[ 　　 ]",
    options: [
      { id: "p5-opt-1", text: "소일", isCorrect: true },
      { id: "p5-opt-2", text: "방황", isCorrect: false },
      { id: "p5-opt-3", text: "고투", isCorrect: false },
      { id: "p5-opt-4", text: "방관", isCorrect: false }
    ],
    definition: "어떠한 것에 재미를 붙여 심심하지 아니하게 세월을 보냄.",
    explanation: "'무료한 시간을 달래기 위해', '텃밭에 채소를 가꾸며 [ 　　 ]했다'에서 소소한 일거리에 재미를 붙여 심심하지 않게 시간을 보낸다는 의미가 호응합니다.",
    hanjaExplanation: "‘날(세월)을 보낸다(消日)’는 뜻으로, 어떠한 일에 재미를 붙여 심심하지 않게 시간을 보냄을 이릅니다."
  },
  {
    id: "pilot-6",
    word: "치군택민",
    hanja: "致君澤民",
    hun: "이를/바칠 치(致), 임금 군(君), 은택 택(澤), 백성 민(民)",
    type: "definition",
    typeLabel: "뜻 확인형",
    isCreative: false,
    sourceLabel: "표준국어대사전 규범 정의",
    question: "다음 중 한자성어 ‘치군택민(致君澤民)’의 의미로 가장 알맞은 것은?",
    passage: "",
    options: [
      { id: "p6-opt-1", text: "임금에게 충성하고 백성에게 은혜를 베풂", isCorrect: true },
      { id: "p6-opt-2", text: "나라를 부강하게 하고 군대를 강력하게 기름", isCorrect: false },
      { id: "p6-opt-3", text: "백성의 재물을 가혹하게 빼앗아 관청을 채움", isCorrect: false },
      { id: "p6-opt-4", text: "벼슬을 사양하고 고향으로 돌아가 숨어 삶", isCorrect: false }
    ],
    definition: "임금에게는 몸을 바쳐 충성하고 백성에게는 혜택을 베풂.",
    explanation: "‘치군택민(致君澤民)’은 임금에게는 몸을 바쳐 충성하고 백성에게는 혜택을 베풂을 뜻하는 전통 선비의 이상적 정치 포부입니다.",
    hanjaExplanation: "致(이를 치), 君(임금 군), 澤(은택 택), 民(백성 민) 자로 이루어져 있습니다."
  },
  {
    id: "pilot-7",
    word: "전려",
    hanja: "田廬",
    hun: "밭 전(田), 오두막/집 려(廬)",
    type: "definition",
    typeLabel: "뜻 확인형",
    isCreative: false,
    sourceLabel: "표준국어대사전 규범 정의",
    question: "다음 중 어휘 ‘전려(田廬)’의 사전적 의미로 가장 알맞은 것은?",
    passage: "",
    options: [
      { id: "p7-opt-1", text: "농사를 본업으로 하는 사람의 집", isCorrect: true },
      { id: "p7-opt-2", text: "높은 벼슬아치가 머물던 크고 화려한 저택", isCorrect: false },
      { id: "p7-opt-3", text: "선현을 제사하고 유학을 가르치던 사설 교육 기관", isCorrect: false },
      { id: "p7-opt-4", text: "상인들이 물건을 벌여 놓고 팔던 상점", isCorrect: false }
    ],
    definition: "농사를 본업으로 하는 사람의 집. 또는 그런 가정. =농가(農家).",
    explanation: "‘전려(田廬)’는 밭가에 지은 오두막집이라는 뜻에서, 농사를 본업으로 하는 사람의 집(농가)을 가리킵니다.",
    hanjaExplanation: "田(밭 전), 廬(오두막/집 려) 자로 구성됩니다."
  },
  {
    id: "pilot-8",
    word: "강호",
    hanja: "江湖",
    hun: "강 강(江), 호수 호(湖)",
    type: "definition",
    typeLabel: "뜻 확인형",
    isCreative: false,
    sourceLabel: "표준국어대사전 규범 정의",
    question: "‘강호(江湖)’가 고전시가의 은거 공간을 뜻할 때, 그 의미로 가장 알맞은 것은?",
    passage: "",
    options: [
      { id: "p8-opt-1", text: "세속의 정치를 떠나 자연에 묻혀 사는 곳", isCorrect: true },
      { id: "p8-opt-2", text: "임금이 머물며 정사를 돌보는 대궐", isCorrect: false },
      { id: "p8-opt-3", text: "군사들이 국경을 지키기 위해 머무는 요새", isCorrect: false },
      { id: "p8-opt-4", text: "상인들이 모여 물건을 사고파는 번화한 시장", isCorrect: false }
    ],
    definition: "예전에, 은자나 시인, 묵객 등이 현실을 도피하여 생활하던 시골이나 자연. ≒호해.",
    explanation: "본래 강과 호수를 뜻하나, 고전시가에서는 벼슬자리인 대궐(조정)을 떠나 자연을 완상하고 유유자적 살아가는 시골이나 자연 공간을 대유적으로 비유합니다.",
    hanjaExplanation: "江(강 강), 湖(호수 호) 자로 구성된 대유적 표현입니다."
  },
  {
    id: "pilot-9",
    word: "흠향",
    hanja: "歆饗",
    hun: "기뻐 받을 흠(歆), 대접할/제사할 향(饗)",
    type: "definition",
    typeLabel: "뜻 확인형",
    isCreative: false,
    sourceLabel: "표준국어대사전 규범 정의",
    question: "다음 중 어휘 ‘흠향(歆饗)’의 사전적 의미로 가장 알맞은 것은?",
    passage: "",
    options: [
      { id: "p9-opt-1", text: "신령이나 조상이 제물을 받아서 먹음", isCorrect: true },
      { id: "p9-opt-2", text: "임금이 공을 세운 신하에게 벼슬을 내림", isCorrect: false },
      { id: "p9-opt-3", text: "먼 길을 떠나는 사람에게 여비를 보태 줌", isCorrect: false },
      { id: "p9-opt-4", text: "승려가 대중에게 불교의 교리를 설명함", isCorrect: false }
    ],
    definition: "신명(神明)이 제물을 받아서 먹음.",
    explanation: "‘흠향(歆饗)’은 신명(신령이나 조상의 혼령)이 정성껏 차려 올린 제물을 기쁘게 받아서 먹음을 뜻합니다.",
    hanjaExplanation: "歆(기뻐 받을 흠), 饗(대접할/제사할 향) 자로 이루어져 있습니다."
  },
  {
    id: "pilot-10",
    word: "주달",
    hanja: "奏達",
    hun: "아뢸 주(奏), 통달할/이를 달(達)",
    type: "definition",
    typeLabel: "뜻 확인형",
    isCreative: false,
    sourceLabel: "표준국어대사전 규범 정의",
    question: "다음 중 역사 문헌이나 고전소설에 쓰이는 어휘 ‘주달(奏達)’의 사전적 의미로 가장 알맞은 것은?",
    passage: "",
    options: [
      { id: "p10-opt-1", text: "신하가 임금에게 사안을 말이나 글로 아룀", isCorrect: true },
      { id: "p10-opt-2", text: "임금이 백성들에게 나라의 법령을 널리 알림", isCorrect: false },
      { id: "p10-opt-3", text: "장수가 군사들에게 적진으로 진격하라고 명령함", isCorrect: false },
      { id: "p10-opt-4", text: "학자들이 모여 경전의 가르침을 묻고 토론함", isCorrect: false }
    ],
    definition: "임금에게 아뢰던 일. ≒주문, 주상.",
    explanation: "‘주달(奏達)’은 신하가 국가의 정사나 상소 내용을 임금에게 공식적으로 아뢰던 일(하의상달)을 뜻합니다.",
    hanjaExplanation: "奏(아뢸 주), 達(통달할/이를 달) 자로 이루어져 있습니다."
  }
];
