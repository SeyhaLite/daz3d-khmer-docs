# Daz Studio 4.x — ឯកសារជាភាសាខ្មែរ

ការបកប្រែជាភាសាខ្មែរដោយសហគមន៍ នៃឯកសារផ្លូវការ **Daz Studio 4.x**
(កំណែចេញផ្សាយទូទៅថ្មីបំផុត **4.24.0.4**) ពី
[DAZ 3D Documentation Center](https://docs.daz3d.com/public/software/dazstudio/4/start)។

**អានឯកសារ៖** <https://seyhalite.github.io/daz3d-khmer-docs/>
ទំព័របម្រុង (Read the Docs)៖ <https://daz3d-khmer-doc.readthedocs.io/>

គម្រោងនេះជាគម្រោងសហគមន៍ឯករាជ្យ — មិនមានទំនាក់ទំនង ឬការគាំទ្រផ្លូវការពី DAZ 3D, LP ទេ។

## មាតិកា

| ផ្នែក | ការពិពណ៌នា |
|---|---|
| ការចាប់ផ្តើម | ការចុះឈ្មោះ ការផ្ទុកមាតិកា ការជ្រើសវត្ថុក្នុងឆាក និងមគ្គុទ្ទេសក៍ QuickStart (Barefoot Dancer) |
| មគ្គុទ្ទេសក៍អ្នកប្រើប្រាស់ ជំពូក ១–៨ | ចំណុចប្រទាក់ ការសាងសង់ឆាក វាយនភាព/ផ្ទៃ/សម្ភារៈ Shaping Posing កាមេរ៉ា និងទិដ្ឋភាព ពន្លឺ និងការ Render |
| មេរៀនបន្ថែម | ការប្ដូរ Interface Layout និង Style ការរក្សាទុក Layout ផ្ទាល់ខ្លួន និងការរៀបចំផ្ទាំង (Panes) |
| ឯកសារយោង | សង្ខេបចំណុចប្រទាក់អ្នកប្រើប្រាស់ និងវចនានុក្រមពាក្យបច្ចេកទេស (ខ្មែរ–អង់គ្លេស) |

គ្រប់ទំព័រមានរូបភាព និងដ្យាក្រាមពីឯកសារផ្លូវការរបស់ DAZ 3D
(User Guide PDF និង Documentation Center)។

## លក្ខណៈពិសេស

- សាងសង់ដោយ Sphinx និង theme ស្តង់ដារ Read the Docs (`sphinx_rtd_theme`)
- ពុម្ពអក្សរខ្មែរពេញលេញ (Noto Sans Khmer / Noto Serif Khmer និង Khmer OS ជា fallback)
- របៀបពណ៌ងងឹតតែមួយមុខ (dark-only) សម្រាប់គ្រប់ទំព័រ
- ប៊ូតុង «Edit on GitHub» នៅលើគ្រប់ទំព័រ សម្រាប់កែតម្រូវបានភ្លាមៗ
- ប្រព័ន្ធសវែងរកក្នុងឯកសារ (ពាក្យបច្ចេកទេសអង់គ្លេសនៅតែស្វែងរកបាន)
- ផ្សាយលើ Read the Docs និងធ្វើ mirror លើ GitHub Pages

## ការសាងសង់ក្នុងម៉ាស៊ីនរបស់អ្នក

```bash
pip install -r requirements.txt
make html        # លទ្ធផលនៅក្នុងថត docs/
```

## ការផ្សាយ (Deployment)

- **Read the Docs** — ដំណើរការតាមឯកសារ `.readthedocs.yaml` (Sphinx config៖ `source/conf.py`)
- **GitHub Pages** — បម្រើពីថត `docs/` លើ branch `main`

## អាជ្ញាបណ្ណ

- មាតិកាឯកសារ និងការបកប្រែជាភាសាខ្មែរ៖
  **Creative Commons Attribution 4.0 International** — សូមមើល [`LICENSE`](LICENSE)។
  ឯកសារដើមជាភាសាអង់គ្លេស ជាកម្មសិទ្ធិរបស់ DAZ 3D, LP ក្រោមអាជ្ញាបណ្ណ
  [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)។
  រូបភាព និងដ្យាក្រាម នៅជាកម្មសិទ្ធិរបស់ម្ចាស់ដើមរៀងៗខ្លួន។
- ការបត់បែន theme ឯកសារកំណត់ (configuration) និងកូដសាងសង់៖
  **MIT License** — សូមមើល [`LICENSE-CODE`](LICENSE-CODE)។

## ការចូលរួមវិភាគទាន

ចុចប៊ូតុង «Edit on GitHub» នៅលើទំព័រណាមួយ ឬកែឯកសារ reStructuredText
ក្នុងថត `source/` រួចបើក Pull Request។ សូមរក្សាឈ្មោះធាតុចំណុចប្រទាក់
(ម៉ឺនុយ ប៊ូតុង ផ្ទាំង) ជាភាសាអង់គ្លេស ដើម្បីឱ្យស្របនឹងកម្មវិធី
ហើយប្រើពុម្ពអក្សរខ្មែរស្តង់ដារ (Unicode)។
