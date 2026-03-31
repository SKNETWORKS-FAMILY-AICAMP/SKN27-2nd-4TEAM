import { ArrowRight, TrendingDown, ShoppingCart, Tag, AlertCircle, Smartphone } from "lucide-react";
import {
  AreaChart, Area, BarChart, Bar, LineChart, Line,
  XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend
} from "recharts";

// =============================================
// 실제 데이터 (통계청 + 한국은행 + Kaggle)
// =============================================

const connections = [
  {
    trend: "소비 위축 · 지출 감소",
    icon: TrendingDown,
    trendColor: "#D97A7A",
    trendBg: "#FDEAEA",
    metric: "OrderCount 감소",
    metricDesc: "이탈 고객 2.82회 vs 유지 고객 3.05회",
    metricColor: "#C45A5A",
    metricBg: "#FDEAEA",
  },
  {
    trend: "구매 공백 증가",
    icon: ShoppingCart,
    trendColor: "#E6A050",
    trendBg: "#FDF1E3",
    metric: "DaySinceLastOrder 증가",
    metricDesc: "이탈 고객 3.24일 vs 유지 고객 4.81일",
    metricColor: "#B87535",
    metricBg: "#FDF1E3",
  },
  {
    trend: "가성비 소비 증가",
    icon: Tag,
    trendColor: "#4A6FA5",
    trendBg: "#EEF2F8",
    metric: "CouponUsed 차이",
    metricDesc: "이탈 고객 1.72개 vs 유지 고객 1.76개",
    metricColor: "#3A5A8C",
    metricBg: "#EEF2F8",
  },
  {
    trend: "모바일 쇼핑 확대",
    icon: Smartphone,
    trendColor: "#5FAD56",
    trendBg: "#EDF7EC",
    metric: "모바일 비중 급증",
    metricDesc: "2020년 69% → 2026년 78.2%",
    metricColor: "#3D7A3C",
    metricBg: "#EDF7EC",
  },
];

// 온라인쇼핑 거래액 연도별 (통계청)
const shoppingData = [
  { year: "2020", amount: 1319, growth: null },
  { year: "2021", amount: 1606, growth: 21.8 },
  { year: "2022", amount: 1801, growth: 12.1 },
  { year: "2023", amount: 2018, growth: 12.0 },
  { year: "2024", amount: 2187, growth: 8.4 },
  { year: "2025", amount: 2292, growth: 4.8 },
  { year: "2026", amount: 2410, growth: 5.1 },
];

// CCSI 연도별 (한국은행)
const ccsiData = [
  { year: "2020", ccsi: 87.4 },
  { year: "2021", ccsi: 103.4 },
  { year: "2022", ccsi: 95.5 },
  { year: "2023", ccsi: 97.2 },
  { year: "2024", ccsi: 99.8 },
  { year: "2025", ccsi: 103.9 },
  { year: "2026", ccsi: 110.8 },
];

// 모바일 비중 연도별
const mobileData = [
  { year: "2020", ratio: 69.0 },
  { year: "2021", ratio: 73.2 },
  { year: "2022", ratio: 75.5 },
  { year: "2023", ratio: 75.1 },
  { year: "2024", ratio: 76.2 },
  { year: "2025", ratio: 77.5 },
  { year: "2026", ratio: 78.2 },
];

// 이탈 vs 유지 고객 비교 (Kaggle 데이터셋)
const churnCompareData = [
  { metric: "주문횟수", churn: 2.82, retain: 3.05 },
  { metric: "쿠폰사용", churn: 1.72, retain: 1.76 },
  { metric: "캐시백(÷10)", churn: 16.0, retain: 18.1 },
];

// 카테고리별 이탈률
const categoryChurnData = [
  { cat: "식료품",    rate: 4.9  },
  { cat: "기타",      rate: 7.6  },
  { cat: "노트북/가전", rate: 10.2 },
  { cat: "패션",      rate: 15.5 },
  { cat: "모바일",    rate: 27.2 },
  { cat: "휴대폰",    rate: 27.5 },
];

// =============================================
// 커스텀 툴팁
// =============================================
function CT({ active, payload, label, map }) {
  if (!active || !payload?.length) return null;
  return (
    <div className="bg-white border border-slate-200 rounded-lg px-3 py-2.5 shadow text-xs space-y-1">
      <p className="font-medium text-slate-700">{label}</p>
      {payload.map((p, i) => (
        <p key={i} style={{ color: p.stroke || p.fill }}>
          {map?.[p.dataKey] || p.dataKey}: {p.value}
        </p>
      ))}
    </div>
  );
}

// =============================================
// 메인 컴포넌트
// =============================================
export default function ConsumerTrends() {
  return (
    <div className="space-y-5 p-4 max-w-4xl mx-auto">

      {/* 헤더 */}
      <div>
        <h1 className="text-xl font-bold text-slate-800">소비 트렌드 분석</h1>
        <p className="text-sm text-slate-500 mt-0.5">
          통계청 온라인쇼핑 동향 × 한국은행 CCSI × 이커머스 고객 데이터
        </p>
      </div>

      {/* KPI 카드 */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
        {[
          { label: "온라인쇼핑 거래액", value: "2,410억", sub: "2026.01 기준", color: "#4A6FA5" },
          { label: "소비자심리지수", value: "110.8", sub: "2026.01 낙관", color: "#5FAD56" },
          { label: "모바일 비중", value: "78.2%", sub: "2020년 대비 +9.2%p", color: "#E6A050" },
          { label: "전체 이탈률", value: "16.8%", sub: "5,630명 기준", color: "#D97A7A" },
        ].map((kpi, i) => (
          <div key={i} className="bg-white rounded-xl border border-slate-100 shadow-sm p-4">
            <p className="text-xs text-slate-400 mb-1">{kpi.label}</p>
            <p className="text-xl font-bold" style={{ color: kpi.color }}>{kpi.value}</p>
            <p className="text-xs text-slate-400 mt-0.5">{kpi.sub}</p>
          </div>
        ))}
      </div>

      {/* 트렌드 → 데이터 연결 */}
      <div className="bg-white rounded-xl border border-slate-100 shadow-sm p-5">
        <h3 className="font-semibold text-sm text-slate-800 mb-0.5">소비 트렌드 → 고객 데이터 연결</h3>
        <p className="text-xs text-slate-400 mb-6">한국 소비 트렌드가 이커머스 고객 지표에 미치는 영향</p>
        <div className="space-y-3">
          {connections.map((c, i) => (
            <div key={i} className="grid grid-cols-[1fr_auto_1fr] items-center gap-3">
              <div
                className="flex items-center gap-2.5 px-4 py-3 rounded-lg border"
                style={{ backgroundColor: c.trendBg, borderColor: `${c.trendColor}35` }}
              >
                <div
                  className="w-7 h-7 rounded-md flex items-center justify-center flex-shrink-0"
                  style={{ backgroundColor: `${c.trendColor}25` }}
                >
                  <c.icon className="w-3.5 h-3.5" style={{ color: c.trendColor }} />
                </div>
                <div>
                  <p className="text-[10px] text-slate-400 font-medium">한국 트렌드</p>
                  <p className="text-xs font-semibold text-slate-700">{c.trend}</p>
                </div>
              </div>
              <div className="flex items-center justify-center">
                <ArrowRight className="w-5 h-5" style={{ color: c.trendColor }} />
              </div>
              <div
                className="px-4 py-3 rounded-lg border"
                style={{ backgroundColor: c.metricBg, borderColor: `${c.metricColor}35` }}
              >
                <p className="text-xs font-bold" style={{ color: c.metricColor }}>{c.metric}</p>
                <p className="text-xs text-slate-500 mt-0.5">{c.metricDesc}</p>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* 차트 2개 */}
      <div className="grid lg:grid-cols-2 gap-5">

        {/* 온라인쇼핑 거래액 */}
        <div className="bg-white rounded-xl border border-slate-100 shadow-sm p-5">
          <h3 className="font-semibold text-sm text-slate-800 mb-0.5">온라인쇼핑 거래액 추이</h3>
          <p className="text-xs text-slate-400 mb-5">통계청 · 연도별 평균 (억원)</p>
          <div className="h-52">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={shoppingData}>
                <defs>
                  <linearGradient id="shopG" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stopColor="#4A6FA5" stopOpacity={0.25} />
                    <stop offset="100%" stopColor="#4A6FA5" stopOpacity={0.02} />
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" stroke="#F1F5F9" />
                <XAxis dataKey="year" tick={{ fontSize: 11 }} axisLine={false} tickLine={false} />
                <YAxis tick={{ fontSize: 11 }} axisLine={false} tickLine={false} />
                <Tooltip content={(p) => <CT {...p} map={{ amount: "거래액(억)" }} />} />
                <Area
                  type="monotone" dataKey="amount"
                  stroke="#4A6FA5" strokeWidth={2.5}
                  fill="url(#shopG)"
                />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* CCSI 추이 */}
        <div className="bg-white rounded-xl border border-slate-100 shadow-sm p-5">
          <h3 className="font-semibold text-sm text-slate-800 mb-0.5">소비자심리지수(CCSI)</h3>
          <p className="text-xs text-slate-400 mb-5">한국은행 · 100 미만 = 소비 위축</p>
          <div className="h-52">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={ccsiData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#F1F5F9" />
                <XAxis dataKey="year" tick={{ fontSize: 11 }} axisLine={false} tickLine={false} />
                <YAxis domain={[70, 120]} tick={{ fontSize: 11 }} axisLine={false} tickLine={false} />
                <Tooltip content={(p) => <CT {...p} map={{ ccsi: "CCSI" }} />} />
                <Bar
                  dataKey="ccsi"
                  radius={[4, 4, 0, 0]}
                  opacity={0.9}
                  fill="#D97A7A"
                  // 100 이상이면 초록, 미만이면 빨강
                  label={false}
                >
                  {ccsiData.map((entry, index) => (
                    <rect
                      key={index}
                      fill={entry.ccsi >= 100 ? "#5FAD56" : "#D97A7A"}
                    />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
          <div className="flex gap-3 mt-2">
            <span className="flex items-center gap-1 text-xs text-slate-500">
              <span className="w-2.5 h-2.5 rounded-sm inline-block" style={{ background: "#5FAD56" }} />
              낙관 (100↑)
            </span>
            <span className="flex items-center gap-1 text-xs text-slate-500">
              <span className="w-2.5 h-2.5 rounded-sm inline-block" style={{ background: "#D97A7A" }} />
              위축 (100↓)
            </span>
          </div>
        </div>
      </div>

      {/* 이탈 vs 유지 + 카테고리 이탈률 */}
      <div className="grid lg:grid-cols-2 gap-5">

        {/* 이탈 vs 유지 비교 */}
        <div className="bg-white rounded-xl border border-slate-100 shadow-sm p-5">
          <h3 className="font-semibold text-sm text-slate-800 mb-0.5">이탈 vs 유지 고객 비교</h3>
          <p className="text-xs text-slate-400 mb-5">이커머스 데이터셋 기반</p>
          <div className="h-52">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={churnCompareData} layout="vertical">
                <CartesianGrid strokeDasharray="3 3" stroke="#F1F5F9" />
                <XAxis type="number" tick={{ fontSize: 11 }} axisLine={false} tickLine={false} />
                <YAxis dataKey="metric" type="category" tick={{ fontSize: 11 }} axisLine={false} tickLine={false} width={60} />
                <Tooltip content={(p) => <CT {...p} map={{ churn: "이탈", retain: "유지" }} />} />
                <Legend
                  wrapperStyle={{ fontSize: 11 }}
                  formatter={(v) => v === "churn" ? "이탈 고객" : "유지 고객"}
                />
                <Bar dataKey="churn"  fill="#D97A7A" radius={[0, 4, 4, 0]} opacity={0.9} />
                <Bar dataKey="retain" fill="#4A6FA5" radius={[0, 4, 4, 0]} opacity={0.9} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* 카테고리별 이탈률 */}
        <div className="bg-white rounded-xl border border-slate-100 shadow-sm p-5">
          <h3 className="font-semibold text-sm text-slate-800 mb-0.5">카테고리별 이탈률</h3>
          <p className="text-xs text-slate-400 mb-5">이커머스 데이터셋 기반 (%)</p>
          <div className="h-52">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={categoryChurnData} layout="vertical">
                <CartesianGrid strokeDasharray="3 3" stroke="#F1F5F9" />
                <XAxis type="number" unit="%" tick={{ fontSize: 11 }} axisLine={false} tickLine={false} />
                <YAxis dataKey="cat" type="category" tick={{ fontSize: 11 }} axisLine={false} tickLine={false} width={55} />
                <Tooltip content={(p) => <CT {...p} map={{ rate: "이탈률" }} />} />
                <Bar dataKey="rate" radius={[0, 4, 4, 0]} opacity={0.9}>
                  {categoryChurnData.map((entry, i) => (
                    <rect key={i} fill={entry.rate > 20 ? "#D97A7A" : entry.rate > 10 ? "#E6A050" : "#5FAD56"} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* 모바일 비중 추이 */}
      <div className="bg-white rounded-xl border border-slate-100 shadow-sm p-5">
        <h3 className="font-semibold text-sm text-slate-800 mb-0.5">모바일쇼핑 비중 추이</h3>
        <p className="text-xs text-slate-400 mb-5">통계청 · 2020~2026 (%)</p>
        <div className="h-52">
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart data={mobileData}>
              <defs>
                <linearGradient id="mobG" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stopColor="#5FAD56" stopOpacity={0.25} />
                  <stop offset="100%" stopColor="#5FAD56" stopOpacity={0.02} />
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" stroke="#F1F5F9" />
              <XAxis dataKey="year" tick={{ fontSize: 11 }} axisLine={false} tickLine={false} />
              <YAxis domain={[60, 85]} unit="%" tick={{ fontSize: 11 }} axisLine={false} tickLine={false} />
              <Tooltip content={(p) => <CT {...p} map={{ ratio: "모바일 비중(%)" }} />} />
              <Area
                type="monotone" dataKey="ratio"
                stroke="#5FAD56" strokeWidth={2.5}
                fill="url(#mobG)"
                dot={{ r: 4, fill: "#5FAD56", strokeWidth: 0 }}
              />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* 인사이트 카드 */}
      <div className="grid md:grid-cols-2 gap-4">
        <div
          className="flex gap-3 bg-white rounded-xl border-l-4 p-5 shadow-sm"
          style={{ borderLeftColor: "#D97A7A" }}
        >
          <AlertCircle className="w-5 h-5 flex-shrink-0 mt-0.5" style={{ color: "#D97A7A" }} />
          <div>
            <p className="text-xs font-bold mb-1" style={{ color: "#D97A7A" }}>인사이트 01</p>
            <p className="text-sm font-medium text-slate-700 leading-relaxed">
              2022~2024년 3년 연속 소비 심리 위축(CCSI 100 미만).
              이 기간 구매 빈도 감소 → 이탈 위험 증가.
            </p>
          </div>
        </div>
        <div
          className="flex gap-3 bg-white rounded-xl border-l-4 p-5 shadow-sm"
          style={{ borderLeftColor: "#E6A050" }}
        >
          <Tag className="w-5 h-5 flex-shrink-0 mt-0.5" style={{ color: "#E6A050" }} />
          <div>
            <p className="text-xs font-bold mb-1" style={{ color: "#E6A050" }}>인사이트 02</p>
            <p className="text-sm font-medium text-slate-700 leading-relaxed">
              캐시백 금액이 낮은 이탈 고객(160원) 대비
              유지 고객(180원) → 혜택 제공이 핵심 전략.
            </p>
          </div>
        </div>
        <div
          className="flex gap-3 bg-white rounded-xl border-l-4 p-5 shadow-sm"
          style={{ borderLeftColor: "#5FAD56" }}
        >
          <Smartphone className="w-5 h-5 flex-shrink-0 mt-0.5" style={{ color: "#5FAD56" }} />
          <div>
            <p className="text-xs font-bold mb-1" style={{ color: "#5FAD56" }}>인사이트 03</p>
            <p className="text-sm font-medium text-slate-700 leading-relaxed">
              모바일 비중 78.2%. 모바일 기반 푸시 알림 및
              앱 전용 쿠폰 전략이 유효함.
            </p>
          </div>
        </div>
        <div
          className="flex gap-3 bg-white rounded-xl border-l-4 p-5 shadow-sm"
          style={{ borderLeftColor: "#4A6FA5" }}
        >
          <ShoppingCart className="w-5 h-5 flex-shrink-0 mt-0.5" style={{ color: "#4A6FA5" }} />
          <div>
            <p className="text-xs font-bold mb-1" style={{ color: "#4A6FA5" }}>인사이트 04</p>
            <p className="text-sm font-medium text-slate-700 leading-relaxed">
              모바일·휴대폰 카테고리 이탈률 27%↑.
              식료품 카테고리(4.9%)로 재유입 유도 쿠폰 전략 추천.
            </p>
          </div>
        </div>
      </div>

    </div>
  );
}
