// 1차 확대 어휘 퀴즈 19문항 전용 데이터 (Batch 01)
// ('환원' 문항은 사전 직접 열람 근거 미확보로 보류 제외됨)
// 기존 기출 DB(js/data.js) 및 기존 시범 데이터들과 분리하여 독립적으로 관리됩니다.

window.EXPANSION_BATCH_01_QUIZ_DATA = [
  {
    id: "batch01-1",
    word: "임천",
    hanja: "林泉",
    hun: "수풀 림(林), 샘 천(泉)",
    type: "meaning",
    typeLabel: "뜻 확인형",
    isCreative: false,
    sourceLabel: "표준국어대사전 규범 정의",
    question: "고전문학에서 은거의 공간을 뜻하는 ‘임천(林泉)’의 의미로 가장 적절한 것은?",
    passage: null,
    options: [
      { id: "b1-opt-1", text: "먼 길을 떠나는 사람을 위해 주막에서 베푸는 송별 잔치", isCorrect: false },
      { id: "b1-opt-2", text: "숲과 샘이라는 뜻으로, 속세를 떠나 은거하는 자연이나 시골", isCorrect: true },
      { id: "b1-opt-3", text: "나라의 큰 제사를 지내기 위해 마련해 둔 신성한 사당", isCorrect: false },
      { id: "b1-opt-4", text: "높은 벼슬을 얻어 백성을 다스리는 관아나 조정", isCorrect: false }
    ],
    definition: "숲과 샘. 또는 은거하는 시골이나 자연을 이르는 말.",
    explanation: "‘임천’은 수풀(林)과 샘(泉)이라는 뜻으로, 사대부들이 벼슬길에서 물러나 조용히 묻혀 지내던 시골이나 자연 공간을 가리킵니다."
  },
  {
    id: "batch01-2",
    word: "진세",
    hanja: "塵世",
    hun: "티끌 진(塵), 인간/세상 세(世)",
    type: "context_meaning",
    typeLabel: "문맥 속 뜻 고르기",
    isCreative: true,
    sourceLabel: "학습용 창작 예문",
    question: "다음 글에서 밑줄 친 ‘진세’의 문맥적 의미로 가장 적절한 것은?",
    passage: "강가에 누워서 맑은 물을 바라보는 뜻은, 흐르는 세월이 빠르니 백 년 인생인들 길겠는가 하는 생각 때문이다. 지난 십 년 동안 진세에 얽매여 품었던 세속의 욕심이 차가운 얼음 녹듯 사라지는구나.",
    targetHighlight: "진세",
    options: [
      { id: "b2-opt-1", text: "번잡한 욕망과 명리를 다투는 속된 인간 세상", isCorrect: true },
      { id: "b2-opt-2", text: "부모나 조상의 영혼을 모신 경건한 사당", isCorrect: false },
      { id: "b2-opt-3", text: "신선들이 모여 산다는 신비롭고 고요한 선계", isCorrect: false },
      { id: "b2-opt-4", text: "억울하게 목숨을 잃은 영혼들이 머무는 저승", isCorrect: false }
    ],
    definition: "정신에 고통을 주는 복잡하고 어수선한 세상. =티끌세상.",
    explanation: "‘진세’는 티끌(塵) 세상(世)이라는 뜻으로, 번거롭고 속된 인간 세상을 비유합니다."
  },
  {
    id: "batch01-3",
    word: "가인",
    hanja: "佳人",
    hun: "아름다울 가(佳), 사람 인(人)",
    type: "context_meaning",
    typeLabel: "문맥 속 뜻 고르기",
    isCreative: true,
    sourceLabel: "학습용 창작 예문",
    question: "다음 글에서 밑줄 친 ‘가인’의 문맥적 의미로 가장 적절한 것은?",
    passage: "따스한 봄바람이 부는 강 언덕에서 한 젊은 선비가 버드나무 그늘 아래 앉아 책을 읽고 있었다. 때마침 연못 건너편 꽃밭 사이로 곱게 차려입은 한 가인이 가벼운 걸음으로 지나가자, 선비는 그 고운 자태에서 한동안 눈을 떼지 못했다.",
    targetHighlight: "가인",
    options: [
      { id: "b3-opt-1", text: "벼슬을 버리고 시골에 은거하는 선비", isCorrect: false },
      { id: "b3-opt-2", text: "전쟁터에서 용맹을 떨치는 장수", isCorrect: false },
      { id: "b3-opt-3", text: "용모나 자태가 매우 아름다운 여인", isCorrect: true },
      { id: "b3-opt-4", text: "먼 길을 오가며 물건을 파는 장사꾼", isCorrect: false }
    ],
    definition: "아름다운 사람. 주로 얼굴이나 몸매 따위가 아름다운 여자를 이른다. =미인.",
    explanation: "‘가인’은 아름다운(佳) 사람(人)이라는 뜻으로, 고전 문학에서 주로 용모와 자태가 아름다운 여인을 가리킵니다."
  },
  {
    id: "batch01-4",
    word: "전별",
    hanja: "餞別",
    hun: "전별할 전(餞), 이별할 별(別)",
    type: "situation",
    typeLabel: "상황에 맞는 용어",
    isCreative: true,
    sourceLabel: "학습용 창작 예문",
    question: "이 글에서 관리가 벗을 떠나보내며 행한 행동을 가리키는 가장 적절한 어휘는?",
    passage: "한 관리가 멀리 변방으로 떠나게 된 오랜 벗을 위해 저녁 무렵 정자에 술과 음식을 풍성하게 차렸다. 함께 모인 사람들은 술잔을 나누며 먼 길의 무사를 빌었고, 밤이 깊도록 시를 읊으며 석별의 정을 나누었다.",
    options: [
      { id: "b4-opt-1", text: "흠향", isCorrect: false },
      { id: "b4-opt-2", text: "탄핵", isCorrect: false },
      { id: "b4-opt-3", text: "강론", isCorrect: false },
      { id: "b4-opt-4", text: "전별", isCorrect: true }
    ],
    definition: "잔치를 베풀어 작별한다는 뜻으로, 보내는 쪽에서 예를 차려 작별함을 이르는 말.",
    explanation: "‘전별’은 잔치를 베풀어 떠나는 사람을 예의를 갖추어 배웅하고 작별하는 일을 뜻합니다."
  },
  {
    id: "batch01-5",
    word: "발복",
    hanja: "發福",
    hun: "일어날 발(發), 복 복(福)",
    type: "meaning",
    typeLabel: "뜻 확인형",
    isCreative: false,
    sourceLabel: "표준국어대사전 규범 정의",
    question: "고전 작품에 자주 나타나는 ‘발복(發福)’의 의미로 가장 적절한 것은?",
    passage: null,
    options: [
      { id: "b5-opt-1", text: "정성을 다해 올린 제물을 제례 절차에 따라 물림", isCorrect: false },
      { id: "b5-opt-2", text: "운수가 비로소 트여 좋은 복이 찾아옴", isCorrect: true },
      { id: "b5-opt-3", text: "억울한 죄를 벗지 못하고 귀양길에 오름", isCorrect: false },
      { id: "b5-opt-4", text: "나라를 다스리는 큰 뜻을 품고 벼슬길에 나아감", isCorrect: false }
    ],
    definition: "『민속』 운이 틔어서 복이 닥침. 또는 그 복.",
    explanation: "‘발복’은 오랫동안 풀리지 않던 운이 트여 복이 찾아오는 것을 뜻합니다."
  },
  {
    id: "batch01-6",
    word: "백년기약",
    hanja: "百年期約",
    hun: "일백 백(百), 해 년(年), 기약할 기(期), 맺을 약(約)",
    type: "meaning",
    typeLabel: "뜻 확인형",
    isCreative: false,
    sourceLabel: "수능 기출 작품 (규원가)",
    question: "고전시가에서 ‘백년기약(百年期約)’의 뜻으로 가장 적절한 것은?",
    passage: null,
    options: [
      { id: "b6-opt-1", text: "한평생 부부로서 함께 살아갈 것을 굳게 맺는 약속", isCorrect: true },
      { id: "b6-opt-2", text: "백 년 동안 전쟁 없이 평화를 지키기로 한 국가 간 맹세", isCorrect: false },
      { id: "b6-opt-3", text: "학문을 백 년 동안 닦아 큰 도를 이루겠다는 결심", isCorrect: false },
      { id: "b6-opt-4", text: "백 살이 될 때까지 벼슬에서 물러나지 않겠다는 다짐", isCorrect: false }
    ],
    definition: "한평생을 부부로 함께 살아가자는 굳은 혼인 약속.",
    explanation: "‘백년기약’은 백 년, 곧 사람의 평생 동안 부부의 인연을 맺어 변치 않고 함께 지내자는 굳은 약속을 뜻합니다. (2022 9모 「규원가」 출전)"
  },
  {
    id: "batch01-7",
    word: "군자호구",
    hanja: "君子好逑",
    hun: "임금/군자 군(君), 아들 자(子), 좋을 호(好), 짝 구(逑)",
    type: "meaning",
    typeLabel: "뜻 확인형",
    isCreative: false,
    sourceLabel: "시경 주남 및 수능 기출 (규원가)",
    question: "고전문학에서 ‘군자호구(君子好逑)’가 뜻하는 바로 가장 적절한 것은?",
    passage: null,
    options: [
      { id: "b7-opt-1", text: "위급한 상황에서 목숨을 바쳐 임금을 구하는 충신", isCorrect: false },
      { id: "b7-opt-2", text: "무리를 지어 산골짜기를 떠돌며 노략질하는 도적", isCorrect: false },
      { id: "b7-opt-3", text: "덕망과 인품을 갖춘 군자의 어진 배필", isCorrect: true },
      { id: "b7-opt-4", text: "임금의 부름을 받고도 시골에 숨어 사는 선비", isCorrect: false }
    ],
    definition: "학식과 덕망을 갖춘 군자의 좋은 짝(배필).",
    explanation: "‘군자호구’는 학덕을 갖춘 군자의 좋은 짝(어진 배필)을 의미합니다. 『시경』 관저편 원문과 2022 9모 「규원가」에 출제된 표현입니다."
  },
  {
    id: "batch01-8",
    word: "공후배필",
    hanja: "公侯配匹",
    hun: "공평할/공작 공(公), 제후/후작 후(侯), 짝 배(配), 짝 필(匹)",
    type: "meaning",
    typeLabel: "뜻 확인형",
    isCreative: false,
    sourceLabel: "수능 기출 작품 (규원가)",
    question: "고전시가에서 ‘공후배필(公侯配匹)’의 의미로 가장 적절한 것은?",
    passage: null,
    options: [
      { id: "b8-opt-1", text: "과거 시험에 장원 급제하여 관직을 제수받은 인재", isCorrect: false },
      { id: "b8-opt-2", text: "농사를 지으며 소박하게 살아가는 시골 백성", isCorrect: false },
      { id: "b8-opt-3", text: "나라의 녹봉을 받지 않고 의병을 일으킨 장수", isCorrect: false },
      { id: "b8-opt-4", text: "높은 지위에 있는 벼슬아치나 제후의 배필", isCorrect: true }
    ],
    definition: "높은 지위에 있는 벼슬아치나 제후의 배필(짝).",
    explanation: "‘공후배필’은 지체 높은 벼슬아치나 제후(公侯)의 짝(配匹)을 가리킵니다. (2022 9모 「규원가」 출전)"
  },
  {
    id: "batch01-9",
    word: "현알",
    hanja: "見謁",
    hun: "뵐 현(見), 뵐 알(謁)",
    type: "context_meaning",
    typeLabel: "문맥 속 뜻 고르기",
    isCreative: true,
    sourceLabel: "학습용 창작 예문",
    question: "다음 글에서 밑줄 친 ‘현알’의 문맥적 의미로 가장 적절한 것은?",
    passage: "오랜 먼 여행길의 험난한 고비를 무사히 넘기고 고향 집으로 돌아온 주인공은, 무사히 돌아왔음을 먼저 조상께 아뢰기 위해 사당으로 나아가 정성껏 현알하였다.",
    targetHighlight: "현알",
    options: [
      { id: "b9-opt-1", text: "사당이나 어른을 찾아가 경건하게 뵘", isCorrect: true },
      { id: "b9-opt-2", text: "죄인의 잘못을 문책하여 옥에 가둠", isCorrect: false },
      { id: "b9-opt-3", text: "잔치를 베풀어 떠나는 길손을 송별함", isCorrect: false },
      { id: "b9-opt-4", text: "먼 곳의 소식을 상소로 적어 임금께 보고함", isCorrect: false }
    ],
    definition: "지체가 높고 귀한 사람을 찾아가 뵘. =알현.",
    explanation: "‘현알’은 뵐(見) 뵐(謁)의 결합으로, 지체가 높고 귀한 사람이나 조상의 사당을 찾아가 경건히 예를 올리는 행위를 가리킵니다."
  },
  {
    id: "batch01-10",
    word: "대경실색",
    hanja: "大驚失色",
    hun: "큰 대(大), 놀랄 경(驚), 잃을 실(失), 빛 색(色)",
    type: "situation",
    typeLabel: "상황에 맞는 용어",
    isCreative: true,
    sourceLabel: "학습용 창작 예문",
    question: "이 글에서 뜻밖의 큰 사건을 겪은 사람들의 모습을 나타내는 가장 적절한 사자성어는?",
    passage: "평화롭던 마을에 한밤중 갑자기 큰 바위가 산 위에서 굴러떨어졌다. 방 안에 모여 있던 사람들은 엄청난 소리에 너무 놀라 입을 다물지 못했고, 얼굴빛이 하얗게 질린 채 서로의 얼굴만 쳐다볼 뿐이었다.",
    options: [
      { id: "b10-opt-1", text: "박장대소", isCorrect: false },
      { id: "b10-opt-2", text: "대경실색", isCorrect: true },
      { id: "b10-opt-3", text: "치군택민", isCorrect: false },
      { id: "b10-opt-4", text: "백년기약", isCorrect: false }
    ],
    definition: "몹시 놀라 얼굴빛이 하얗게 질림.",
    explanation: "‘대경실색’은 크게 놀라(大驚) 얼굴빛을 잃어버릴(失色) 정도로 질린 상태를 뜻합니다."
  },
  {
    id: "batch01-11",
    word: "전제",
    hanja: "前提",
    hun: "앞 전(前), 끌/제시할 제(提)",
    type: "meaning",
    typeLabel: "뜻 확인형",
    isCreative: false,
    sourceLabel: "표준국어대사전 규범 정의",
    question: "논리학이나 학술적 논의에서 ‘전제(前提)’의 뜻으로 가장 적절한 것은?",
    passage: null,
    options: [
      { id: "b11-opt-1", text: "상대방의 주장에서 드러난 논리적 모순을 지적하여 반박함", isCorrect: false },
      { id: "b11-opt-2", text: "여러 주장을 절충하여 하나의 결론으로 종합하는 과정", isCorrect: false },
      { id: "b11-opt-3", text: "어떤 결론이나 판단을 이끌어 내기 위해 먼저 바탕으로 삼는 명제", isCorrect: true },
      { id: "b11-opt-4", text: "이미 내려진 결론을 다시 의심하여 검증하는 절차", isCorrect: false }
    ],
    definition: "어떠한 사물이나 현상을 이루기 위하여 먼저 내세우는 것. 『철학』 결론의 기초가 되는 판단.",
    explanation: "‘전제’는 논증이나 추론에서 어떤 결론을 정당화하기 위해 앞서 참이라고 인정하거나 바탕으로 내세우는 명제입니다."
  },
  {
    id: "batch01-12",
    word: "유추",
    hanja: "類推",
    hun: "무리/유사할 류(類), 미룰 추(推)",
    type: "situation",
    typeLabel: "상황에 맞는 용어",
    isCreative: true,
    sourceLabel: "학습용 창작 예문",
    question: "이 글에서 학생이 취한 생각의 방식을 가리키는 가장 적절한 어휘는?",
    passage: "철수는 자신이 기르던 화초의 잎이 시들었을 때 물을 주자 잎이 다시 싱싱해졌던 경험을 떠올렸다. 그는 친구가 기르는 다른 종류의 화초도 잎이 시들어 있는 것을 보고, 두 식물이 모두 흙이 말라 시들었다는 공통점에 주목하여 물을 주면 다시 살아날 가능성이 높다고 짐작했다.",
    options: [
      { id: "b12-opt-1", text: "유추", isCorrect: true },
      { id: "b12-opt-2", text: "귀속", isCorrect: false },
      { id: "b12-opt-3", text: "왜곡", isCorrect: false },
      { id: "b12-opt-4", text: "망각", isCorrect: false }
    ],
    definition: "같은 종류의 것 또는 비슷한 것에 기초하여 다른 사물을 미루어 추측하는 일.",
    explanation: "‘유추’는 비슷한 속성을 가진 두 대상을 비교하여 한쪽의 성질을 바탕으로 다른 쪽도 그러할 것이라 미루어 추론하는 방식입니다."
  },
  {
    id: "batch01-13",
    word: "발산",
    hanja: "發散",
    hun: "일어날 발(發), 흩어질 산(散)",
    type: "meaning",
    typeLabel: "뜻 확인형",
    isCreative: false,
    sourceLabel: "표준국어대사전 규범 정의",
    question: "‘발산(發散)’의 사전적 의미로 가장 적절한 것은?",
    passage: null,
    options: [
      { id: "b13-opt-1", text: "여러 갈래로 나뉘어 있던 생각들이 하나의 결론으로 모여듦", isCorrect: false },
      { id: "b13-opt-2", text: "이미 일어난 사건의 결과를 처음 원인 상태로 되돌림", isCorrect: false },
      { id: "b13-opt-3", text: "서로 다른 두 대상이 충돌하여 상호 작용을 멈춤", isCorrect: false },
      { id: "b13-opt-4", text: "기운이나 빛, 향기 따위가 밖으로 퍼져 나감", isCorrect: true }
    ],
    definition: "기운이나 빛 따위가 밖으로 뻗어 나가 퍼짐.",
    explanation: "‘발산’은 안에 뭉쳐 있던 기운이나 빛, 향기 따위가 바깥으로 뻗어 나가 널리 퍼지는 것을 뜻합니다."
  },
  {
    id: "batch01-14",
    word: "인과",
    hanja: "因果",
    hun: "원인 인(因), 열매/결과 과(果)",
    type: "meaning",
    typeLabel: "뜻 확인형",
    isCreative: false,
    sourceLabel: "표준국어대사전 규범 정의",
    question: "학술 지문에서 ‘인과(因果) 관계’의 뜻으로 가장 적절한 것은?",
    passage: null,
    options: [
      { id: "b14-opt-1", text: "시간 순서와 상관없이 우연히 함께 발생한 두 사건의 관계", isCorrect: false },
      { id: "b14-opt-2", text: "어떤 원인과 그로 인해 생겨난 결과의 관계", isCorrect: true },
      { id: "b14-opt-3", text: "겉으로 드러난 모양새와 그 속에 감추어진 본질의 관계", isCorrect: false },
      { id: "b14-opt-4", text: "전체를 구성하는 부분과 그 부분들의 총합 사이의 관계", isCorrect: false }
    ],
    definition: "원인과 결과를 아울러 이르는 말.",
    explanation: "‘인과’는 어떤 원인(因)과 그 원인으로 인해 생겨난 결과(果)의 관계를 뜻합니다."
  },
  {
    id: "batch01-15",
    word: "효용",
    hanja: "效用",
    hun: "본받을/효험 효(效), 쓸 용(用)",
    type: "context_meaning",
    typeLabel: "문맥 속 뜻 고르기",
    isCreative: true,
    sourceLabel: "학습용 창작 예문",
    question: "이 글에서 밑줄 친 ‘효용’의 문맥적 의미로 가장 적절한 것은?",
    passage: "날씨가 무더운 날 운동을 마친 영수는 시원한 음료수를 한 캔 사 마셨다. 목이 몹시 말랐던 터라 첫 모금을 마셨을 때 얻은 효용은 매우 컸다. 갈증이 풀리자 같은 음료수를 한 캔 더 마셨을 때에는 처음에 비해 느끼는 만족감이 크지 않았다.",
    targetHighlight: "효용",
    options: [
      { id: "b15-opt-1", text: "상품을 소비하여 얻는 주관적인 만족감", isCorrect: true },
      { id: "b15-opt-2", text: "상품을 만들기 위해 생산자가 지출한 총비용", isCorrect: false },
      { id: "b15-opt-3", text: "거래되는 물건의 객관적인 무게나 부피", isCorrect: false },
      { id: "b15-opt-4", text: "돈을 빌려 쓴 대가로 지불하는 금융 이자", isCorrect: false }
    ],
    definition: "보람 있게 쓰거나 쓰임. 또는 그런 보람이나 쓸모. 『경제』 인간의 욕망을 만족시킬 수 있는 재화의 능력.",
    explanation: "‘효용’은 경제 문맥에서 소비자가 상품이나 서비스를 소비함으로써 얻는 주관적인 만족의 크기를 뜻합니다."
  },
  {
    id: "batch01-16",
    word: "도출",
    hanja: "導出",
    hun: "이끌 도(導), 날 출(出)",
    type: "blank",
    typeLabel: "빈칸형",
    isCreative: true,
    sourceLabel: "학습용 창작 예문",
    question: "다음 글의 빈칸에 들어갈 가장 적절한 어휘를 고르시오.",
    passage: "도서관 운영진은 지난 한 달간 이용자들의 방문 시간대를 조사했다. 그 결과 늦은 저녁 시간에 방문객이 가장 많다는 사실을 확인하고, 이를 바탕으로 평일 저녁 운영 시간을 한 시간 연장하기로 결론을 [　　]했다.",
    blankText: "[　　]",
    options: [
      { id: "b16-opt-1", text: "왜곡", isCorrect: false },
      { id: "b16-opt-2", text: "유보", isCorrect: false },
      { id: "b16-opt-3", text: "도출", isCorrect: true },
      { id: "b16-opt-4", text: "기피", isCorrect: false }
    ],
    definition: "판단이나 결론 따위를 이끌어 냄.",
    explanation: "‘도출’은 조사 자료나 사실을 바탕으로 판단이나 결론을 밖으로 이끌어 내는 것을 뜻합니다."
  },
  {
    id: "batch01-17",
    word: "환기",
    hanja: "喚起",
    hun: "부를 환(喚), 일어날 기(起)",
    type: "context_meaning",
    typeLabel: "문맥 속 뜻 고르기",
    isCreative: true,
    sourceLabel: "학습용 창작 예문",
    question: "이 글에서 밑줄 친 ‘환기’의 문맥적 의미로 가장 적절한 것은?",
    passage: "환경 운동가는 강의를 시작하면서 바다거북의 몸에 플라스틱 쓰레기가 박혀 있는 사진을 화면에 띄웠다. 그는 청중에게 이 사진을 보여 줌으로써 해양 오염의 심각성을 알리고, 환경 보호에 대한 대중의 경각심과 주의를 강하게 환기하고자 했다.",
    targetHighlight: "환기",
    options: [
      { id: "b17-opt-1", text: "탁한 공기를 빼내고 맑은 공기를 들여옴", isCorrect: false },
      { id: "b17-opt-2", text: "빌린 돈이나 물건을 원래 주인에게 되돌려줌", isCorrect: false },
      { id: "b17-opt-3", text: "상대방의 반대 의견을 물리치고 결정을 강행함", isCorrect: false },
      { id: "b17-opt-4", text: "주의나 생각, 경각심 등을 불러일으킴", isCorrect: true }
    ],
    definition: "주의나 여론, 생각 따위를 불러일으킴.",
    explanation: "‘환기’는 주의나 생각, 여론 등을 일깨워 불러일으킨다는 뜻입니다."
  },
  {
    id: "batch01-18",
    word: "개연성",
    hanja: "蓋然性",
    hun: "덮을/대개 개(蓋), 그러할 연(然), 성품 성(性)",
    type: "meaning",
    typeLabel: "뜻 확인형",
    isCreative: false,
    sourceLabel: "표준국어대사전 규범 정의",
    question: "학술 논의에서 ‘개연성(蓋然性)’의 의미로 가장 적절한 것은?",
    passage: null,
    options: [
      { id: "b18-opt-1", text: "어떤 경우에도 절대 변하지 않는 영원불변의 법칙", isCorrect: false },
      { id: "b18-opt-2", text: "절대적으로 확실하지는 않으나 대개 그러할 법한 성질", isCorrect: true },
      { id: "b18-opt-3", text: "상식적으로 전혀 일어날 수 없는 황당무계한 공상", isCorrect: false },
      { id: "b18-opt-4", text: "이전부터 전통적으로 전해 내려오는 고유한 풍습", isCorrect: false }
    ],
    definition: "『철학』 절대적으로 확실하지 않으나 아마 그럴 것이라고 생각되는 성질.",
    explanation: "‘개연성’은 반드시 그렇게 된다는 필연성이나 전혀 일어날 수 없다는 불가능성과 달리, 현실적으로 충분히 일어날 법하다고 여겨지는 그럴듯한 성질을 뜻합니다."
  },
  {
    id: "batch01-19",
    word: "당위",
    hanja: "當爲",
    hun: "마땅 당(當), 할 위(爲)",
    type: "meaning",
    typeLabel: "뜻 확인형",
    isCreative: false,
    sourceLabel: "표준국어대사전 규범 정의",
    question: "윤리학과 철학에서 ‘당위(當爲)’의 뜻으로 가장 적절한 것은?",
    passage: null,
    options: [
      { id: "b19-opt-1", text: "마땅히 지키거나 행해야 할 도리나 법칙", isCorrect: true },
      { id: "b19-opt-2", text: "자연계나 사회에서 실제로 관찰되는 사실", isCorrect: false },
      { id: "b19-opt-3", text: "개인의 이익을 채우기 위해 세운 은밀한 계획", isCorrect: false },
      { id: "b19-opt-4", text: "정당이나 당파가 가지고 있는 정치적 세력", isCorrect: false }
    ],
    definition: "마땅히 그렇게 하거나 되어야 하는 것.",
    explanation: "‘당위’는 실제로 존재하는 ‘사실’과 대비되어, 가치 판단상 ‘마땅히 그렇게 해야만 하는 도리나 법칙’을 뜻합니다."
  }
];
