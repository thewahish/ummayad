# Acoustic Simulation Specification - Umayyad Mosque Sound System
**Project**: Umayyad Mosque Sound System Assessment & Redesign
**Engineer**: Obai Sukar
**Purpose**: Define comprehensive acoustic simulation requirements for scientifically accurate system design

---

## SIMULATION REQUIREMENTS

### Software Platforms Required
1. **EASE (Enhanced Acoustic Simulator for Engineers)**
   - Industry standard for large-scale venue modeling
   - Ray-tracing for RT60 prediction
   - SPL mapping and coverage analysis

2. **ODEON Room Acoustics Software**
   - Accurate for worship spaces with high RT60
   - STI (Speech Transmission Index) prediction
   - Auralization capabilities

3. **CATT-Acoustic**
   - Excellent for complex geometry (domes, arches, columns)
   - Frequency-dependent absorption modeling
   - Time-domain analysis

### Critical Input Data Still Required
- ⚠️ **AutoCAD file from mosque staff** (NOT YET RECEIVED)
- Precise ceiling heights at multiple points
- Dome geometry (Dome of the Eagle - octagonal dome)
- Column positions and dimensions (Corinthian columns)
- Material absorption coefficients:
  - Marble floors
  - Stone walls
  - **NEW carpet** (changed after initial visit - requires measurement)
  - Prayer rugs (occupancy-dependent)
  - Wooden features (doors, minbar)
  - Gold mosaic surfaces (4,000 m²)

---

## MEASUREMENT POSITION GRID (12+ Positions)

### Zone 1: MIHRAB & FRONT PRAYER AREA (3 positions)

**Position M1 - Front Center (Mihrab Axis)**
- **Location**: 3m from mihrab, on central axis below Dome of the Eagle
- **Height**: 1.5m (seated listener)
- **Purpose**: Imam's voice projection, dome reflection analysis
- **Expected Issues**:
  - Strong early reflections from dome (15-30ms)
  - Potential flutter echo from parallel walls
  - Low-frequency buildup in domed space

**Position M2 - Front Right (Near Qibla Wall)**
- **Location**: 5m from mihrab, 10m right of center axis
- **Height**: 1.5m
- **Purpose**: Asymmetry analysis, column shadowing effects
- **Expected Issues**:
  - Corinthian column obstruction
  - Delayed arrival from center speakers
  - Reduced high-frequency content (shadowing)

**Position M3 - Front Left (Near Qibla Wall)**
- **Location**: 5m from mihrab, 10m left of center axis
- **Height**: 1.5m
- **Purpose**: Left/right symmetry verification
- **Expected Issues**: Mirror of M2

---

### Zone 2: CENTRAL PRAYER HALL - UNDER ARCADES (4 positions)

**Position C1 - Center Mid-Hall (40m from Mihrab)**
- **Location**: 40m from mihrab, on central axis
- **Height**: 1.5m
- **Purpose**: Primary congregation area, delay timing verification
- **Expected Issues**:
  - Long RT60 tail (3.8-5.2s)
  - Multiple speaker overlap zone
  - Delay synchronization critical (expected: ~117ms from mihrab)

**Position C2 - Right Arcade (40m from Mihrab)**
- **Location**: 40m from mihrab, 15m right of center (between columns)
- **Height**: 1.5m
- **Purpose**: Arcade column effects, distributed speaker coverage
- **Expected Issues**:
  - Column-mounted speaker proximity (potential comb filtering)
  - Arcade ceiling reflections
  - Side wall flutter echo

**Position C3 - Left Arcade (40m from Mihrab)**
- **Location**: 40m from mihrab, 15m left of center
- **Height**: 1.5m
- **Purpose**: Left arcade symmetry verification
- **Expected Issues**: Mirror of C2

**Position C4 - Center Deep-Hall (80m from Mihrab)**
- **Location**: 80m from mihrab, on central axis
- **Height**: 1.5m
- **Purpose**: Long-throw speaker performance, far-field coverage
- **Expected Issues**:
  - Significant SPL drop (inverse square law)
  - Increased reverberant field dominance (D/R ratio negative)
  - Delay timing critical (expected: ~235ms from mihrab)

---

### Zone 3: REAR PRAYER HALL (3 positions)

**Position R1 - Back Center (120m from Mihrab)**
- **Location**: 120m from mihrab, on central axis
- **Height**: 1.5m
- **Purpose**: Maximum throw distance verification, worst-case scenario
- **Expected Issues**:
  - Severe SPL reduction (target: 75 dB minimum)
  - Heavy reverberant field (RT60 dominant over direct sound)
  - Delay synchronization critical (expected: ~353ms from mihrab)

**Position R2 - Back Right Corner**
- **Location**: 120m from mihrab, 15m right of center (near side wall)
- **Height**: 1.5m
- **Purpose**: Corner effects, worst acoustic environment
- **Expected Issues**:
  - Low-frequency buildup (corner loading)
  - Side wall reflections
  - Potential dead zone (speaker aim miss)

**Position R3 - Back Left Corner**
- **Location**: 120m from mihrab, 15m left of center
- **Height**: 1.5m
- **Purpose**: Corner symmetry verification
- **Expected Issues**: Mirror of R2

---

### Zone 4: COURTYARD (SAHN) (2 positions)

**Position Y1 - Courtyard Center (Open Air)**
- **Location**: Center of 122m × 50m courtyard
- **Height**: 1.5m
- **Purpose**: Exterior speaker coverage, weather effects
- **Expected Issues**:
  - No reverberation (open air)
  - Wind effects on propagation
  - Temperature gradient effects
  - SPL drop due to no boundary reinforcement

**Position Y2 - Courtyard Arcade (Under Perimeter Colonnade)**
- **Location**: Under arcade surrounding courtyard
- **Height**: 1.5m
- **Purpose**: Semi-exterior acoustic environment
- **Expected Issues**:
  - Partial reverberation from arcade ceiling
  - Transition zone between interior/exterior
  - Delayed sound from interior speakers bleeding through

---

### ADDITIONAL CRITICAL POSITIONS

**Position A1 - Athan Room (Separate Chamber)**
- **Location**: Center of Athan Room
- **Height**: 1.5m (standing performer position)
- **Purpose**: Feedback suppression requirements, room mode analysis
- **Expected Issues**:
  - Small room modes (standing waves)
  - High feedback potential (microphone + monitors)
  - Requires separate acoustic treatment

**Position A2 - Under Minaret (Exterior Ground Level)**
- **Location**: Base of Minaret of the Bride (40m height)
- **Height**: 1.5m
- **Purpose**: Exterior athan projection to market areas
- **Expected Issues**:
  - Urban acoustic environment (traffic noise ~70 dBA)
  - Building reflections from surrounding market
  - Weatherproofing requirements
  - 360° coverage pattern verification

---

## MEASUREMENT PARAMETERS FOR EACH POSITION

### Primary Measurements
1. **RT60 (Reverberation Time)**
   - Frequency bands: 125 Hz, 250 Hz, 500 Hz, 1 kHz, 2 kHz, 4 kHz, 8 kHz
   - Expected range: 3.8-5.2 seconds (current), target: 1.5-2.5 seconds (with treatment)

2. **STI (Speech Transmission Index)**
   - Scale: 0.00 (unintelligible) to 1.00 (perfect)
   - Current expected: 0.28-0.45 (Poor to Fair)
   - Target: >0.60 (Good to Excellent)

3. **SPL (Sound Pressure Level)**
   - Target: 75 dB ±3 dB at all listening positions
   - Ambient noise baseline: 55 dBA (empty mosque)
   - SNR (Signal-to-Noise Ratio): Minimum 15-20 dB

4. **Frequency Response (20 Hz - 20 kHz)**
   - 1/3 octave band resolution
   - Direct sound vs. reverberant field ratio
   - High-pass filter verification (<125 Hz rolloff)

5. **C50 (Clarity Index)**
   - Ratio of early sound (0-50ms) to late sound (>50ms)
   - Target: >+2 dB for good speech intelligibility
   - Critical speech bands: 1 kHz, 2 kHz, 4 kHz

6. **D/R Ratio (Direct-to-Reverberant Ratio)**
   - Positive D/R = more direct sound than reverberant (GOOD)
   - Negative D/R = reverberant field dominates (POOR for speech)
   - Target: >0 dB (positive) at all primary listening positions

7. **Delay Time Analysis**
   - Measure arrival time from each speaker zone
   - Identify delay mismatches (threshold: <15ms acceptable)
   - Current expected variance: 28-45ms (UNACCEPTABLE)

---

## EXPECTED FREQUENCY RESPONSE CHARACTERISTICS (By Position)

### EXISTING SYSTEM (Fragmented, 9 brands, 15-35 years old)

**Dynacord Speakers (1990-1995 generation)**
- **Low-frequency response (20-125 Hz)**: -15 to -20 dB (weak bass extension)
- **Mid-range (125-2000 Hz)**: Relatively flat but with 3-5 dB peaks at 400 Hz, 800 Hz
- **Critical speech band (2000-5000 Hz)**: Inconsistent, ±5 dB variance
- **High-frequency (5000-16000 Hz)**: **SEVERE ROLLOFF** -10 to -15 dB above 8 kHz (age degradation)
- **Overall character**: Muffled, muddy, poor speech clarity

**Inter-M SE-8 Speakers (1998-2002 generation)**
- **Low-frequency response**: -10 to -15 dB (better than Dynacord but still weak)
- **Mid-range**: 2-5 kHz band shows ±5-8 dB inconsistency (critical for intelligibility)
- **High-frequency**: Better extension than Dynacord but still -5 to -8 dB rolloff above 10 kHz
- **Left/Right asymmetry**: Significant variance indicating blown drivers or wiring faults

**UNI-PEX, TOA, PASO Speakers (1995-2005 generation)**
- **Power inconsistency**: 10W to 100W continuous (impossible to match SPL levels)
- **Frequency response**: Wide variance across brands
- **Expected rolloff**: Similar age-related degradation patterns

---

### PROPOSED SYSTEM (Unified, Line Arrays or Steerable Columns)

**Target Frequency Response (All Positions)**
- **Low-frequency (<125 Hz)**: Intentional rolloff -12 dB/octave via DSP high-pass filter
  - **Reason**: Reduces low-frequency buildup in reverberant space, prevents muddy sound
- **Mid-range (125-2000 Hz)**: ±3 dB flatness (room EQ applied)
- **Critical speech band (2000-5000 Hz)**: ±2 dB flatness (tightest tolerance)
  - **Boost**: +2 to +3 dB at 2.5 kHz and 4 kHz (speech presence enhancement)
- **High-frequency (5000-16000 Hz)**: -3 dB gentle rolloff above 10 kHz
  - **Reason**: Reduces excessive brightness in reverberant space, prevents harshness

**Position-Specific EQ Adjustments**

**Front Positions (M1, M2, M3) - Near Dome**
- **400-800 Hz**: -3 to -5 dB cut (dome resonance reduction)
- **2-4 kHz**: +2 dB boost (clarity enhancement under dome)

**Mid-Hall Positions (C1, C2, C3, C4)**
- **125-250 Hz**: -6 dB cut (arcade ceiling reflections reduction)
- **1-2 kHz**: ±0 dB (neutral, primary speech band)
- **4-8 kHz**: +1 dB boost (air absorption compensation)

**Rear Positions (R1, R2, R3) - Far Field**
- **2-5 kHz**: +3 to +4 dB boost (long-distance air absorption compensation)
- **8-16 kHz**: +2 dB boost (increased high-frequency reinforcement)

**Courtyard Positions (Y1, Y2) - Exterior**
- **Full-range response**: ±3 dB flatness (no room EQ needed in open air)
- **Wind compensation**: Dynamic EQ adjustment for outdoor conditions

---

## AI IMAGE GENERATION PROMPTS

### For Generating Accurate Frequency Response Graphs

**IMPORTANT**: These prompts are for creating scientifically accurate frequency response graphs based on acoustic simulation data. Use tools like DALL-E, Midjourney, or specialized acoustic visualization software.

---

#### PROMPT 1: Existing System - Dynacord Speaker (Aged, Degraded)

```
Create a professional frequency response graph for acoustic measurement analysis.

X-axis: Frequency (Hz) on logarithmic scale from 20 Hz to 16,000 Hz
Tick marks at: 20, 31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000

Y-axis: Gain (dB) from -20 dB to +5 dB
Horizontal gridlines every 5 dB

Graph characteristics:
- Line color: RED (#E74C3C)
- Line style: Solid, 2pt thickness
- Data points: Circular markers at each 1/3 octave band

Frequency response curve shape:
- 20-63 Hz: -20 dB (very weak bass)
- 63-125 Hz: Rising slope to -15 dB
- 125-250 Hz: -10 dB
- 250-500 Hz: Rising to -5 dB
- 500-800 Hz: Peak at 0 dB (minor resonance)
- 800-2000 Hz: Flat at -2 dB
- 2000-4000 Hz: Variable between -3 dB and +1 dB (inconsistent critical band)
- 4000-6300 Hz: Flat at 0 dB
- 6300-8000 Hz: Begin steep rolloff from 0 dB to -5 dB
- 8000-12500 Hz: Severe rolloff from -5 dB to -12 dB (AGE DEGRADATION)
- 12500-16000 Hz: Continued rolloff from -12 dB to -18 dB

Title: "Right Back (Dynacord) - Aged Speaker Response"
Legend: "Right Back (Dynacord)" in top-right corner

Style: Professional acoustic measurement graph with clean white background, gray gridlines, black text labels
```

---

#### PROMPT 2: Existing System - Inter-M SE-8 Speaker (Moderate Degradation)

```
Create a professional frequency response graph for acoustic measurement analysis.

X-axis: Frequency (Hz) on logarithmic scale from 20 Hz to 16,000 Hz
Tick marks at: 20, 31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000

Y-axis: Gain (dB) from -20 dB to +5 dB
Horizontal gridlines every 5 dB

Graph characteristics:
- Line color: ORANGE (#E67E22)
- Line style: Solid, 2pt thickness
- Data points: Circular markers at each 1/3 octave band

Frequency response curve shape:
- 20-63 Hz: -18 dB (weak bass)
- 63-125 Hz: Rising slope to -12 dB
- 125-250 Hz: -8 dB
- 250-500 Hz: -4 dB
- 500-1000 Hz: Flat at -2 dB
- 1000-2500 Hz: INCONSISTENT, variable between -4 dB and +2 dB (5-8 dB variance - CRITICAL SPEECH BAND PROBLEM)
- 2500-4000 Hz: Stabilize at 0 dB
- 4000-6300 Hz: +1 dB
- 6300-10000 Hz: Gradual rolloff from +1 dB to -3 dB (better high-frequency than Dynacord)
- 10000-12500 Hz: Moderate rolloff from -3 dB to -8 dB
- 12500-16000 Hz: -10 dB

Title: "Right Front (Inter-M SE-8) - Moderate Age Degradation"
Legend: "Right Front (Inter-M SE-8)" in top-right corner

Style: Professional acoustic measurement graph with clean white background, gray gridlines, black text labels
```

---

#### PROMPT 3: Reference System - Yamaha HS8 Studio Monitor (Flat Response Baseline)

```
Create a professional frequency response graph for acoustic measurement analysis.

X-axis: Frequency (Hz) on logarithmic scale from 20 Hz to 16,000 Hz
Tick marks at: 20, 31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000

Y-axis: Gain (dB) from -20 dB to +5 dB
Horizontal gridlines every 5 dB

Graph characteristics:
- Line color: BLUE (#3498DB)
- Line style: Solid, 2pt thickness
- Data points: Circular markers at each 1/3 octave band

Frequency response curve shape (FLAT REFERENCE):
- 20-40 Hz: -18 dB (below HS8 specification)
- 40-63 Hz: Rising to -8 dB
- 63-125 Hz: Rising to -2 dB
- 125-250 Hz: Flat at 0 dB
- 250-500 Hz: Flat at 0 dB
- 500-1000 Hz: Flat at +1 dB
- 1000-2000 Hz: FLAT at 0 dB (perfect critical speech band)
- 2000-4000 Hz: FLAT at 0 dB
- 4000-6300 Hz: Flat at 0 dB
- 6300-10000 Hz: Flat at -1 dB (very gentle rolloff)
- 10000-12500 Hz: Gentle rolloff to -3 dB
- 12500-16000 Hz: Smooth rolloff to -6 dB

Overall tolerance: ±3 dB from 50 Hz to 16 kHz (EXCELLENT FLAT RESPONSE)

Title: "Right Back - Yamaha HS8 (Reference Test)"
Legend: "Right Back - Yamaha HS8" in top-right corner

Style: Professional acoustic measurement graph with clean white background, gray gridlines, black text labels
```

---

#### PROMPT 4: Proposed System - Line Array with Room EQ (Position M1 - Front Center)

```
Create a professional frequency response graph for acoustic measurement analysis showing PROPOSED system response.

X-axis: Frequency (Hz) on logarithmic scale from 20 Hz to 16,000 Hz
Tick marks at: 20, 31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000

Y-axis: Gain (dB) from -20 dB to +5 dB
Horizontal gridlines every 5 dB

Graph characteristics:
- Line color: GREEN (#27AE60)
- Line style: Solid, 3pt thickness (emphasized as target)
- Data points: Circular markers at each 1/3 octave band

Frequency response curve shape (EQ'D FOR FRONT POSITION):
- 20-63 Hz: Steep rolloff from -20 dB (high-pass filter to -12 dB/octave)
- 63-125 Hz: -12 dB (intentional bass reduction for reverberant space)
- 125-250 Hz: -6 dB (controlled low-mid)
- 250-400 Hz: -3 dB (slight reduction)
- 400-800 Hz: -5 dB CUT (dome resonance compensation at front position)
- 800-1000 Hz: Rise to -1 dB
- 1000-2000 Hz: Flat at 0 dB (neutral speech foundation)
- 2000-2500 Hz: +2 dB BOOST (speech presence)
- 2500-4000 Hz: +3 dB BOOST (clarity enhancement under dome)
- 4000-6300 Hz: +2 dB (maintained brightness)
- 6300-10000 Hz: Flat at 0 dB
- 10000-12500 Hz: Gentle rolloff to -2 dB (controlled brightness in reverberant space)
- 12500-16000 Hz: -4 dB (prevents harshness)

Overall tolerance: ±2 dB from 1 kHz to 5 kHz (TIGHT SPEECH BAND CONTROL)

Title: "Proposed System - Position M1 (Front Center, Below Dome)"
Legend: "Proposed Line Array + Room EQ" in top-right corner with GREEN color

Style: Professional acoustic measurement graph with clean white background, gray gridlines, black text labels. Add subtle green shading under curve to emphasize this is target response.
```

---

#### PROMPT 5: Proposed System - Line Array with Room EQ (Position R1 - Rear Center, 120m)

```
Create a professional frequency response graph for acoustic measurement analysis showing PROPOSED system response.

X-axis: Frequency (Hz) on logarithmic scale from 20 Hz to 16,000 Hz
Tick marks at: 20, 31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000

Y-axis: Gain (dB) from -20 dB to +5 dB
Horizontal gridlines every 5 dB

Graph characteristics:
- Line color: GREEN (#27AE60)
- Line style: Solid, 3pt thickness
- Data points: Circular markers at each 1/3 octave band

Frequency response curve shape (EQ'D FOR REAR POSITION):
- 20-63 Hz: Steep rolloff from -20 dB (high-pass filter)
- 63-125 Hz: -12 dB (intentional bass reduction)
- 125-250 Hz: -6 dB
- 250-500 Hz: -3 dB
- 500-1000 Hz: -1 dB
- 1000-2000 Hz: Flat at 0 dB
- 2000-3150 Hz: +3 dB BOOST (long-distance air absorption compensation)
- 3150-5000 Hz: +4 dB BOOST (increased high-frequency reinforcement for far field)
- 5000-8000 Hz: +3 dB (maintained clarity at distance)
- 8000-10000 Hz: +2 dB (air absorption compensation above 8 kHz)
- 10000-12500 Hz: 0 dB (extended high-frequency response maintained)
- 12500-16000 Hz: -2 dB (gentle rolloff)

Overall tolerance: ±2 dB from 1 kHz to 5 kHz
Note: More aggressive high-frequency boost compared to front positions due to 120m propagation distance

Title: "Proposed System - Position R1 (Rear Center, 120m from Source)"
Legend: "Proposed Line Array + Room EQ (Long Throw)" in top-right corner with GREEN color

Style: Professional acoustic measurement graph with clean white background, gray gridlines, black text labels. Add subtle green shading under curve.
```

---

#### PROMPT 6: Courtyard (Exterior, Open Air) - Weatherproof Speakers

```
Create a professional frequency response graph for acoustic measurement analysis showing PROPOSED system response.

X-axis: Frequency (Hz) on logarithmic scale from 20 Hz to 16,000 Hz
Tick marks at: 20, 31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000

Y-axis: Gain (dB) from -20 dB to +5 dB
Horizontal gridlines every 5 dB

Graph characteristics:
- Line color: CYAN (#1ABC9C)
- Line style: Solid, 3pt thickness
- Data points: Circular markers at each 1/3 octave band

Frequency response curve shape (EXTERIOR, NO ROOM EQ):
- 20-40 Hz: -20 dB (outdoor speakers typically roll off below 40 Hz)
- 40-63 Hz: -10 dB
- 63-125 Hz: -4 dB
- 125-250 Hz: -1 dB
- 250-500 Hz: 0 dB (FLAT - no room modes in open air)
- 500-1000 Hz: 0 dB (FLAT)
- 1000-2000 Hz: 0 dB (FLAT)
- 2000-4000 Hz: 0 dB (FLAT)
- 4000-6300 Hz: 0 dB (FLAT)
- 6300-10000 Hz: -1 dB (very gentle rolloff)
- 10000-12500 Hz: -2 dB
- 12500-16000 Hz: -4 dB (natural speaker rolloff)

Overall tolerance: ±3 dB from 100 Hz to 10 kHz (EXCELLENT FLAT RESPONSE in non-reverberant environment)

Title: "Proposed System - Position Y1 (Courtyard Center, Open Air)"
Legend: "Weatherproof Column Speakers (Exterior)" in top-right corner with CYAN color

Style: Professional acoustic measurement graph with clean white background, gray gridlines, black text labels. Add subtle cyan shading under curve.
```

---

## SIMULATION WORKFLOW

### Step 1: 3D Model Creation
1. Import AutoCAD file into EASE/ODEON/CATT
2. Verify all dimensions (157m × 97m overall, 136m × 37m prayer hall, 122m × 50m courtyard)
3. Model Dome of the Eagle (octagonal, precise height TBD)
4. Model all Corinthian columns (8-12 units)
5. Model minarets (Bride ~40m, Jesus, Qaitbay)

### Step 2: Material Assignment
1. **Marble floors**: Absorption coefficient 0.01 @ 125 Hz to 0.02 @ 4 kHz (highly reflective)
2. **Stone walls**: 0.02 @ 125 Hz to 0.04 @ 4 kHz (reflective)
3. **New carpet**: Measure on-site or estimate 0.10 @ 125 Hz to 0.40 @ 4 kHz
4. **Prayer rugs (occupied)**: 0.25 @ 125 Hz to 0.60 @ 4 kHz (human absorption)
5. **Gold mosaics**: 0.01-0.02 (reflective like glass)
6. **Wooden features**: 0.10 @ 125 Hz to 0.10 @ 4 kHz

### Step 3: Speaker Placement Modeling
1. Import speaker GLL/CLF files (manufacturer data)
2. Position speakers per design (line arrays vs. columns)
3. Set aim angles (critical for directivity control)
4. Model delays (0ms, 131ms, 262ms zones)
5. Model EQ settings per zone

### Step 4: Run Simulations
1. Ray-tracing analysis (minimum 10,000 rays per source)
2. Calculate RT60 at all 12+ positions
3. Calculate STI at all positions
4. Calculate SPL coverage maps
5. Calculate C50, D/R ratio
6. Generate frequency response at each position
7. Export data for graph generation

### Step 5: Iterative Optimization
1. Adjust speaker aim angles
2. Adjust EQ settings
3. Adjust delay times
4. Re-run simulations
5. Compare results to targets
6. Repeat until targets achieved

---

## EXPECTED SIMULATION RESULTS (Targets)

| Position | RT60 (s) | STI | SPL (dB) | C50 (dB) | D/R Ratio (dB) | Notes |
|----------|----------|-----|----------|----------|----------------|-------|
| M1 - Front Center | 3.8-4.2 | >0.60 | 75 ±2 | >+2 | >0 | Below dome, strong early reflections |
| M2 - Front Right | 3.8-4.2 | >0.58 | 75 ±2 | >+1 | >0 | Column shadowing |
| M3 - Front Left | 3.8-4.2 | >0.58 | 75 ±2 | >+1 | >0 | Symmetry check |
| C1 - Mid-Hall Center | 4.0-4.5 | >0.55 | 75 ±3 | >+1 | >-1 | Primary congregation |
| C2 - Right Arcade | 4.0-4.5 | >0.52 | 75 ±3 | >0 | >-2 | Arcade reflections |
| C3 - Left Arcade | 4.0-4.5 | >0.52 | 75 ±3 | >0 | >-2 | Symmetry check |
| C4 - Deep-Hall | 4.2-4.8 | >0.50 | 75 ±3 | >0 | >-3 | Long throw challenge |
| R1 - Rear Center | 4.5-5.2 | >0.48 | 75 ±3 | >-1 | >-5 | Worst case, reverberant field dominant |
| R2 - Rear Right | 4.5-5.2 | >0.46 | 72 ±3 | >-2 | >-6 | Corner loading |
| R3 - Rear Left | 4.5-5.2 | >0.46 | 72 ±3 | >-2 | >-6 | Symmetry check |
| Y1 - Courtyard | 0.2-0.5 | >0.70 | 75 ±3 | >+10 | >+10 | Open air, minimal reverberation |
| Y2 - Arcade | 1.5-2.0 | >0.65 | 75 ±3 | >+5 | >+5 | Semi-exterior |

**Target Achievement**:
- STI >0.50 at ALL positions (minimum "Fair" intelligibility)
- STI >0.60 at 75% of positions (target "Good" intelligibility)
- SPL 75 dB ±3 dB at all primary positions
- No dead zones (SPL <65 dB unacceptable)

---

## VALIDATION REQUIREMENTS

### Pre-Installation Validation
1. **Simulation peer review**: Independent acoustic consultant verification
2. **Client review**: Present simulation results to mosque administration
3. **Manufacturer verification**: Confirm speaker GLL/CLF data accuracy
4. **Cost-benefit analysis**: Verify investment justification vs. performance improvement

### Post-Installation Validation
1. **On-site measurements at all 12+ positions**
2. **Compare measured vs. simulated data**
   - RT60: ±0.3s tolerance
   - STI: ±0.05 tolerance
   - SPL: ±2 dB tolerance
3. **Live application testing** (lectures, khutbas, prayers, inshad, athan)
4. **User feedback collection** (worshippers, imams, muezzins)
5. **Iterative tuning** until targets achieved

---

## TIMELINE FLEXIBILITY

⚠️ **IMPORTANT**: All dates in previous documents were examples only. Actual timeline depends on:

1. **AutoCAD file receipt** (NOT YET RECEIVED from mosque staff)
2. **Post-Ramadan re-measurement** (carpet changed, requires new baseline)
3. **Client approval process** (mosque administration decision timeline)
4. **Budget approval** (funding availability)
5. **Procurement lead times** (equipment availability, shipping to Syria)
6. **Installation access** (mosque schedule, prayer times, Ramadan restrictions)

**Estimated Timeline** (from project approval):
- **Phase 1**: Simulation & Design (4-6 weeks)
- **Phase 2**: Procurement & Shipping (8-12 weeks, Syria logistics)
- **Phase 3**: Installation (6-8 weeks, prayer schedule dependent)
- **Phase 4**: Testing & Tuning (2-3 weeks)
- **Phase 5**: Training & Handover (1 week)

**Total**: 21-30 weeks (5-7 months) from approval to completion

---

## NEXT STEPS

1. ✅ **Complete**: Reference document created
2. ⚠️ **PENDING**: Obtain AutoCAD file from mosque staff
3. ⚠️ **PENDING**: Schedule post-Ramadan acoustic measurements
4. ⚠️ **PENDING**: Run comprehensive acoustic simulations (12+ positions)
5. ⚠️ **PENDING**: Generate accurate frequency response graphs (use AI prompts above)
6. ⚠️ **PENDING**: Update HTML/PDF report with simulation data
7. ⚠️ **PENDING**: Client presentation and approval

---

**Document prepared by**: Obai Sukar
**Company**: obaisukar.com
**Purpose**: Scientific acoustic simulation specification for UNESCO World Heritage Site project
