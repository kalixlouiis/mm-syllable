# 📑 mm-syllable: A simple, rule-based tool for Myanamr (Burmese) syllable segmentation.

A lightweight, rule-based Burmese syllable tokenizer designed for accuracy and simplicity. Developed by **Khant Sint Heinn**.

## Key Features
*   **Zero Dependencies:** Built using only Python's standard library.
*   **Pali-Aware:** Correctly handles Pali conjuncts (ဗျည်းဆင့်) and stacked characters without breaking their phonetic integrity.
*   **Phonetic Precision:** Optimized for breaking syllables based on Burmese orthography and phonetics.

## Installation
```bash
pip install git+https://github.com/kalixlouiis/mm-syllable.git
```
# Quick Start
```python
from mmsyllable import SyllableBreaker

breaker = SyllableBreaker()

# Example 1: Standard Burmese
print(breaker.split("မြန်မာစာသည် လှပပါသည်။"))
# Output: ['မြန်', 'မာ', 'စာ', 'သည်', 'လှ', 'ပ', 'ပါ', 'သည်', '။']

# Example 2: Handling Pali Conjuncts (ဗျည်းဆင့်)
print(breaker.split("ပြဿနာရှိလျှင် ဖြေရှင်းပါ။"))
# Output: ['ပြဿ', 'နာ', 'ရှိ', 'လျှင်', 'ဖြေ', 'ရှင်း', 'ပါ', '။']

# Example 3: Complex Pali Words
print(breaker.split("ရွာအဝင်လမ်းတွင် ကြီးမားသော ကုက္ကိုလ်ပင်ကြီးတစ်ပင် ရှိသည်။"))
# Output: ['ရွာ', 'အ', 'ဝင်', 'လမ်း', 'တွင်', 'ကြီး', 'မား', 'သော', 'ကုက္ကိုလ်', 'ပင်', 'ကြီး', 'တစ်', 'ပင်', 'ရှိ', 'သည်', '။']
```
# How it Works❔

`mm-syllable` uses a refined Regex-based approach to identify syllable boundaries. It specifically prevents the over-segmentation of stacked characters (e.g., `ကုက္ကိုလ်`, `ကိစ္စ`), ensuring that the phonetic unit remains intact for downstream NLP tasks.

# 👤 Author
- Khant Sint Heinn

**Connect with the Author:**  
[GitHub](https://github.com/kalixlouiis) | [Hugging Face](https://huggingface.co/kalixlouiis) | [Kaggle](https://www.kaggle.com/organizations/kalixlouiis)

# 📑 License
- Apache-2.0
  
## Citation (BibTeX)
If you use `mm-syllable` in your research or project, please cite it as follows:
```BibTeX
@software{KhantSintHeinn_mmsyllable_2026,
  author = {{Khant Sint Heinn}},,
  title = {mm-syllable: A simple, rule-based tool for Myanamr (Burmese) syllable segmentation.},
  url = {https://github.com/kalixlouiis/mm-syllable},
  version = {0.1.0},
  year = {2026}
}
```

---
# About the Author

**Khant Sint Heinn**, working under the name **Kalix Louis**, is a **Machine Learning Engineer focused on Natural Language Processing (NLP), data foundations, and open-source AI development**. His work is centered on improving support for the Burmese (Myanmar) language in modern AI systems by building high-quality datasets, practical tools, and scalable infrastructure for language technology.

He is currently the **Lead Developer at DatarrX**, where he develops data pipelines, manages large-scale data collection workflows, and helps create open-source resources for researchers, developers, and organizations. His experience includes data engineering, web scripting, dataset curation, and building systems that support real-world machine learning applications.

Khant Sint Heinn is especially interested in advancing low-resource languages and making AI more accessible to underrepresented communities. Through his open-source contributions, he works to strengthen the Burmese (Myanmar) tech ecosystem and provide reliable building blocks for future language models, search systems, and intelligent applications.

His goal is simple: to turn limited language resources into practical opportunities through clean data, useful tools, and community-driven innovation.

**Connect with the Author:**  
[GitHub](https://github.com/kalixlouiis) | [Hugging Face](https://huggingface.co/kalixlouiis) | [Kaggle](https://www.kaggle.com/organizations/kalixlouiis)
