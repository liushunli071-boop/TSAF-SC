
# TSAF-SC V9.1

A reproducible computational framework for stability analysis and phase transition detection in complex systems.

---

## 📌 DOI

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20278955.svg)](https://doi.org/10.5281/zenodo.20278955)

---

## 🧠 Overview

TSAF-SC is a minimal axiomatic computational system designed to model:

- System stability evolution
- Phase transition detection
- Structural regime shifts in dynamic systems

It defines a computable stability function σ(x) and a formal transition criterion based on structural perturbations.

---

## 📐 Model

Stability is defined as:

σ(x) = α·f(x) + β·g(x) + γ·h(x)

where:

- f(x): mean state value  
- g(x): variance component  
- h(x): anomaly ratio  

---

## ⚙️ How to Run

```bash
python src/main.py