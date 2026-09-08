# 한알국쉬 수능 연구 기록 및 감사 보고서 (Research & Audit Records)

## 1. 개요 및 목적

본 `research/` 디렉터리는 **한알국쉬 수능([suneung.easyhanja.org](https://suneung.easyhanja.org/))**의 코퍼스 구축, 단계별 편찬 검증, AI 생성 오류 색출 및 교정 과정에 관한 모든 연구 통계와 작업시간 감사 기록을 보존하기 위해 생성되었습니다.

- **기준 최종 배포 준비 HEAD**: `a18f436` (Phase 5 SEO 기준본)
- **최종 코퍼스 규모**: 701 표제어 / 879 기출 문맥 / 17개 평가원 기출 전수
- **학술적 목적**: LLM 기반 코퍼스 편찬 시 발생하는 실제 오류(환각, 다의어 오염, 스키마 잔재, 출전 왜곡 등)의 실증적 분류 체계를 수립하고, AI 보조 연구의 투입 시간 및 공수를 객관적으로 측정·보고할 수 있는 근거를 제공함.

> [!NOTE]
> **Phase 6B 통계 교정 감사(Metrics Reconciliation Audit)**:
> Phase 6에서 자동 집계된 연구 통계 자체도 Git 실제 커밋 객체, 커밋별 `js/data.js`, 보존된 `research/evidence/` 매니페스트 원자료와 다시 1:1 대조하여 교정되었습니다. AI는 원자료 편찬 단계뿐만 아니라 후속 통계 요약·집계 단계에서도 서로 다른 지표(예: 도구 호출 요청 수와 도구 실행 응답 이벤트)를 하나로 합치거나, 순감소량(Net change: -25)과 원시 삭제 건수(Raw removed: 26)를 혼동할 수 있음이 확인되었습니다. 본 디렉터리의 모든 수치는 Phase 6B 재검증을 거쳐 확정된 값입니다.

---

## 2. 디렉터리 구성 및 파일 설명

```text
research/
├── README.md                      # 본 연구 기록 안내 문서 (Phase 6B 교정 반영)
├── correction_log.md              # Phase 6B 통계 및 서술 교정 상세 일지 (OLD / EVIDENCE / NEW / STATUS)
├── phase6b_correction_audit.json  # Phase 6B 교정 수치 감사 데이터 (기계 판독형)
├── project_metrics.json           # 기계 판독 가능한 최종 종합 연구 메트릭 (교정 반영)
├── git_timeline.csv               # 최초 배포부터 HEAD a18f436까지의 Git 커밋 전수 타임라인 (42개 커밋)
├── worktime_audit.json            # AntiGravity 세션 로그 기반 작업시간 감사 상세 기록 (상한/엄격 프록시 분리)
├── ai_error_cases.md              # 실증 사례 20선 및 엄격한 5개 범주화 분석표
├── presentation_statistics.md     # 학술 발표 및 대외 보고용 핵심 인용문, 표준 통계 및 시간 표현
└── evidence/                      # 검증에 사용된 13개 핵심 JSON 매니페스트 원본 보존 (수정 금지 참조용)
```

### 각 파일 상세 설명

1. **`correction_log.md`**:
   - Phase 6의 기존 주장과 Phase 6B 재검증 결과를 12개 주요 쟁점별로 비교하고, 검증 근거와 교정 판정 상태(`CORRECTED`, `DOWNGRADED` 등)를 명시한 감사 일지입니다.
2. **`phase6b_correction_audit.json`**:
   - 문맥 제거/추가 내역, 사전 출처 검증 내역, 스키마 정리, 도구 사용량, 활동 프록시 등 Phase 6B에서 재계산된 수치를 담은 구조화 데이터입니다.
3. **`project_metrics.json`**:
   - 최종 데이터베이스 통계(표제어, 문맥, 출전, 갈래, 카테고리, 난이도, 사전 출처 분포), 체크포인트 이력, Git 기술 통계(Churn), 작업시간 요약, 검증/정비 성과 지표를 일원화한 JSON 문서입니다.
4. **`git_timeline.csv`**:
   - Git 저장소의 전체 커밋 이력을 시간순으로 추출하여 커밋 해시, 작성 일시, 커밋 일시, 메시지, 변경 파일 수, 추가/삭제 라인 수를 기록한 CSV 파일입니다.
5. **`worktime_audit.json`**:
   - AntiGravity IDE 세션 트랜스크립트 로그를 바탕으로 산출한 경과시간(Wall-clock span)과 10분 상한 활동 프록시(Interval-capped proxy), 10분 엄격 갭 배제 프록시(Strict gap-exclusion proxy), 16개 작업 세션 분할 내역, 15개 세부 Phase별 소요 시간 분석을 담고 있습니다.
6. **`ai_error_cases.md`**:
   - 수능 코퍼스 편찬 중 관찰된 20개 사례를 실제 오류(`ACTUAL_ERROR`: 5건), 편찬상 정제(`EDITORIAL_REFINEMENT`: 3건), 동음어 구별 정제(`DISAMBIGUATION_REFINEMENT`: 6건), 공정 관찰(`PROCESS_OBSERVATION`: 5건), 잠재 위험(`POTENTIAL_RISK`: 1건)으로 엄격히 분류한 분석 보고서입니다.
7. **`presentation_statistics.md`**:
   - 학술 발표나 논문에서 즉시 인용할 수 있는 4대 핵심 연구 명제, 작업시간 표현 표준 문장 3종, 10대 핵심 통계 지표, 대표 사례 5선을 선별한 문서입니다.
8. **`evidence/`**:
   - Phase 2부터 Phase 5까지의 단계별 검증 매니페스트 및 전수 감사 JSON 파일 13건을 원형 그대로 보존한 디렉터리입니다. 본 디렉터리의 파일들은 교정 대상이 아닌 원천 근거 자료입니다.

---

## 3. 작업시간 산출 방법론 및 주의사항

### A. 총 경과시간(Wall-Clock Span) vs 추정 순 작업시간 프록시(Active Working Time Proxy)
- **총 경과시간(Wall-Clock Span)**: 최초 작업 로그의 타임스탬프부터 최종 작업 로그 타임스탬프까지의 단순 달력상 경과 시간입니다. 여기에는 연구자의 수면, 식사, 휴식, 기타 학술 업무 시간이 모두 포함되어 있습니다.
- **인터벌 캡 프록시 (Interval-Capped Proxy: $\sum \min(\Delta t, \text{threshold})$)**:
  - 연속 이벤트 간격 $\Delta t$가 임계치를 초과할 경우 최대 임계치로 상한을 두어 가산하는 방식입니다. (10분 임계치 기준: 9월 캠페인 약 18.3시간, Range B 약 4.1시간)
  - 이는 비활동 구간을 0으로 전액 배제하는 방식이 아니므로, 상한 처리된 활동 프록시로 표기해야 합니다.
- **엄격 갭 배제 프록시 (Strict Gap-Exclusion Proxy: $\sum [\Delta t \le \text{threshold} \times \Delta t]$)**:
  - 10분을 초과하는 간격을 비활동으로 간주하여 전액 0으로 배제한 보수적 하한선 프록시입니다. (10분 기준: 9월 캠페인 약 15.0시간, Range B 약 3.6시간)

### B. 신뢰도 등급 (Confidence Rating)
- **FINAL EDITORIAL / VALIDATION RANGE (`7204b1d` ~ `a18f436`)**: **`ESTIMATED`**
  - 기출 전수 입력 마감 이후의 정밀 검증 및 배포 준비 구간으로, 1,689건의 이벤트와 806회의 실제 모델 도구 호출이 100% 온전히 기록되어 있습니다.
- **SEPTEMBER COMPILATION CAMPAIGN (2026-09-06 ~ 2026-09-08)**: **`ESTIMATED`**
  - 6개년 평가원 기출 전수 입력 및 재검증부터 최종 배포 준비까지 이어진 3일간의 집중 캠페인으로, 6,090건의 이벤트가 온전히 기록되었습니다.
- **FULL PROJECT RANGE (2026-06-20 ~ 2026-09-08)**: **`PARTIAL`**
  - 6월 초기 프로토타입 설계 로그는 존재하나, 7~8월 중 리트 분기 및 오프라인 기출 연구 구간의 세션 로그가 분절되어 있으므로 `PARTIAL` 등급을 엄격히 적용합니다.

---

## 4. 데이터베이스 사실 데이터와의 분리 원칙

- 웹 배포 및 서비스 런타임에 직접 사용되는 실제 데이터는 `js/data.js`에 엄격히 보존되어 있으며, Phase 5 및 Phase 6, Phase 6B를 거치며 **단 1바이트의 변경도 없이 완전히 동결(0 diff)**되었습니다.
- 본 `research/` 디렉터리에 포함된 모든 통계, 로그 감사치, 오류 분석표는 연구 분석용 2차 산출물이므로 웹 서비스 구동 코드에 어떠한 영향도 미치지 않습니다.
