# NLP CLI Suite

[![Research Benchmark CI](https://github.com/rgb-99/nlp-cli-suite/actions/workflows/research-ci.yml/badge.svg)](https://github.com/rgb-99/nlp-cli-suite/actions)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

> Unified research infrastructure for reproducible NLP benchmarking, regression detection, and experiment orchestration.

`nlp-cli-suite` is a **research-grade NLP experimentation platform** that orchestrates multi-model benchmarking, regression detection, result archiving, and CI automation — the same class of tooling used by infrastructure teams at HuggingFace, EleutherAI, and BigScience.

It answers the question:

> **“Can we trust this model version in production and can we prove it?”**

---

## Why This Tool Exists

Most ML projects:

• Run one-off benchmarks  
• Manually compare results  
• Lose historical performance data  
• Ship silent performance regressions  

This platform introduces **continuous research benchmarking** — performance becomes a *first-class CI artifact.*

---

## Research Pipeline

```
Suite Definition (YAML)
↓
Parallel Model Execution
↓
Device-Agnostic Benchmarking
↓
Structured JSON Archival
↓
CSV Artifact Export
↓
Baseline vs Current Regression Detection
↓
CI-Gated Performance Validation
```
---

## Platform Components

| Layer | Tool |
|------|----|
| Dataset ingestion | `nlp-engine-yuvraj` |
| Model benchmarking | `hf-inference-benchmark` |
| Orchestration & CI | `nlp-cli-suite` |

---

## Installation

```bash
# From Source (for Developers)
git clone https://github.com/rgb-99/nlp-cli-suite.git
cd nlp-cli-suite
pip install -e .
```
---

## CLI

```bash
nlp-tool --help
``` 
```
|Command |Purpose|
|------|----|
|ingest	|Dataset ingestion|
|benchmark|	Benchmark single model|
|suite	|Run multi-model suites|
|report	|Generate leaderboards|
|compare	|Detect regressions|
``` 
---

## Run a Research Suite
suite.yaml
```yaml
out_dir: current_results
workers: 2

benchmarks:
  - model: facebook/opt-125m
    tokens: 32
    out: facebook_opt-125m.json

  - model: gpt2
    tokens: 32
    out: gpt2.json

  - model: EleutherAI/pythia-70m
    tokens: 32
    out: EleutherAI_pythia-70m.json
```    
Run:

```bash

nlp-tool suite suite.yaml
```
---

## Leaderboard Generation
```bash

nlp-tool report current_results
```
```bash

Model Performance Leaderboard

Model                     Speed(tok/s)   Latency(ms)   Memory(MB)
---------------------------------------------------------------
EleutherAI/pythia-70m       115.8          268.3        591.5
distilgpt2                  81.6          401.4        663.0
facebook/opt-125m           53.6         3442.9        798.5
gpt2                        50.5         3652.8        854.1

``` 
---

## Regression Detection
```bash

nlp-tool compare baseline_results current_results
``` 
```bash
MODEL REGRESSION REPORT

Model                 Speed Δ %   Memory Δ MB   Verdict
------------------------------------------------------
facebook/opt-125m      -4.2%       -0.39 MB     REGRESSED
gpt2                  -81.95%      -1.34 MB     REGRESSED
```
---

CI Automation
The GitHub Actions pipeline:

• Executes benchmark suites
• Archives artifacts
• Compares against baselines
• Fails on regressions
• Produces CSV research artifacts

This creates a continuous research benchmarking system.