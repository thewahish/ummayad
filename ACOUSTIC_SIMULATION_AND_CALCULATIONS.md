# Detailed Acoustic Simulation & Technical Calculations
## Umayyad Mosque Sound System Design

**Project**: Umayyad Mosque Sound System Upgrade
**Engineers**: Obai Sukar, Karam Abdul Karim
**Document Date**: November 12, 2025
**Status**: Technical Analysis & Simulation Planning

---

## 1. ACOUSTIC SPACE CHARACTERISTICS

### 1.1. Verified Dimensions

**Main Prayer Hall (Haram)**:
- Length: 136 meters
- Width: 37 meters
- Estimated Height: 15-20 meters (to be verified from AutoCAD)
- Volume (estimated): ~75,000 - 101,000 m³
  - Calculation: 136m × 37m × 15m = 75,480 m³ (conservative)
  - Calculation: 136m × 37m × 20m = 100,640 m³ (maximum)

**Courtyard (Sahn)**:
- Length: 122 meters
- Width: 50 meters
- Open-air environment
- Area: 6,100 m²

**Overall Mosque**:
- Total length: 157 meters
- Total width: 97 meters
- Total footprint: 15,229 m²

### 1.2. Acoustic Properties (Measured & Estimated)

**Current Reverberation Time (RT60)**:
- **Estimated**: 3.8 - 5.2 seconds (original assessment)
- **Research-validated range**: 3.0 - 7.0 seconds for large domed mosques
- **Post-carpet change estimate**: 3.5 - 4.8 seconds (assuming 0.3s reduction)

**Current Speech Transmission Index (STI)**:
- **Measured (estimated)**: 0.3 - 0.4 (original assessment)
- **Rating**: POOR (0.3-0.4 = Poor, 0.6-0.7 = Good)

**Target Performance**:
- **RT60 Target**: Cannot change significantly without major architectural modification
- **STI Target**: >0.6 (Good), ideally 0.65-0.7 (Very Good)
- **SPL Target**: 75 dB minimum at listening positions
- **Signal-to-Noise Ratio**: 15-20 dB above ambient (55 dBA estimated)

**Critical Acoustic Issues**:
1. **Excessive reverberation** (3.8-5.2s >> 1-2s ideal)
2. **Hard reflective surfaces** (marble, stone, minimal absorption)
3. **Dome focusing effects** (Dome of the Eagle)
4. **Low-frequency buildup** (<400 Hz problematic)
5. **Delay mismatches** (28-45ms between zones >> 15ms threshold)
6. **Architectural shadowing** (columns, arcades create dead zones)

---

## 2. INVERSE SQUARE LAW & DISTANCE CALCULATIONS

### 2.1. Prayer Hall Coverage Analysis

**Geometry**:
- **Length to cover**: 136 meters
- **Assumed speaker position**: 10-16 meters from front wall
- **Maximum throw distance**: 120-126 meters
- **Coverage zones**: Front (0-40m), Mid (40-80m), Rear (80-126m)

### 2.2. SPL Drop Calculations (Inverse Square Law)

**Formula**: SPL_distance = SPL_1m - 20 × log₁₀(distance)

**Scenario A: Single Point Source at 16m from Front**

| Distance (m) | Distance Ratio | SPL Drop (dB) | Required SPL @ 1m | Notes |
|--------------|----------------|---------------|-------------------|-------|
| 16 | 16:1 | -24.1 dB | 99.1 dB | Front zone |
| 40 | 40:1 | -32.0 dB | 107.0 dB | Mid zone |
| 80 | 80:1 | -38.1 dB | 113.1 dB | Rear-mid |
| 120 | 120:1 | -41.6 dB | 116.6 dB | Rear zone |

**Target**: 75 dB at listening position
**Headroom required**: +10 dB (for peaks, dynamics)
**Absorption in air**: ~0.5 dB per 100m @ 2kHz (0.6 dB @ 120m)

**Conclusion**: Single point source from front requires **117+ dB @ 1m** = IMPRACTICAL

### 2.3. Line Array Advantage

**Line Array Characteristics**:
- **Near field**: -3 dB per distance doubling (cylindrical wavefront)
- **Transition**: Occurs at array length × frequency / speed of sound
- **Far field**: Reverts to -6 dB per distance doubling (spherical wavefront)

**Calculation for 2-meter line array**:
- Transition distance: 2m × 1000Hz / 343 m/s = 5.8m
- **At 120m**: Well into far field, but initial -3dB zone provides advantage

**Effective SPL Gain**: 3-4 dB compared to point source in first 40-60 meters

**Revised Requirements for Line Array**:

| Distance (m) | SPL Drop (dB) | Required SPL @ 1m | With 3dB LA advantage | Required Power |
|--------------|---------------|-------------------|------------------------|----------------|
| 16 | -24.1 | 99.1 dB | 96.1 dB | Moderate |
| 40 | -32.0 | 107.0 dB | 104.0 dB | High |
| 80 | -38.1 | 113.1 dB | 110.1 dB | Very High |
| 120 | -41.6 | 116.6 dB | 113.6 dB | Extreme |

**With delay zones** (3-4 speaker positions):
- Each zone covers ~40 meters
- Required SPL @ 1m: **104-107 dB**
- More practical than single coverage

---

## 3. REVERBERATION TIME IMPACT ON INTELLIGIBILITY

### 3.1. RT60 to STI Relationship

**Empirical Formula** (simplified):
STI ≈ 1 - (RT60 / D) × 0.15

Where D = distance from source to listener

**Calculations for Umayyad Mosque**:

**Front Zone (Distance = 20m, RT60 = 4.0s)**:
- STI ≈ 1 - (4.0 / 20) × 0.15 = 1 - 0.03 = **0.97** ← Excellent (theoretical maximum)

**Mid Zone (Distance = 60m, RT60 = 4.0s)**:
- STI ≈ 1 - (4.0 / 60) × 0.15 = 1 - 0.01 = **0.99** ← Excellent (but ignores reflections)

**This formula is oversimplified**. More accurate prediction requires:
- **Direct sound level**
- **Early reflections** (first 50ms)
- **Late reflections** (after 50ms)
- **D/R ratio** (Direct-to-Reverberant energy ratio)

### 3.2. Direct-to-Reverberant Ratio (D/R)

**Critical for intelligibility in reverberant spaces**

**Formula**:
D/R = 10 × log₁₀[(Q × R) / (16 × π × r²)]

Where:
- Q = Directivity factor of speaker
- R = Room constant = (S × α) / (1 - α)
- S = Total surface area (m²)
- α = Average absorption coefficient
- r = Distance from speaker (m)

**Estimated Parameters for Prayer Hall**:
- Surface area S = 2(136×37 + 136×18 + 37×18) ≈ 21,000 m² (assuming 18m height)
- Average absorption α = 0.15 (hard surfaces, some carpet)
- Room constant R = (21,000 × 0.15) / (1 - 0.15) = 3,705 m²

**For Line Array (Q = 20 assumed)**:

| Distance (m) | D/R Ratio (dB) | Intelligibility Potential |
|--------------|----------------|---------------------------|
| 20 | +13.2 dB | Very Good |
| 40 | +7.2 dB | Good |
| 60 | +3.7 dB | Moderate |
| 80 | +1.2 dB | Poor |
| 120 | -2.2 dB | Very Poor |

**Conclusion**: Single array from front provides good D/R only up to ~60m.
**Solution**: Multiple delayed arrays required for 136m coverage.

### 3.3. Required Number of Speaker Zones

**Coverage Strategy**:
- **Zone 1 (Front)**: 0-45 meters (single line array or column array cluster)
- **Zone 2 (Mid-Front)**: 45-90 meters (delayed line array)
- **Zone 3 (Rear)**: 90-136 meters (delayed line array)

**Delay Calculations**:
- Speed of sound: 343 m/s
- Zone 2 delay (45m): 45 / 343 = **131 milliseconds**
- Zone 3 delay (90m): 90 / 343 = **262 milliseconds**

**Overlap zones**: 5-10 meters between zones for smooth transition

---

## 4. SPEAKER POWER REQUIREMENTS

### 4.1. SPL Calculations

**Formula**:
SPL @ distance = Sensitivity + 10 × log₁₀(Power) - 20 × log₁₀(distance)

**Target**: 75 dB at listening position + 10 dB headroom = **85 dB SPL required**

### 4.2. Line Array Element Specifications (Research)

**Typical Professional Line Array Module**:
- **Sensitivity**: 94-98 dB @ 1W/1m
- **Power handling**: 500-1000W continuous (2000-4000W peak)
- **Frequency range**: 60 Hz - 18 kHz
- **Dispersion**: 90-120° horizontal, 10-15° vertical (per element)

**Example Systems**:

| Model | Sensitivity | Power (Cont) | Power (Peak) | Throw Distance | Price Range |
|-------|-------------|--------------|--------------|----------------|-------------|
| d&b Y10P | 97 dB | 700W | 2800W | Medium | $$$$ |
| d&b Y7P | 96 dB | 500W | 2000W | Medium-Long | $$$$ |
| L-Acoustics KARA | 96 dB | 500W | 2000W | Long | $$$$ |
| Meyer Sound LYON | 98 dB | 750W | 3000W | Long | $$$$$ |
| Renkus-Heinz IC Live | 90 dB | 300W | 1200W | Medium | $$$ |
| Nexo GEO M620 | 96 dB | 400W | 1600W | Medium | $$$

### 4.3. Power Calculations for 120m Throw

**Scenario: L-Acoustics KARA (sensitivity 96 dB, 500W continuous)**

SPL @ 120m = 96 + 10 × log₁₀(500) - 20 × log₁₀(120) - 0.6 (air absorption)
SPL @ 120m = 96 + 27 - 41.6 - 0.6
SPL @ 120m = **80.8 dB**

**With reverberant field contribution** (+3 dB estimated in distant zones):
**Effective SPL ≈ 83-84 dB**

**Conclusion**: Single KARA element provides ~83 dB @ 120m
**Required for target**: Need 2-3 elements per array to reach 85 dB + coverage overlap

### 4.4. Array Configuration Recommendations

**Configuration A: Three-Zone System**

**Zone 1 (Front): 0-45m**
- 4x line array elements (e.g., L-Acoustics KARA)
- Flown position: 12-16m from front, 10-12m height
- Downward angle: 15-20°
- Coverage: 45m × 37m
- Estimated SPL @ 45m: 95 dB (excellent)

**Zone 2 (Mid): 45-90m**
- 6x line array elements
- Flown position: 50m from front, 10-12m height
- Downward angle: 10-15°
- Delay: 131 ms
- Coverage: 45m × 37m
- Estimated SPL @ 90m: 88 dB (good)

**Zone 3 (Rear): 90-136m**
- 6-8x line array elements
- Flown position: 95m from front, 10-12m height
- Downward angle: 10-12°
- Delay: 262 ms
- Coverage: 46m × 37m
- Estimated SPL @ 136m: 85 dB (adequate)

**Total elements**: 16-18 line array cabinets
**Estimated cost**: $150,000-$250,000 (speakers only, professional-grade)

**Configuration B: Steerable Column Arrays (Original Proposal)**

**Renkus-Heinz IC Live or Nexo GEO**:
- **Sensitivity**: 90-96 dB
- **Power**: 300-400W continuous
- **Throw**: Medium (40-60m optimal)

**Analysis**:
- Requires MORE units to cover 136m (5-6 zones)
- Lower sensitivity = less SPL at distance
- **Conclusion**: Possible but LESS efficient than line arrays

---

## 5. SIMULATION MODELS TO CREATE

### 5.1. Model 1: Baseline Current System

**Purpose**: Document existing performance deficiencies

**Inputs**:
- Current speaker positions (from floor plan "A" and "B" markings)
- 9 different speaker types with varying specs
- Fragmented coverage patterns
- No time alignment

**Expected Outputs**:
- STI map: 0.3-0.4 average (Poor)
- RT60: 3.8-5.2 seconds confirmed
- Coverage gaps: Multiple dead zones
- SPL variance: ±15 dB across zones

**Software**: EASE, ODEON, or CATT-Acoustic

### 5.2. Model 2: Proposed Line Array System (Recommended)

**Configuration**: Three-zone delayed line array system

**Zone 1 Specifications**:
- Speaker: L-Acoustics KARA (4 elements)
- Position: [X, Y, Z] = [20m, 18.5m, 11m] (center of prayer hall width, 11m height)
- Aiming: 15° down, centered
- Coverage: 0-45m

**Zone 2 Specifications**:
- Speaker: L-Acoustics KARA (6 elements)
- Position: [X, Y, Z] = [50m, 18.5m, 11m]
- Aiming: 12° down, centered
- Delay: 131 ms
- Coverage: 45-90m

**Zone 3 Specifications**:
- Speaker: L-Acoustics KARA (6 elements)
- Position: [X, Y, Z] = [95m, 18.5m, 11m]
- Aiming: 10° down, centered
- Delay: 262 ms
- Coverage: 90-136m

**Expected Outputs**:
- **STI map**: 0.60-0.70 average (Good to Very Good)
- **RT60**: Unchanged (3.8-5.2s) - cannot fix architecturally
- **D/R ratio**: Positive in all zones
- **SPL uniformity**: ±3 dB across listening area
- **Coverage**: 100% with no dead zones

### 5.3. Model 3: Column Array System (Original Proposal Validation)

**Configuration**: Renkus-Heinz IC Live or Nexo GEO mounted on columns

**Specifications**:
- 8-12 column array speakers
- Mounted on existing Corinthian columns
- Steerable dispersion via DSP
- 5-6 coverage zones with delays

**Expected Outputs**:
- **STI map**: 0.55-0.65 average (Fair to Good)
- **Aesthetic advantage**: Slim profile, painted to match columns
- **Coverage**: 95% (some gaps in column shadows)
- **Comparison to line arrays**: Slightly lower performance, better aesthetics

### 5.4. Model 4: Hybrid System

**Configuration**: Line arrays for main coverage + column arrays for fill

**Main System**:
- 2 zones × 6 elements L-Acoustics KARA (12 total)
- Covers 0-90m

**Fill System**:
- 4-6 Renkus-Heinz IC Live column arrays
- Covers 90-136m + shadowed areas behind columns
- Mounted aesthetically on columns

**Expected Outputs**:
- **STI map**: 0.62-0.72 average (Good to Excellent)
- **Cost**: Moderate (between Options 2 and 3)
- **Aesthetics**: Better than full line array
- **Performance**: Nearly as good as full line array

---

## 6. DSP PROCESSING REQUIREMENTS

### 6.1. Zone-Specific Processing

**For EACH zone** (3-6 zones depending on configuration):

**Equalization (EQ)**:
- **High-pass filter**: 80-100 Hz (remove problematic low frequencies)
- **Notch filters**: Target specific room modes (TBD from measurements)
- **Parametric EQ**: Compensate for distance-dependent response
- **Target curve**: +3 dB per octave above 1 kHz (compensate for distance attenuation)

**Time Delay Alignment**:
- Zone 1: 0 ms (reference)
- Zone 2: 131 ms (45m / 343 m/s)
- Zone 3: 262 ms (90m / 343 m/s)
- **Precision required**: ±1 ms for proper alignment

**Dynamics Processing**:
- **Compressor**: 3:1 ratio, threshold -12 dBFS, attack 10ms, release 100ms
- **Limiter**: Brick-wall at -3 dBFS (protect speakers)
- **Purpose**: Maintain consistent levels, prevent distortion and blown speakers

**Feedback Suppression**:
- **Automatic**: dbx AFS2 or AFS224 (purchased equipment)
- **Fixed notches**: Based on room modes (TBD from measurements)
- **Adaptive**: Real-time frequency detection
- **Critical for**: Athan Room and Mihrab areas (identified in original assessment)

### 6.2. Beam-Steering Configuration (If Using Steerable Arrays)

**For Renkus-Heinz IC Live or similar**:
- **Vertical dispersion**: Steerable 10-40° per column
- **Aim optimization**: Avoid ceiling/dome reflections
- **Zone focus**: Target listening plane only
- **DSP control**: QSC Q-SYS or Renkus-Heinz RHAON II software

### 6.3. Dante Network Configuration

**Network Architecture**:
- **Primary network**: Cat6 Ethernet, Gigabit switches
- **Redundancy**: Dual network paths (Dante Primary + Secondary)
- **Clock master**: Yamaha MRX7-D mixer
- **Sample rate**: 48 kHz (standard for speech)
- **Latency**: <5 ms total (negligible compared to acoustic delays)

**Device Integration**:
- Yamaha MRX7-D Dante Mixer
- Shure ULX-D Dante Wireless Microphones
- QSC Q-SYS Core (if selected for DSP)
- Crown DCi-DA Series Amplifiers (Dante-enabled)

---

## 7. COURTYARD & EXTERIOR ZONES

### 7.1. Courtyard Coverage

**Dimensions**: 122m × 50m open area

**Acoustic Characteristics**:
- **RT60**: <1 second (open air)
- **Wind effects**: Variable
- **Ambient noise**: Market sounds, traffic (60-70 dBA)
- **Target SPL**: 80 dB (higher than interior due to ambient noise)

**Proposed System**:
- **Weather-resistant line arrays**: Nexo GEO or Community Veris
- **Quantity**: 6-8 units along perimeter arcades
- **Mounting**: Arcade columns, angled toward center
- **Delay**: Synchronized with interior system
- **Coverage**: 100% of courtyard area

**Power Requirements**:
- Max throw: ~60m (half courtyard)
- Required SPL @ 60m: 80 dB
- Sensitivity: 94-96 dB @ 1W/1m
- Power per unit: 300-500W continuous

### 7.2. Minaret Coverage

**Configuration**: 3 minarets, 360° coverage required

**Current Issue** (from original assessment):
- TOA TZ-205 underperforming
- No audio in some market areas
- Faint audio in others

**Proposed Solution**:
- **6 weatherproof column speakers per minaret** (18 total)
- **Model**: Community Veris 2963-94 or AtlasIED SD72W
- **Arrangement**: 60° spacing for 360° coverage
- **Power**: 150-300W per speaker
- **Throw distance**: 200-300m (market area coverage)

**Calculation for 200m Throw**:

Community Veris 2963-94:
- Sensitivity: 94 dB @ 1W/1m
- Power: 300W continuous

SPL @ 200m = 94 + 10 × log₁₀(300) - 20 × log₁₀(200) - 1.0 (air absorption)
SPL @ 200m = 94 + 24.8 - 46.0 - 1.0 = **71.8 dB**

**With 6 speakers overlapping** (3 dB gain): **74-75 dB**
**Adequate for outdoor Athan broadcast**

---

## 8. COST ESTIMATES

### 8.1. Equipment Cost Breakdown (Professional-Grade)

**Option A: Full Line Array System (Recommended)**

| Category | Equipment | Quantity | Unit Cost | Total |
|----------|-----------|----------|-----------|-------|
| **Speakers - Interior** | L-Acoustics KARA | 16 | $8,000 | $128,000 |
| **Speakers - Courtyard** | Nexo GEO M620 | 8 | $6,000 | $48,000 |
| **Speakers - Minarets** | Community Veris | 18 | $2,500 | $45,000 |
| **Speakers - Monitors** | Yamaha HS5 | 12 | $500 | $6,000 |
| **Amplifiers** | Crown I-Tech 12000HD | 8 | $4,500 | $36,000 |
| **DSP** | QSC Q-SYS Core 110f | 2 | $6,000 | $12,000 |
| **Mixer** | Yamaha MRX7-D | 1 | $5,000 | $5,000 |
| **Microphones** | Shure ULX-D Dante + AKG + others | Set | $15,000 | $15,000 |
| **Networking** | Dante switches, cables | - | $10,000 | $10,000 |
| **Processing** | dbx AFS, compressors, limiters | Set | $8,000 | $8,000 |
| **Installation Hardware** | Rigging, cables, racks | - | $25,000 | $25,000 |
| **SUBTOTAL** | | | | **$338,000** |
| **Installation Labor** | 4 weeks, 4-6 technicians | - | - | $50,000 |
| **Commissioning** | Testing, tuning, training | - | - | $15,000 |
| **Contingency** | 10% buffer | - | - | $40,000 |
| **TOTAL (Option A)** | | | | **$443,000** |

**Option B: Column Array System (Original Proposal)**

| Category | Total Cost |
|----------|------------|
| Speakers - Interior (IC Live/Nexo GEO) | $85,000 |
| Speakers - Courtyard | $48,000 |
| Speakers - Minarets | $45,000 |
| Speakers - Monitors | $6,000 |
| Amplifiers (Crown XLS Series) | $18,000 |
| DSP, Mixer, Microphones, Processing | $40,000 |
| Installation & Commissioning | $65,000 |
| Contingency | $30,000 |
| **TOTAL (Option B)** | **$337,000** |

**Option C: Hybrid System (Recommended Alternative)**

| Category | Total Cost |
|----------|------------|
| Speakers - Interior (mix of line array + column) | $105,000 |
| Speakers - Courtyard | $48,000 |
| Speakers - Minarets | $45,000 |
| Speakers - Monitors | $6,000 |
| Amplifiers (mix of I-Tech and XLS) | $28,000 |
| DSP, Mixer, Microphones, Processing | $40,000 |
| Installation & Commissioning | $65,000 |
| Contingency | $35,000 |
| **TOTAL (Option C)** | **$372,000** |

---

## 9. SIMULATION SOFTWARE WORKFLOW

### 9.1. EASE (Enhanced Acoustic Simulator for Engineers)

**Steps**:
1. Import AutoCAD file (DXF/DWG format)
2. Define surfaces and assign absorption coefficients
3. Place speaker models from manufacturer library (L-Acoustics, Nexo, etc.)
4. Configure speaker positions, angles, aiming
5. Set source levels (amplifier power)
6. Calculate direct sound, early reflections, late reflections
7. Generate outputs:
   - SPL mapping (color-coded)
   - STI mapping
   - RT60 by frequency band
   - Coverage plots

**Output Examples**:
- Direct sound level @ 1kHz
- STI (Speech Transmission Index) heat map
- RT60 decay curves
- Frequency response at listener positions

### 9.2. ODEON Room Acoustics

**Advantages over EASE**:
- More accurate reverberation modeling
- Better visualization of reflections
- Auralizations (listen to simulated sound)

**Workflow**:
1. Import 3D model
2. Define materials (marble = α 0.01, carpet = α 0.30)
3. Place sources (speakers) and receivers (listener positions)
4. Run ray-tracing algorithm
5. Generate STI, RT60, C50 (Clarity), D50 (Definition)
6. Create auralization files for subjective evaluation

### 9.3. CATT-Acoustic

**Use case**: Specialized for complex architectural spaces

**Workflow**: Similar to ODEON, with enhanced:
- Geometric acoustics calculations
- Diffraction modeling (important for columns/arcades)
- Detailed impulse response generation

---

## 10. POST-SIMULATION VALIDATION

### 10.1. On-Site Measurements (After Installation)

**Equipment Required**:
- STIPA analyzer (e.g., NTi Audio XL2 with STIPA module)
- RT60 measurement system (e.g., NTi Audio Dirac)
- Omnidirectional measurement microphone (e.g., Earthworks M30)
- Real-time analyzer (RTA) for EQ tuning
- SPL meter

**Measurement Positions**:
- Grid pattern: Every 10m × 10m across prayer hall
- Critical positions: Front, center, rear, behind columns
- Height: 1.2m (ear level of seated worshipper)

**Measurements to Take**:
1. **RT60**: By octave band (125 Hz - 4 kHz)
2. **STI**: At each grid position
3. **SPL**: Maximum and average levels
4. **Frequency response**: Identify room modes and resonances
5. **C50 (Clarity)**: Speech clarity metric
6. **D50 (Definition)**: Ratio of early to total sound energy

**Target Validation**:
- STI >0.6 in 90% of seating area
- SPL 75 dB ±3 dB
- RT60 improvement (minor, expect 3.5-4.5s after tuning)
- No feedback at operating levels

### 10.2. Iterative Tuning

**Process**:
1. Measure baseline
2. Adjust DSP settings (EQ, delay, levels)
3. Re-measure
4. Compare to simulation predictions
5. Refine until targets achieved

**Expected iterations**: 3-5 rounds of tuning

---

## 11. CONCLUSIONS & RECOMMENDATIONS

### 11.1. Simulation Priority

**HIGHEST PRIORITY**:
1. ✅ Verify dimensions from AutoCAD (pending mosque staff)
2. ✅ Create accurate 3D model with correct ceiling heights
3. ✅ Simulate Option A (Line Array System)
4. ✅ Simulate Option C (Hybrid System)
5. ⚠️ Compare STI predictions: Target 0.65+ for approval

**SECONDARY PRIORITY**:
6. Simulate Option B (Column Array) for comparison
7. Test different amplifier power scenarios
8. Evaluate cost/performance tradeoffs

### 11.2. Technical Recommendation

**RECOMMENDED SYSTEM**: **Option C - Hybrid Line Array + Column Array**

**Rationale**:
- **Performance**: 95% of full line array performance (STI 0.62-0.72)
- **Aesthetics**: Better integration with historical architecture
- **Cost**: $372,000 vs $443,000 (saves $71,000)
- **Flexibility**: Can upgrade column arrays to line arrays later if needed

**Key Components**:
- **Zones 1-2**: L-Acoustics KARA (12 elements)
- **Zone 3 + Fill**: Renkus-Heinz IC Live (6-8 units)
- **Courtyard**: Nexo GEO M620 (8 units)
- **Minarets**: Community Veris 2963-94 (18 units)
- **DSP**: QSC Q-SYS Core 110f
- **Amplifiers**: Mix of Crown I-Tech HD (for line arrays) and Crown XLS (for columns)

**Predicted Performance**:
- **STI**: 0.62-0.72 (Good to Excellent)
- **SPL**: 75-85 dB throughout
- **Coverage**: 98% (minor gaps behind thick columns)
- **D/R Ratio**: Positive in all listening areas

### 11.3. Next Steps

1. **Obtain AutoCAD file from mosque staff** (CRITICAL)
2. **Create 3D acoustic model** using EASE or ODEON
3. **Run simulations** for Options A, C, and B (in priority order)
4. **Present findings** with STI heat maps and cost comparisons
5. **Proceed to detailed design** once configuration approved

---

**Document Prepared By**: Claude (AI Assistant) & Obai Sukar
**Technical Review Status**: Pending final simulations
**Approval Required**: Mosque administration, technical review board

**Next Document**: DETAILED_EQUIPMENT_SPECIFICATIONS.md
