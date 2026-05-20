import streamlit as st

st.title("🎈 SimuLab")
st.write(
    "Let's start finding!"
)
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SimuLab — Indikator Asam Basa</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0c10;
    --surface: #12151c;
    --surface2: #1a1e28;
    --border: rgba(255,255,255,0.07);
    --text: #e8eaf0;
    --muted: #6b7280;
    --accent: #7ef5c0;
    --acid-color: #ff6b6b;
    --base-color: #60a5fa;
    --neutral-color: #a3e635;
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* Background grid */
  body::before {
    content: '';
    position: fixed; inset: 0;
    background-image:
      linear-gradient(rgba(126,245,192,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(126,245,192,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
  }

  .header {
    padding: 2rem 2rem 1rem;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: baseline;
    gap: 1.5rem;
  }

  .logo {
    font-family: 'Space Mono', monospace;
    font-size: 1.4rem;
    color: var(--accent);
    letter-spacing: -0.02em;
  }

  .logo span { color: var(--muted); }

  .tagline {
    font-size: 0.8rem;
    color: var(--muted);
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }

  .main {
    max-width: 1100px;
    margin: 0 auto;
    padding: 2.5rem 2rem;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    align-items: start;
  }

  /* ---- Controls panel ---- */
  .panel {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.8rem;
  }

  .panel-title {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    color: var(--accent);
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 1.6rem;
  }

  .field { margin-bottom: 1.4rem; }

  .label {
    display: block;
    font-size: 0.8rem;
    color: var(--muted);
    margin-bottom: 0.6rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    font-weight: 500;
  }

  .select-wrap { position: relative; }

  select {
    width: 100%;
    background: var(--surface2);
    border: 1px solid var(--border);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    font-size: 0.95rem;
    padding: 0.75rem 2.5rem 0.75rem 1rem;
    border-radius: 10px;
    appearance: none;
    cursor: pointer;
    transition: border-color 0.2s;
    outline: none;
  }

  select:focus, select:hover { border-color: rgba(126,245,192,0.3); }

  .select-wrap::after {
    content: '▾';
    position: absolute;
    right: 1rem;
    top: 50%;
    transform: translateY(-50%);
    color: var(--muted);
    pointer-events: none;
    font-size: 0.8rem;
  }

  .run-btn {
    width: 100%;
    padding: 0.9rem;
    background: var(--accent);
    color: #0a0c10;
    font-family: 'Space Mono', monospace;
    font-size: 0.9rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    transition: transform 0.15s, box-shadow 0.15s, filter 0.15s;
    margin-top: 0.4rem;
  }

  .run-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(126,245,192,0.2);
    filter: brightness(1.08);
  }

  .run-btn:active { transform: translateY(0); }

  /* info cards below select */
  .solution-info {
    margin-top: 0.6rem;
    padding: 0.7rem 1rem;
    background: var(--surface2);
    border-radius: 8px;
    font-size: 0.82rem;
    color: var(--muted);
    line-height: 1.5;
    min-height: 2.5rem;
    transition: all 0.3s;
  }

  /* ---- Result panel ---- */
  .result-panel {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.8rem;
    display: flex;
    flex-direction: column;
    gap: 1.4rem;
  }

  .ph-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    color: var(--accent);
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 1rem;
  }

  .ph-display {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    margin-bottom: 1rem;
  }

  .ph-value {
    font-family: 'Space Mono', monospace;
    font-size: 3.2rem;
    font-weight: 700;
    line-height: 1;
    transition: color 0.5s;
  }

  .ph-nature {
    display: flex;
    flex-direction: column;
    gap: 0.3rem;
  }

  .nature-badge {
    display: inline-block;
    padding: 0.3rem 0.9rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    background: transparent;
    border: 2px solid;
    transition: all 0.5s;
  }

  .ph-formula {
    font-size: 0.78rem;
    color: var(--muted);
    font-family: 'Space Mono', monospace;
  }

  /* pH bar */
  .ph-bar-wrap {
    position: relative;
    height: 20px;
    border-radius: 10px;
    overflow: hidden;
    background: linear-gradient(to right,
      #ff2d2d 0%, #ff7b00 14%, #ffcc00 25%,
      #a8e063 36%, #56ab2f 50%,
      #4fc3f7 64%, #1565c0 75%,
      #7b1fa2 86%, #4a148c 100%);
    margin-bottom: 0.5rem;
  }

  .ph-bar-labels {
    display: flex;
    justify-content: space-between;
    font-size: 0.65rem;
    color: var(--muted);
    font-family: 'Space Mono', monospace;
    padding: 0 2px;
  }

  .ph-cursor {
    position: absolute;
    top: -4px;
    width: 4px;
    height: 28px;
    background: white;
    border-radius: 2px;
    box-shadow: 0 0 8px rgba(255,255,255,0.9);
    transition: left 0.7s cubic-bezier(0.34,1.56,0.64,1);
    transform: translateX(-50%);
  }

  /* Beaker */
  .beaker-section {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
  }

  .beaker-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    color: var(--accent);
    letter-spacing: 0.14em;
    text-transform: uppercase;
    align-self: flex-start;
  }

  .beaker-container {
    width: 100%;
    display: flex;
    gap: 1.5rem;
    justify-content: center;
    flex-wrap: wrap;
  }

  .beaker-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
  }

  .beaker-name {
    font-size: 0.75rem;
    color: var(--muted);
    font-family: 'Space Mono', monospace;
  }

  /* SVG beaker */
  .beaker-svg { filter: drop-shadow(0 4px 12px rgba(0,0,0,0.4)); }

  .liquid {
    transition: fill 0.8s ease, opacity 0.8s ease;
  }

  .color-chip {
    display: inline-block;
    width: 18px; height: 18px;
    border-radius: 4px;
    border: 1px solid rgba(255,255,255,0.15);
    vertical-align: middle;
    transition: background 0.7s ease;
  }

  /* indicator result rows */
  .indicator-results { display: flex; flex-direction: column; gap: 0.6rem; }

  .ind-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.75rem 1rem;
    background: var(--surface2);
    border-radius: 10px;
    border: 1px solid var(--border);
    transition: border-color 0.3s;
  }

  .ind-row.active { border-color: rgba(126,245,192,0.25); }

  .ind-name { font-size: 0.85rem; font-weight: 500; }
  .ind-range { font-size: 0.72rem; color: var(--muted); font-family: 'Space Mono', monospace; }

  .ind-color-display {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.8rem;
  }

  .swatch {
    width: 24px; height: 24px;
    border-radius: 6px;
    border: 1px solid rgba(255,255,255,0.1);
    transition: background 0.7s ease;
    flex-shrink: 0;
  }

  /* Placeholder state */
  .placeholder {
    text-align: center;
    padding: 3rem 1rem;
    color: var(--muted);
    font-size: 0.85rem;
    line-height: 1.8;
  }

  .placeholder-icon {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    opacity: 0.4;
  }

  /* Animation */
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .animate-in { animation: fadeIn 0.4s ease forwards; }

  @keyframes bubble {
    0%, 100% { transform: translateY(0) scale(1); opacity: 0.6; }
    50% { transform: translateY(-8px) scale(1.15); opacity: 1; }
  }

  .bubble {
    animation: bubble 2s ease-in-out infinite;
  }

  .bubble:nth-child(2) { animation-delay: 0.4s; }
  .bubble:nth-child(3) { animation-delay: 0.8s; }

  @media (max-width: 700px) {
    .main { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>

<header class="header">
  <div class="logo">SimuLab<span>.</span></div>
  <div class="tagline">Simulasi Indikator Asam–Basa</div>
</header>

<div class="main">
  <!-- Controls -->
  <div class="panel">
    <div class="panel-title">// Parameter Larutan</div>

    <div class="field">
      <label class="label" for="sol">Pilih Larutan</label>
      <div class="select-wrap">
        <select id="sol" onchange="updateSolutionInfo()">
          <option value="">— pilih larutan —</option>
          <optgroup label="⚡ ASAM KUAT">
            <option value="HCl_1">HCl 1 M — Asam Klorida</option>
            <option value="HCl_01">HCl 0.1 M — Asam Klorida</option>
            <option value="HCl_001">HCl 0.01 M — Asam Klorida</option>
            <option value="H2SO4_1">H₂SO₄ 1 M — Asam Sulfat</option>
            <option value="H2SO4_01">H₂SO₄ 0.1 M — Asam Sulfat</option>
            <option value="HNO3_1">HNO₃ 1 M — Asam Nitrat</option>
            <option value="HNO3_01">HNO₃ 0.1 M — Asam Nitrat</option>
            <option value="HBr">HBr 0.1 M — Asam Bromida</option>
            <option value="HI">HI 0.1 M — Asam Iodida</option>
            <option value="HClO4">HClO₄ 0.1 M — Asam Perklorat</option>
          </optgroup>
          <optgroup label="🔶 ASAM LEMAH">
            <option value="CH3COOH_1">CH₃COOH 1 M — Asam Asetat</option>
            <option value="CH3COOH_01">CH₃COOH 0.1 M — Asam Asetat</option>
            <option value="CH3COOH_001">CH₃COOH 0.01 M — Asam Asetat</option>
            <option value="H2CO3">H₂CO₃ 0.03 M — Asam Karbonat</option>
            <option value="HF_01">HF 0.1 M — Asam Fluorida</option>
            <option value="H3PO4">H₃PO₄ 0.1 M — Asam Fosfat</option>
            <option value="HCN">HCN 0.1 M — Asam Sianida</option>
            <option value="HCOOH">HCOOH 0.1 M — Asam Format</option>
            <option value="H2C2O4">H₂C₂O₄ 0.1 M — Asam Oksalat</option>
            <option value="C6H5COOH">C₆H₅COOH 0.1 M — Asam Benzoat</option>
            <option value="H2S">H₂S 0.1 M — Asam Sulfida</option>
            <option value="HNO2">HNO₂ 0.1 M — Asam Nitrit</option>
            <option value="H3BO3">H₃BO₃ 0.1 M — Asam Borat</option>
            <option value="lactic">CH₃CH(OH)COOH 0.1 M — Asam Laktat</option>
            <option value="citric">C₆H₈O₇ 0.1 M — Asam Sitrat</option>
            <option value="ascorbic">C₆H₈O₆ 0.1 M — Asam Askorbat (Vit.C)</option>
          </optgroup>
          <optgroup label="🧊 LARUTAN NETRAL">
            <option value="H2O">H₂O — Air Murni</option>
            <option value="NaCl">NaCl 0.1 M — Natrium Klorida</option>
            <option value="KNO3">KNO₃ 0.1 M — Kalium Nitrat</option>
            <option value="Na2SO4">Na₂SO₄ 0.1 M — Natrium Sulfat</option>
            <option value="glukosa">C₆H₁₂O₆ 0.1 M — Glukosa</option>
          </optgroup>
          <optgroup label="🔷 GARAM TERHIDROLISIS (ASAM)">
            <option value="NH4Cl">NH₄Cl 0.1 M — Amonium Klorida</option>
            <option value="AlCl3">AlCl₃ 0.1 M — Aluminium Klorida</option>
            <option value="FeCl3">FeCl₃ 0.1 M — Besi(III) Klorida</option>
            <option value="CuSO4">CuSO₄ 0.1 M — Tembaga(II) Sulfat</option>
            <option value="ZnSO4">ZnSO₄ 0.1 M — Seng Sulfat</option>
          </optgroup>
          <optgroup label="🔷 GARAM TERHIDROLISIS (BASA)">
            <option value="Na2CO3">Na₂CO₃ 0.1 M — Natrium Karbonat</option>
            <option value="Na3PO4">Na₃PO₄ 0.1 M — Natrium Fosfat</option>
            <option value="CH3COONa">CH₃COONa 0.1 M — Natrium Asetat</option>
            <option value="NaHCO3">NaHCO₃ 0.1 M — Natrium Bikarbonat</option>
            <option value="Na2S">Na₂S 0.1 M — Natrium Sulfida</option>
            <option value="NaCN">NaCN 0.1 M — Natrium Sianida</option>
          </optgroup>
          <optgroup label="🟢 BASA LEMAH">
            <option value="NH3_01">NH₃ 0.1 M — Amonia</option>
            <option value="NH3_1">NH₃ 1 M — Amonia</option>
            <option value="N2H4">N₂H₄ 0.1 M — Hidrazin</option>
            <option value="C6H5NH2">C₆H₅NH₂ 0.1 M — Anilin</option>
            <option value="CH3NH2">CH₃NH₂ 0.1 M — Metilamina</option>
            <option value="pyridine">C₅H₅N 0.1 M — Piridin</option>
          </optgroup>
          <optgroup label="⚡ BASA KUAT">
            <option value="NaOH_001">NaOH 0.01 M — Natrium Hidroksida</option>
            <option value="NaOH_01">NaOH 0.1 M — Natrium Hidroksida</option>
            <option value="NaOH_1">NaOH 1 M — Natrium Hidroksida</option>
            <option value="KOH_01">KOH 0.1 M — Kalium Hidroksida</option>
            <option value="KOH_1">KOH 1 M — Kalium Hidroksida</option>
            <option value="Ca_OH_2">Ca(OH)₂ 0.1 M — Kalsium Hidroksida</option>
            <option value="Ba_OH_2">Ba(OH)₂ 0.1 M — Barium Hidroksida</option>
            <option value="LiOH">LiOH 0.1 M — Litium Hidroksida</option>
            <option value="Mg_OH_2">Mg(OH)₂ 0.01 M — Magnesium Hidroksida</option>
          </optgroup>
          <optgroup label="🧪 LARUTAN ALAMI / KEHIDUPAN">
            <option value="cuka">Cuka makan (~5% CH₃COOH)</option>
            <option value="jeruk">Jus Jeruk (~pH 3.5)</option>
            <option value="apel">Jus Apel (~pH 3.8)</option>
            <option value="tomat">Jus Tomat (~pH 4.2)</option>
            <option value="kopi">Kopi (~pH 5.0)</option>
            <option value="teh">Teh (~pH 5.5)</option>
            <option value="susu">Susu segar (~pH 6.5)</option>
            <option value="air_hujan">Air Hujan (~pH 5.6)</option>
            <option value="air_laut">Air Laut (~pH 8.1)</option>
            <option value="sabun">Larutan Sabun (~pH 9.5)</option>
            <option value="deterjen">Deterjen (~pH 10.5)</option>
            <option value="pemutih">Pemutih/Bayclin (~pH 12)</option>
            <option value="lambung">Asam Lambung (~pH 2.0)</option>
            <option value="darah">Darah manusia (~pH 7.4)</option>
            <option value="saliva">Saliva/Air Liur (~pH 6.8)</option>
            <option value="urin">Urin (~pH 6.0)</option>
          </optgroup>
        </select>
      </div>
      <div class="solution-info" id="sol-info">Pilih larutan untuk melihat informasi.</div>
    </div>

    <div class="field">
      <label class="label" for="ind">Pilih Indikator</label>
      <div class="select-wrap">
        <select id="ind">
          <option value="">— pilih indikator —</option>
          <option value="all">✦ Tampilkan Semua Indikator</option>
          <option value="pp">Fenolftalein (PP)</option>
          <option value="mo">Metil Jingga (MO)</option>
          <option value="litmus">Lakmus</option>
          <option value="mr">Metil Merah (MR)</option>
          <option value="btb">Bromtimol Biru (BTB)</option>
          <option value="universal">Indikator Universal</option>
        </select>
      </div>
    </div>

    <button class="run-btn" onclick="simulate()">⟶ JALANKAN SIMULASI</button>
  </div>

  <!-- Results -->
  <div class="result-panel" id="result-panel">
    <div class="placeholder" id="placeholder">
      <div class="placeholder-icon">⚗</div>
      <div>Pilih larutan dan indikator,<br>lalu klik <strong>Jalankan Simulasi</strong>.</div>
    </div>
    <div id="result-content" style="display:none; display:flex; flex-direction:column; gap:1.4rem;"></div>
  </div>
</div>

<script>
// ===================== DATA =====================
const solutions = {
  // === ASAM KUAT ===
  HCl_1:      { name:'HCl 1 M',        ph:0,    type:'asam',   strong:true,  formula:'HCl → H⁺ + Cl⁻',              desc:'Asam kuat monoprotic. Terionisasi sempurna. pH = 0.' },
  HCl_01:     { name:'HCl 0.1 M',      ph:1,    type:'asam',   strong:true,  formula:'HCl → H⁺ + Cl⁻',              desc:'Asam kuat, konsentrasi rendah. pH = −log[HCl] = 1.' },
  HCl_001:    { name:'HCl 0.01 M',     ph:2,    type:'asam',   strong:true,  formula:'HCl → H⁺ + Cl⁻',              desc:'Asam kuat, sangat encer.' },
  H2SO4_1:    { name:'H₂SO₄ 1 M',      ph:0,    type:'asam',   strong:true,  formula:'H₂SO₄ → 2H⁺ + SO₄²⁻',        desc:'Asam sulfat pekat. Sangat korosif dan eksotermis.' },
  H2SO4_01:   { name:'H₂SO₄ 0.1 M',    ph:0.7,  type:'asam',   strong:true,  formula:'H₂SO₄ → 2H⁺ + SO₄²⁻',        desc:'Asam kuat diprotik. Menghasilkan 2 mol H⁺ per mol.' },
  HNO3_1:     { name:'HNO₃ 1 M',       ph:0,    type:'asam',   strong:true,  formula:'HNO₃ → H⁺ + NO₃⁻',            desc:'Asam nitrat pekat. Oksidator kuat, berbahaya.' },
  HNO3_01:    { name:'HNO₃ 0.1 M',     ph:1,    type:'asam',   strong:true,  formula:'HNO₃ → H⁺ + NO₃⁻',            desc:'Asam kuat, digunakan dalam analisis kimia.' },
  HBr:        { name:'HBr 0.1 M',      ph:1,    type:'asam',   strong:true,  formula:'HBr → H⁺ + Br⁻',              desc:'Asam kuat halida. Terionisasi sempurna.' },
  HI:         { name:'HI 0.1 M',       ph:1,    type:'asam',   strong:true,  formula:'HI → H⁺ + I⁻',                desc:'Asam kuat terkuat di antara asam halida.' },
  HClO4:      { name:'HClO₄ 0.1 M',    ph:1,    type:'asam',   strong:true,  formula:'HClO₄ → H⁺ + ClO₄⁻',          desc:'Asam perklorat — asam okso terkuat yang dikenal.' },

  // === ASAM LEMAH ===
  CH3COOH_1:  { name:'CH₃COOH 1 M',   ph:2.4,  type:'asam',   strong:false, formula:'CH₃COOH ⇌ CH₃COO⁻ + H⁺',     desc:'Asam asetat. Ka = 1.8×10⁻⁵. Komponen utama cuka.' },
  CH3COOH_01: { name:'CH₃COOH 0.1 M', ph:2.9,  type:'asam',   strong:false, formula:'CH₃COOH ⇌ CH₃COO⁻ + H⁺',     desc:'Asam asetat encer. Terdapat dalam cuka makan ~5%.' },
  CH3COOH_001:{ name:'CH₃COOH 0.01 M',ph:3.4,  type:'asam',   strong:false, formula:'CH₃COOH ⇌ CH₃COO⁻ + H⁺',     desc:'Asam asetat sangat encer.' },
  H2CO3:      { name:'H₂CO₃ 0.03 M',  ph:4.2,  type:'asam',   strong:false, formula:'H₂CO₃ ⇌ HCO₃⁻ + H⁺',         desc:'Asam karbonat lemah. Terbentuk dari CO₂ + H₂O.' },
  HF_01:      { name:'HF 0.1 M',       ph:2.1,  type:'asam',   strong:false, formula:'HF ⇌ H⁺ + F⁻',                desc:'Asam fluorida. Ka = 7.2×10⁻⁴. Sangat toksik.' },
  H3PO4:      { name:'H₃PO₄ 0.1 M',   ph:1.6,  type:'asam',   strong:false, formula:'H₃PO₄ ⇌ H₂PO₄⁻ + H⁺',        desc:'Asam fosfat triprotik lemah. Ka₁ = 7.5×10⁻³.' },
  HCN:        { name:'HCN 0.1 M',      ph:5.1,  type:'asam',   strong:false, formula:'HCN ⇌ H⁺ + CN⁻',              desc:'Asam hidrosianat. Ka = 6.2×10⁻¹⁰. Sangat beracun.' },
  HCOOH:      { name:'HCOOH 0.1 M',    ph:2.4,  type:'asam',   strong:false, formula:'HCOOH ⇌ H⁺ + HCOO⁻',          desc:'Asam format (asam semut). Ka = 1.77×10⁻⁴.' },
  H2C2O4:     { name:'H₂C₂O₄ 0.1 M',  ph:1.3,  type:'asam',   strong:false, formula:'H₂C₂O₄ ⇌ HC₂O₄⁻ + H⁺',       desc:'Asam oksalat diprotik. Ka₁ = 5.6×10⁻². Ada dalam bayam.' },
  C6H5COOH:   { name:'C₆H₅COOH 0.1 M',ph:2.9,  type:'asam',   strong:false, formula:'C₆H₅COOH ⇌ C₆H₅COO⁻ + H⁺',   desc:'Asam benzoat. Ka = 6.5×10⁻⁵. Pengawet makanan E210.' },
  H2S:        { name:'H₂S 0.1 M',      ph:4.0,  type:'asam',   strong:false, formula:'H₂S ⇌ H⁺ + HS⁻',              desc:'Asam sulfida. Ka₁ = 9.5×10⁻⁸. Bau telur busuk.' },
  HNO2:       { name:'HNO₂ 0.1 M',     ph:2.2,  type:'asam',   strong:false, formula:'HNO₂ ⇌ H⁺ + NO₂⁻',            desc:'Asam nitrit. Ka = 4.5×10⁻⁴. Lebih lemah dari HNO₃.' },
  H3BO3:      { name:'H₃BO₃ 0.1 M',    ph:5.1,  type:'asam',   strong:false, formula:'H₃BO₃ + H₂O ⇌ B(OH)₄⁻ + H⁺', desc:'Asam borat. Ka = 5.8×10⁻¹⁰. Digunakan antiseptik.' },
  lactic:     { name:'Asam Laktat 0.1 M',ph:2.4, type:'asam',  strong:false, formula:'CH₃CH(OH)COOH ⇌ CH₃CH(OH)COO⁻ + H⁺', desc:'Ka = 1.4×10⁻⁴. Terbentuk dalam otot saat olahraga.' },
  citric:     { name:'Asam Sitrat 0.1 M',ph:2.1, type:'asam',  strong:false, formula:'C₆H₈O₇ ⇌ C₆H₇O₇⁻ + H⁺',      desc:'Asam triprotik. Ka₁ = 7.4×10⁻⁴. Ada di buah jeruk.' },
  ascorbic:   { name:'Asam Askorbat 0.1 M',ph:3.0,type:'asam', strong:false, formula:'C₆H₈O₆ ⇌ C₆H₇O₆⁻ + H⁺',      desc:'Vitamin C. Ka = 8×10⁻⁵. Antioksidan penting.' },

  // === NETRAL ===
  H2O:        { name:'H₂O',             ph:7,    type:'netral', strong:false, formula:'H₂O ⇌ H⁺ + OH⁻',              desc:'Air murni. [H⁺]=[OH⁻]=10⁻⁷ M, Kw = 10⁻¹⁴ pada 25°C.' },
  NaCl:       { name:'NaCl 0.1 M',       ph:7,    type:'netral', strong:false, formula:'NaCl → Na⁺ + Cl⁻',              desc:'Garam dari asam kuat & basa kuat. Tidak terhidrolisis.' },
  KNO3:       { name:'KNO₃ 0.1 M',      ph:7,    type:'netral', strong:false, formula:'KNO₃ → K⁺ + NO₃⁻',            desc:'Garam netral. Digunakan sebagai pupuk dan bahan peledak.' },
  Na2SO4:     { name:'Na₂SO₄ 0.1 M',    ph:7,    type:'netral', strong:false, formula:'Na₂SO₄ → 2Na⁺ + SO₄²⁻',       desc:'Garam netral dari NaOH dan H₂SO₄.' },
  glukosa:    { name:'Glukosa 0.1 M',    ph:7,    type:'netral', strong:false, formula:'C₆H₁₂O₆ (tidak terionisasi)',  desc:'Senyawa organik non-elektrolit. Tidak mengubah pH.' },

  // === GARAM TERHIDROLISIS (ASAM) ===
  NH4Cl:      { name:'NH₄Cl 0.1 M',     ph:5.1,  type:'asam',   strong:false, formula:'NH₄⁺ + H₂O ⇌ NH₃ + H₃O⁺',    desc:'Hidrolisis parsial kation NH₄⁺. Larutan bersifat asam.' },
  AlCl3:      { name:'AlCl₃ 0.1 M',     ph:3.0,  type:'asam',   strong:false, formula:'Al³⁺ + 3H₂O ⇌ Al(OH)₃ + 3H⁺',desc:'Ion Al³⁺ menghidrolisis kuat. pH cukup rendah.' },
  FeCl3:      { name:'FeCl₃ 0.1 M',     ph:3.1,  type:'asam',   strong:false, formula:'Fe³⁺ + 3H₂O ⇌ Fe(OH)₃ + 3H⁺',desc:'Hidrolisis Fe³⁺ menghasilkan larutan asam.' },
  CuSO4:      { name:'CuSO₄ 0.1 M',     ph:3.9,  type:'asam',   strong:false, formula:'Cu²⁺ + 2H₂O ⇌ Cu(OH)₂ + 2H⁺',desc:'Ion Cu²⁺ terhidrolisis. Larutan berwarna biru, bersifat asam.' },
  ZnSO4:      { name:'ZnSO₄ 0.1 M',     ph:4.4,  type:'asam',   strong:false, formula:'Zn²⁺ + 2H₂O ⇌ Zn(OH)₂ + 2H⁺',desc:'Hidrolisis Zn²⁺ menghasilkan larutan sedikit asam.' },

  // === GARAM TERHIDROLISIS (BASA) ===
  Na2CO3:     { name:'Na₂CO₃ 0.1 M',    ph:11.6, type:'basa',   strong:false, formula:'CO₃²⁻ + H₂O ⇌ HCO₃⁻ + OH⁻',  desc:'Hidrolisis anion CO₃²⁻. Larutan basa kuat (soda cuci).' },
  Na3PO4:     { name:'Na₃PO₄ 0.1 M',    ph:12.0, type:'basa',   strong:false, formula:'PO₄³⁻ + H₂O ⇌ HPO₄²⁻ + OH⁻', desc:'Hidrolisis PO₄³⁻ menghasilkan larutan sangat basa.' },
  CH3COONa:   { name:'CH₃COONa 0.1 M',  ph:8.9,  type:'basa',   strong:false, formula:'CH₃COO⁻ + H₂O ⇌ CH₃COOH + OH⁻',desc:'Natrium asetat. Hidrolisis anion asetat, basa lemah.' },
  NaHCO3:     { name:'NaHCO₃ 0.1 M',    ph:8.3,  type:'basa',   strong:false, formula:'HCO₃⁻ + H₂O ⇌ H₂CO₃ + OH⁻',  desc:'Soda kue. Sedikit basa karena hidrolisis HCO₃⁻.' },
  Na2S:       { name:'Na₂S 0.1 M',       ph:12.5, type:'basa',   strong:false, formula:'S²⁻ + H₂O ⇌ HS⁻ + OH⁻',       desc:'Hidrolisis S²⁻ sangat kuat, larutan sangat basa.' },
  NaCN:       { name:'NaCN 0.1 M',       ph:11.1, type:'basa',   strong:false, formula:'CN⁻ + H₂O ⇌ HCN + OH⁻',        desc:'Natrium sianida. Hidrolisis CN⁻, larutan basa. Sangat toksik.' },

  // === BASA LEMAH ===
  NH3_01:     { name:'NH₃ 0.1 M',        ph:11.1, type:'basa',   strong:false, formula:'NH₃ + H₂O ⇌ NH₄⁺ + OH⁻',      desc:'Basa lemah. Kb = 1.8×10⁻⁵. Terionisasi sebagian.' },
  NH3_1:      { name:'NH₃ 1 M',          ph:11.6, type:'basa',   strong:false, formula:'NH₃ + H₂O ⇌ NH₄⁺ + OH⁻',      desc:'Amonia pekat. Berbau tajam, larutan basa lemah.' },
  N2H4:       { name:'N₂H₄ 0.1 M',       ph:10.6, type:'basa',   strong:false, formula:'N₂H₄ + H₂O ⇌ N₂H₅⁺ + OH⁻',   desc:'Hidrazin. Kb = 9.8×10⁻⁷. Bahan bakar roket.' },
  C6H5NH2:    { name:'C₆H₅NH₂ 0.1 M',   ph:8.8,  type:'basa',   strong:false, formula:'C₆H₅NH₂ + H₂O ⇌ C₆H₅NH₃⁺ + OH⁻', desc:'Anilin. Basa sangat lemah, Kb = 4.3×10⁻¹⁰.' },
  CH3NH2:     { name:'CH₃NH₂ 0.1 M',     ph:11.8, type:'basa',   strong:false, formula:'CH₃NH₂ + H₂O ⇌ CH₃NH₃⁺ + OH⁻',desc:'Metilamina. Kb = 4.4×10⁻⁴. Basa lebih kuat dari NH₃.' },
  pyridine:   { name:'C₅H₅N 0.1 M',      ph:9.0,  type:'basa',   strong:false, formula:'C₅H₅N + H₂O ⇌ C₅H₅NH⁺ + OH⁻',desc:'Piridin. Kb = 1.9×10⁻⁹. Basa lemah, pelarut organik.' },

  // === BASA KUAT ===
  NaOH_001:   { name:'NaOH 0.01 M',      ph:12,   type:'basa',   strong:true,  formula:'NaOH → Na⁺ + OH⁻',              desc:'Basa kuat encer. pH = 14 + log[NaOH].' },
  NaOH_01:    { name:'NaOH 0.1 M',       ph:13,   type:'basa',   strong:true,  formula:'NaOH → Na⁺ + OH⁻',              desc:'Basa kuat umum di laboratorium. Kaustik, korosif.' },
  NaOH_1:     { name:'NaOH 1 M',         ph:14,   type:'basa',   strong:true,  formula:'NaOH → Na⁺ + OH⁻',              desc:'Basa kuat pekat. Sangat korosif, merusak jaringan.' },
  KOH_01:     { name:'KOH 0.1 M',        ph:13,   type:'basa',   strong:true,  formula:'KOH → K⁺ + OH⁻',              desc:'Kalium hidroksida. Basa kuat, digunakan dalam sabun cair.' },
  KOH_1:      { name:'KOH 1 M',          ph:14,   type:'basa',   strong:true,  formula:'KOH → K⁺ + OH⁻',              desc:'Kalium hidroksida pekat. Lebih larut dari NaOH.' },
  Ca_OH_2:    { name:'Ca(OH)₂ 0.1 M',   ph:12.3, type:'basa',   strong:true,  formula:'Ca(OH)₂ → Ca²⁺ + 2OH⁻',        desc:'Air kapur. Basa kuat diprotik, kelarutan terbatas.' },
  Ba_OH_2:    { name:'Ba(OH)₂ 0.1 M',   ph:13.0, type:'basa',   strong:true,  formula:'Ba(OH)₂ → Ba²⁺ + 2OH⁻',        desc:'Barium hidroksida. Basa kuat diprotik, lebih larut dari Ca(OH)₂.' },
  LiOH:       { name:'LiOH 0.1 M',       ph:13,   type:'basa',   strong:true,  formula:'LiOH → Li⁺ + OH⁻',              desc:'Litium hidroksida. Basa kuat, digunakan dalam baterai.' },
  Mg_OH_2:    { name:'Mg(OH)₂ 0.01 M',  ph:10.5, type:'basa',   strong:true,  formula:'Mg(OH)₂ → Mg²⁺ + 2OH⁻',        desc:'Susu magnesia. Basa kuat, kelarutan sangat rendah.' },

  // === LARUTAN ALAMI ===
  cuka:       { name:'Cuka Makan',        ph:2.5,  type:'asam',   strong:false, formula:'CH₃COOH ~5% (0.83 M)',          desc:'Cuka dapur mengandung ~5% asam asetat. pH ≈ 2.4–3.4.' },
  jeruk:      { name:'Jus Jeruk',         ph:3.5,  type:'asam',   strong:false, formula:'Asam sitrat + asam askorbat',    desc:'Mengandung asam sitrat dan vitamin C. Segar dan asam.' },
  apel:       { name:'Jus Apel',          ph:3.8,  type:'asam',   strong:false, formula:'Asam malat dominan',              desc:'Asam malat memberikan rasa asam pada apel. pH 3.3–4.0.' },
  tomat:      { name:'Jus Tomat',         ph:4.2,  type:'asam',   strong:false, formula:'Asam sitrat + asam malat',       desc:'Campuran asam organik. Sumber likopen dan vitamin C.' },
  kopi:       { name:'Kopi',              ph:5.0,  type:'asam',   strong:false, formula:'Asam klorogenat + asam asetat',  desc:'Kopi mengandung berbagai asam organik. pH 4.5–5.5.' },
  teh:        { name:'Teh',               ph:5.5,  type:'asam',   strong:false, formula:'Asam tanin + asam galat',        desc:'Sedikit asam karena kandungan tanin. pH 5.0–6.0.' },
  susu:       { name:'Susu Segar',        ph:6.5,  type:'asam',   strong:false, formula:'Asam laktat + kasein',            desc:'Sedikit asam, mendekati netral. pH 6.3–6.8.' },
  air_hujan:  { name:'Air Hujan',         ph:5.6,  type:'asam',   strong:false, formula:'CO₂ + H₂O → H₂CO₃',            desc:'Sedikit asam karena CO₂ atmosfer membentuk H₂CO₃.' },
  air_laut:   { name:'Air Laut',          ph:8.1,  type:'basa',   strong:false, formula:'Buffer karbonat (HCO₃⁻/CO₃²⁻)', desc:'Sedikit basa karena sistem buffer bikarbonat-karbonat.' },
  sabun:      { name:'Larutan Sabun',     ph:9.5,  type:'basa',   strong:false, formula:'RCOO⁻ + H₂O ⇌ RCOOH + OH⁻',   desc:'Sabun adalah garam dari asam lemak + basa kuat. Basa lemah.' },
  deterjen:   { name:'Deterjen',          ph:10.5, type:'basa',   strong:false, formula:'Surfaktan + builder basa',       desc:'Deterjen mengandung fosfat/karbonat. Cukup basa.' },
  pemutih:    { name:'Pemutih (Bayclin)',  ph:12,   type:'basa',   strong:false, formula:'NaOCl → Na⁺ + OCl⁻',            desc:'Larutan NaOCl. Basa kuat, oksidator, desinfektan.' },
  lambung:    { name:'Asam Lambung',      ph:2.0,  type:'asam',   strong:true,  formula:'HCl encer (pH 1.5–3.5)',        desc:'Cairan lambung mengandung HCl dan pepsin. Pencernaan protein.' },
  darah:      { name:'Darah Manusia',     ph:7.4,  type:'basa',   strong:false, formula:'Buffer fosfat + buffer bikarbonat', desc:'pH darah dijaga ketat 7.35–7.45. Penyimpangan = asidosis/alkalosis.' },
  saliva:     { name:'Saliva (Air Liur)', ph:6.8,  type:'asam',   strong:false, formula:'Buffer bikarbonat + musin',      desc:'Sedikit asam. pH bervariasi 6.2–7.6 tergantung kondisi.' },
  urin:       { name:'Urin',              ph:6.0,  type:'asam',   strong:false, formula:'NH₄⁺, fosfat, kreatinin',       desc:'Biasanya sedikit asam, pH 4.6–8.0 tergantung diet.' },
};

const indicators = {
  pp: {
    name: 'Fenolftalein (PP)',
    range: 'pH 8.2 – 10.0',
    transitions: [
      { phMax: 8.2,  color: '#f5f5f5', label: 'Tidak berwarna' },
      { phMax: 10.0, color: '#ffb3d9', label: 'Merah muda (transisi)' },
      { phMax: 14,   color: '#e91e8c', label: 'Merah muda – Magenta' },
    ]
  },
  mo: {
    name: 'Metil Jingga (MO)',
    range: 'pH 3.1 – 4.4',
    transitions: [
      { phMax: 3.1,  color: '#ff3d00', label: 'Merah' },
      { phMax: 4.4,  color: '#ff9800', label: 'Oranye (transisi)' },
      { phMax: 14,   color: '#ffd600', label: 'Kuning' },
    ]
  },
  litmus: {
    name: 'Lakmus',
    range: 'pH 4.5 – 8.3',
    transitions: [
      { phMax: 4.5,  color: '#e53935', label: 'Merah' },
      { phMax: 8.3,  color: '#9c27b0', label: 'Ungu (transisi)' },
      { phMax: 14,   color: '#1565c0', label: 'Biru' },
    ]
  },
  mr: {
    name: 'Metil Merah (MR)',
    range: 'pH 4.4 – 6.2',
    transitions: [
      { phMax: 4.4,  color: '#e53935', label: 'Merah' },
      { phMax: 6.2,  color: '#ff7043', label: 'Oranye-Merah (transisi)' },
      { phMax: 14,   color: '#ffeb3b', label: 'Kuning' },
    ]
  },
  btb: {
    name: 'Bromtimol Biru (BTB)',
    range: 'pH 6.0 – 7.6',
    transitions: [
      { phMax: 6.0,  color: '#f9a825', label: 'Kuning' },
      { phMax: 7.6,  color: '#66bb6a', label: 'Hijau (transisi)' },
      { phMax: 14,   color: '#1565c0', label: 'Biru' },
    ]
  },
  universal: {
    name: 'Indikator Universal',
    range: 'pH 0 – 14',
    transitions: [
      { phMax: 1,  color: '#d32f2f', label: 'Merah tua' },
      { phMax: 3,  color: '#f44336', label: 'Merah' },
      { phMax: 5,  color: '#ff7043', label: 'Oranye' },
      { phMax: 6,  color: '#ffa726', label: 'Oranye-Kuning' },
      { phMax: 7,  color: '#aed581', label: 'Kuning-Hijau' },
      { phMax: 8,  color: '#66bb6a', label: 'Hijau' },
      { phMax: 9,  color: '#26a69a', label: 'Hijau Kebiruan' },
      { phMax: 10, color: '#42a5f5', label: 'Biru Muda' },
      { phMax: 11, color: '#1e88e5', label: 'Biru' },
      { phMax: 12, color: '#5c6bc0', label: 'Biru-Ungu' },
      { phMax: 14, color: '#7b1fa2', label: 'Ungu' },
    ]
  }
};

function getColor(indicatorKey, ph) {
  const ind = indicators[indicatorKey];
  for (const t of ind.transitions) {
    if (ph <= t.phMax) return { color: t.color, label: t.label };
  }
  return ind.transitions[ind.transitions.length - 1];
}

function updateSolutionInfo() {
  const key = document.getElementById('sol').value;
  const info = document.getElementById('sol-info');
  if (!key || !solutions[key]) {
    info.textContent = 'Pilih larutan untuk melihat informasi.';
    return;
  }
  const s = solutions[key];
  info.innerHTML = `<strong style="color:var(--text)">${s.formula}</strong><br>${s.desc}`;
}

function simulate() {
  const solKey = document.getElementById('sol').value;
  const indKey = document.getElementById('ind').value;

  if (!solKey || !indKey) {
    alert('Pilih larutan dan indikator terlebih dahulu.');
    return;
  }

  const sol = solutions[solKey];
  const ph = sol.ph;
  const type = sol.type;

  // which indicators to show
  const indKeys = indKey === 'all' ? Object.keys(indicators) : [indKey];

  // hide placeholder, show result
  document.getElementById('placeholder').style.display = 'none';
  const rc = document.getElementById('result-content');
  rc.style.display = 'flex';
  rc.innerHTML = '';
  rc.className = 'animate-in';
  rc.style.flexDirection = 'column';
  rc.style.gap = '1.4rem';

  // colors
  const typeColor = type === 'asam' ? '#ff6b6b' : type === 'basa' ? '#60a5fa' : '#a3e635';
  const typeLabel = type === 'asam' ? 'ASAM' : type === 'basa' ? 'BASA' : 'NETRAL';
  const strengthLabel = sol.strong ? (type === 'asam' ? 'Asam Kuat' : 'Basa Kuat') : (type === 'netral' ? 'Netral' : type === 'asam' ? 'Asam Lemah' : 'Basa Lemah');

  // ---- pH section ----
  const phSec = document.createElement('div');
  phSec.innerHTML = `
    <div class="ph-label">// Hasil pH & Sifat</div>
    <div class="ph-display">
      <div class="ph-value" style="color:${typeColor}">${ph.toFixed(1)}</div>
      <div class="ph-nature">
        <span class="nature-badge" style="border-color:${typeColor}; color:${typeColor}">${typeLabel}</span>
        <span style="font-size:0.78rem; color:var(--muted); margin-top:2px">${strengthLabel}</span>
        <span class="ph-formula">${sol.formula}</span>
      </div>
    </div>
    <div class="ph-bar-wrap">
      <div class="ph-cursor" id="ph-cursor" style="left:0%"></div>
    </div>
    <div class="ph-bar-labels">
      <span>0</span><span>2</span><span>4</span><span>6</span><span>7</span><span>8</span><span>10</span><span>12</span><span>14</span>
    </div>`;
  rc.appendChild(phSec);

  // animate cursor
  setTimeout(() => {
    document.getElementById('ph-cursor').style.left = `${(ph / 14) * 100}%`;
  }, 50);

  // ---- Beaker visual section ----
  const beakerSec = document.createElement('div');
  beakerSec.className = 'beaker-section';
  beakerSec.innerHTML = `<div class="beaker-label">// Visualisasi Warna Larutan</div>`;

  const beakerContainer = document.createElement('div');
  beakerContainer.className = 'beaker-container';

  indKeys.forEach(ik => {
    const colorData = getColor(ik, ph);
    const item = document.createElement('div');
    item.className = 'beaker-item';

    item.innerHTML = `
      <svg class="beaker-svg" width="70" height="100" viewBox="0 0 70 100">
        <!-- beaker outline -->
        <path d="M10,10 L10,80 Q10,92 22,92 L48,92 Q60,92 60,80 L60,10 Z" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="2"/>
        <!-- liquid -->
        <clipPath id="clip-${ik}">
          <path d="M11,38 L11,80 Q11,90 22,90 L48,90 Q59,90 59,80 L59,38 Z"/>
        </clipPath>
        <rect x="11" y="36" width="48" height="56" clip-path="url(#clip-${ik})" fill="${colorData.color}" opacity="0.88" class="liquid"/>
        <!-- bubbles in liquid -->
        <circle class="bubble" cx="25" cy="70" r="3" fill="rgba(255,255,255,0.2)"/>
        <circle class="bubble" cx="38" cy="78" r="2" fill="rgba(255,255,255,0.15)"/>
        <circle class="bubble" cx="48" cy="65" r="2.5" fill="rgba(255,255,255,0.18)"/>
        <!-- glass sheen -->
        <path d="M15,12 L15,80" stroke="rgba(255,255,255,0.08)" stroke-width="3" stroke-linecap="round"/>
        <!-- beaker lip -->
        <path d="M6,10 L64,10" stroke="rgba(255,255,255,0.25)" stroke-width="2.5" stroke-linecap="round"/>
        <!-- measurement lines -->
        <line x1="12" y1="55" x2="18" y2="55" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
        <line x1="12" y1="65" x2="18" y2="65" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
        <line x1="12" y1="75" x2="18" y2="75" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
      </svg>
      <div class="beaker-name">${indicators[ik].name.split(' ')[0]}</div>
      <div style="font-size:0.7rem; color:${colorData.color}; font-family:'Space Mono',monospace; text-align:center; max-width:70px;">${colorData.label}</div>`;

    beakerContainer.appendChild(item);
  });

  beakerSec.appendChild(beakerContainer);
  rc.appendChild(beakerSec);

  // ---- Indicator result table ----
  const indSec = document.createElement('div');
  indSec.innerHTML = `<div class="ph-label">// Detail Indikator</div>`;
  const indRows = document.createElement('div');
  indRows.className = 'indicator-results';

  indKeys.forEach(ik => {
    const ind = indicators[ik];
    const colorData = getColor(ik, ph);
    const row = document.createElement('div');
    row.className = 'ind-row active animate-in';
    row.innerHTML = `
      <div>
        <div class="ind-name">${ind.name}</div>
        <div class="ind-range">Trayek: ${ind.range}</div>
      </div>
      <div class="ind-color-display">
        <div class="swatch" style="background:${colorData.color}"></div>
        <span style="color:${colorData.color}; font-weight:500">${colorData.label}</span>
      </div>`;
    indRows.appendChild(row);
  });

  indSec.appendChild(indRows);
  rc.appendChild(indSec);
}
</script>
</body>
</html>
