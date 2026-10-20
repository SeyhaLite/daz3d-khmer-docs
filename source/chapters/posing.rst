ជំពូក ៥ — Posing (កែកាយវិការ)
================================

.. meta::
   :description: ជំពូក ៥៖ Posing — ផ្ទាំង Posing, Universal/Pose Tool, កាយវិការមុខ (Expressions) និង Pose Presets។ Chapter 5: posing figures, pose tools, expressions and presets.


.. raw:: html

   <p class="src-note">បកប្រែពី៖ <a href="https://docs.daz3d.com/public/software/dazstudio/4/userguide/chapters/posing/start" target="_blank" rel="noopener">V — Posing</a> · <i>Giving Life to Your Scene</i></p>

Render មិនគួរឱ្យចាប់អារម្មណ៍ទេ បើតួនៅក្នុង «T-pose» លំនាំដើម។ Posing ជួយឱ្យ render **ប្រាប់រឿង** — បង្កើត «leading lines» សម្រាប់សមាសភាព លាយតួជាមួយឆាក ឬធ្វើឱ្យវាលេចធ្លោ។ Posing គួរជាជំហានសំខាន់បំផុតមួយក្នុងលំហូរការងារ — បើ pose មិនធម្មជាតិ render នឹងមើលទៅ «សំប៉ែត» មិនថា realistic ឬ stylized ទេ។

ដោយសារ posing សំខាន់ខ្លាំង Daz Studio មាន Activity ទាំងមូលសម្រាប់វា — **'Pose & Animate'** នៃ layout Hollywood Blvd។

ការជ្រើសសម្រាប់ Posing
------------------------

ដូចក្នុង Shaping — ការជ្រើសឆាកបច្ចុប្បន្នកំណត់លក្ខណៈសម្បត្តិដែលបង្ហាញក្នុងផ្ទាំង Posing។ លក្ខណៈសម្បត្តិត្រូវបានរៀបចំជាក្រុមតាមមុខងារ ហើយតួដែលមាន nodes ច្រើនអាចមាន groups/លក្ខណៈសម្បត្តិផ្សេងគ្នាសម្រាប់ node នីមួយៗ។

អ្វីដែលត្រូវធ្វើគឺ **ជ្រើស node ដែលចង់ pose**៖ ចង់កែដៃ → ជ្រើសដៃ · ចង់កែភ្លៅ → ជ្រើសភ្លៅ។

- ជ្រើសតាមផ្ទាំង **Scene** ឬផ្ទាល់ក្នុង **Viewport**
- **Universal Tool** — បើកពី toolbar រួចចុច node ក្នុង Viewport (ដាក់ទ្រនិចលើតួ → ផ្នែករាងកាយលេចពណ៌ → ចុចឆ្វេងដើម្បីជ្រើស)
- **ចុចស្ដាំ** ក្នុង Viewport → ម៉ឺនុយបង្ហាញបញ្ជី nodes ដែលជ្រើសបានពីចំណុចនោះ — មានប្រយោជន៍សម្រាប់ជ្រើសសម្លៀកបំពាក់ សក់ ឬ followers ផ្សេងៗដែល conformed នឹងតួ

ផ្ទាំង Posing
-------------

ស្ថិតនៅខាងឆ្វេង (ក្នុង Activity 'Pose & Animate') — មាន ២ pages ដូច Surfaces/Shaping៖ **Editor** និង **Presets** (ប្ដូរដោយចុចស្លាកខាងលើ)។

Page Editor
~~~~~~~~~~~

- **Group View** (ឆ្វេង) — property groups ទាំងអស់សម្រាប់ការជ្រើសបច្ចុប្បន្ន (ដូច Parameters ប៉ុន្តែបង្ហាញតែ groups ដែលមានលក្ខណៈសម្បត្តិ posing)។ ចុចដើម្បីជ្រើស · ចុចព្រួញដើម្បីពង្រីក/បង្រួម
- **Property View** (ស្ដាំ) — លក្ខណៈសម្បត្តិ posing នីមួយៗនៃ group ដែលជ្រើស។ អូស slider ឆ្វេង/ស្ដាំ ឬចុចលើលេខ រួចវាយតម្លៃផ្ទាល់ខ្លួន
- **Scene Selection Menu** (ម៉ឺនុយធ្លាក់ចុះខាងលើឆ្វេង) — កំណែតូចនៃផ្ទាំង Scene សម្រាប់ប្ដូរការជ្រើសរហ័ស
- **Filters** — «All» = លក្ខណៈសម្បត្តិ posing ទាំងអស់ · «Currently Used» = តែអ្វីដែលអ្នកបានកែ (វិធីងាយមើលថាអ្វីកំពុងប៉ះពាល់ការជ្រើស)
- មាន **ការស្វែងរកអត្ថបទ** នៅផ្នែកខាងលើផ្ទាំង

.. important:: រកលក្ខណៈសម្បត្តិមិនឃើញ? សាក (១) ប្ដូរ node ដែលជ្រើស (២) ប្ដូរ property group (៣) ប្រើ filter «All»។

.. tip:: Posing ជំនាញបានដោយ **អនុវត្ត** — ចំណាយពីរនាទីលេងក្នុង Editor page៖ ប្ដូរការជ្រើស ប្ដូរ group អូស slider នីមួយៗដើម្បីឃើញឥទ្ធិពល។ វីដេអូជំនួយ៖ `Posing Pane Overview <https://docs.daz3d.com/public/software/dazstudio/4/userguide/posing/videos/posing/start>`_។

Page Presets
~~~~~~~~~~~~

កន្លែងផ្ទុក **Pose Presets** — preset អនុវត្តកាយវិការកំណត់ជាមុនទៅលើតួ ជួយសន្សំពេលវេលា (ជំនួសការ pose node នីមួយៗដោយដៃ)។ សម្រាប់អ្នកសិល្បៈភាគច្រើន Pose Preset ជា **ចំណុចចាប់ផ្តើម** — ផ្ទុក preset រួចកែបន្តិចបន្តួចក្នុង Editor page។

- រៀបចំដូច Smart Content៖ categories នៅខាងឆ្វេង (ចុចព្រួញដើម្បីពង្រីក subcategories) · poses នៅខាងស្ដាំ
- ផ្ទុកដោយ **ចុចពីរដង** លើរូបភាពតំណាង ឬ **អូសទម្លាក់** លើតួ
- **ចុចស្ដាំ** លើរូបភាពតំណាង → ជម្រើសបន្ថែម រួមទាំង **merge** pose ចូលឆាក
- Pose Presets ភាគច្រើនរៀបចំតាម function និង region — Daz Studio ភ្ជាប់ presets មួយចំនួនសម្រាប់ Genesis និង Genesis 2 Female (មើលក្រោម category **Poses**)។ Presets បន្ថែមអាចទិញពី `DAZ 3D Store <https://www.daz3d.com/animations-poses>`_

.. note:: Pose Presets ខ្លះមាន rotation ក្រៅដែនកំណត់ធម្មតារបស់តួ — ពេលផ្ទុក អ្នកនឹងត្រូវបានសួរឱ្យ **បិទ limits**។ គួរយល់ព្រម បើចង់ឱ្យ pose ត្រូវនឹងឯកសារ។ ហើយដូច Smart Content — បង្ហាញតែ presets ដែលស្របនឹងការជ្រើសបច្ចុប្បន្ន ដូច្នេះជ្រើសតួជាមុន។

Posing ផ្ទាល់ក្នុង Viewport
---------------------------

អ្នកខ្លះចូលចិត្ត pose ផ្ទាល់ក្នុង Viewport ជាង។ ជាទូទៅគេប្រើ **ផ្សំគ្នា**៖ ចលនាធំៗក្នុង Viewport រួចកែលម្អិតតូចៗក្នុង Editor page របស់ផ្ទាំង Posing។ ឧបករណ៍សំខាន់ពីរ៖

Universal Tool
~~~~~~~~~~~~~~

ឧបករណ៍ដែលអ្នកស្គាល់ពីជំពូកមុន (translate/rotate/scale) — ក៏ប្រើ pose **nodes** របស់តួបានដែរ៖

#. បើកឧបករណ៍ពី toolbar (រូបភាពតំណាងនឹងលេចពណ៌ពេលសកម្ម)
#. ជ្រើសតួ (ដាក់ទ្រនិចលើតួ → លេចពណ៌ → ចុច) រួចជ្រើស node (ផ្នែករាងកាយលេចពណ៌ពេលដាក់ទ្រនិចលើ)
#. ប្រើ gizmos — **rotation ងាយស្រួលបំផុត** ព្រោះវាប៉ះពាល់តែ node ដែលជ្រើស ខណៈ translation អាចប៉ះពាល់ nodes ខាងលើក្នុង chain។ ចុចឆ្វេង + អូសធ្នូ ក្រហម (X) / បៃតង (Y) / ខៀវ (Z) ដើម្បីបង្វិល

.. tip:: Universal Tool មានតម្លៃខ្លាំងពេល pose **ដៃ និងម្រាមដៃ**។

Pose Tool
~~~~~~~~~

ឧបករណ៍ pose ជំនាញក្នុង Viewport ជាមួយមុខងារគួរឱ្យចាប់អារម្មណ៍៖

.. note:: ក្នុង layout Hollywood Blvd — Pose Tool **លាក់ជាលំនាំដើម**។ បើកវាតាមរយៈ **Viewport Options Menu** → **'Show Pose Tool.'** ហើយវាលេចតែពេលអ្នកជ្រើស **ឆ្អឹង (bone)** — បើជ្រើស root node វាមិនលេចទេ។

- **Free Rotate Control** — បាល់នៅកណ្ដាលឧបករណ៍៖ ចុច + អូសដើម្បីបង្វិលឆ្អឹង **គ្រប់អ័ក្សទាំង ៣ ព្រមគ្នា**។ «Angle Indicators» នីមួយៗផ្លាស់ទីក្នុងដែនរបស់វា បង្ហាញពីឥទ្ធិពលលើអ័ក្សនីមួយៗ
- **Pose Controls** — កងពណ៌រង្វេលកណ្ដាល (concentric rings) សម្រាប់អ័ក្សនីមួយៗ៖ 🔴 X · 🟢 Y · 🔵 Z។ ចុចលើកង រួចអូសដើម្បី pose តាមអ័ក្សនោះ។ បន្ទាត់ខ្មៅ = ទីតាំងបច្ចុប្បន្ន។ កងមានពីរពណ៌៖ ពណ៌ច្បាស់ = ដែន pose បាន · ពណ៌ស្រអាប់ = ក្រៅដែនកំណត់ rotation
- **Restore Options Menu** (រូបភាពតំណាងខាងលើឆ្វេង) — ស្ដារ pose នៃឆ្អឹងបច្ចុប្បន្ន ឬតួទាំងមូល (សម្រាប់ពេលខូច ចង់ចាប់ផ្តើមឡើងវិញ) + បើក/បិទ rotation limits
- **Pinning Options Menu** (រូបភាពតំណាងខាងលើស្ដាំ) — pin (ខ្ទាស់) ឆ្អឹងឱ្យនៅនឹងថ្កល់ ឬ unpin។ ចំណាំ៖ ជា **soft pins** — ឆ្អឹងដែល pin ព្យាយាមនៅនឹងថ្កល់ ប៉ុន្តែបើចលនាឆ្អឹងផ្សេងទាញវា វានឹងផ្លាស់ទី ហើយបន្ទាត់ដាច់ៗនឹងលេចពី pin ទៅឆ្អឹង។ សាកល្បង៖ pin ជើងរបស់ Genesis 2 Female រួចអូសដៃ — ដល់ចំណុចមួយជើងនឹងដើរតាម។ ការ pose ដោយ pins ត្រូវការការអនុវត្ត — **មិនណែនាំសម្រាប់អ្នកថ្មី**។

កាយវិការមុខ (Expressions)
-----------------------------

Pose ល្អបំផុតក៏មិនពេញលេញដែរ បើគ្មាន expression សមស្រប — expressions ជាផ្នែកមិនអាចខ្វះនៃ posing។

#. **ជ្រើសក្បាល (Head)** របស់តួ — ក្នុងផ្ទាំង Scene ឬ Scene Selection Menu នៃផ្ទាំង Posing។ ⚠️ សំខាន់ណាស់៖ បើជ្រើស node ផ្សេង expression controls មិនលេចទេ!
#. ក្នុងផ្ទាំង Posing → group **'Pose Controls'** → ពង្រីកឃើញ **'Head'** និង **'Neck'**
#. ក្រោម 'Head' មាន groups សម្រាប់ **'Brow'** (ចិញ្ចើម), **'Cheeks'** (ថ្ពាល់), **'Eyes'** (ភ្នែក) ជាដើម — រួមទាំង group **'Expressions'** ដែលមាន expression ពេញលេញរួចរាល់
#. អូស sliders — ប្រើលក្ខណៈសម្បត្តិតែមួយ ឬផ្សំគ្នា ដើម្បីបង្កើត expression ដ៏ល្អឥតខ្ចោះ

Genesis និង Genesis 2 Female ភ្ជាប់មកជាមួយ expressions និង pose controls សម្រាប់មុខមួយចំនួន — បន្ថែមអាចទិញពី DAZ 3D Store។ Expression ក៏អាចផ្ទុកជា Pose Preset ពី Presets page បានដែរ។

រក្សាទុក Pose Preset ផ្ទាល់ខ្លួន
---------------------------------

#. **File > Save As > Pose Preset…** (ឬចុច Pose Preset action ក្នុង toolbar) → ផ្ទាំងសន្ទនា «Filtered Save» — ដាក់ឈ្មោះ ជ្រើសទីតាំង ចុច **Save**
#. ផ្ទាំងសន្ទនា **«Pose Preset Save Options»**៖

   - **«Animation Range»** — ជ្រើស animation sequence ឬ pose តែមួយ frame។ បើមិនបានបង្កើត animation ជ្រើស **'Current Frame Only'**
   - **«Properties List»** — ជ្រើសលក្ខណៈសម្បត្តិដែលរួមក្នុង preset (ពង្រីក skeleton និង property groups ដោយចុចព្រួញ · ដកធីកដើម្បីដកចេញ)
   - **«File Options»** — compress ឯកសារ (ណែនាំ — សន្សំកន្លែងថាស។ ឯកសារ compressed ត្រូវ «unzip» មុនកែក្នុង text editor — អាច unzip តាមរយៈផ្ទាំង Batch Convert)

#. ចុច **Accept** — preset លេចក្រោម category **'Uncategorized'** នៃ Presets page

.. warning::

   ដកធីក property group **'General'** ក្រោម root node របស់តួ — បើមិនដូច្នោះ Pose Preset នឹងផ្លាស់ទីតួទាំងមូលពេលអនុវត្ត (ជាធម្មតាអ្នកមិនចង់បានទេ!)។

គន្លឹះចុងក្រោយ
---------------

- Pose ជាច្រើន **អាស្រ័យលើរូបរាងតួ** — លំដាប់ល្អបំផុត៖ **Shape មុន រួច Pose**។ បើធ្វើច្រាស អាចមាន collisions ឬអ្វីៗមិនត្រូវគ្នាក្រោយពេល shape
- Pose Preset នីមួយៗត្រូវបានរចនាសម្រាប់តួ/រូបរាងជាក់លាក់ (ជាធម្មតាបញ្ជាក់ក្នុងឈ្មោះ) — អាចប្រើលើតួផ្សេងបាន ប៉ុន្តែត្រូវការការកែបន្តិចបន្តួចក្នុង Editor page
- ភាពជំនាញត្រូវការពេលវេលា — កុំប្រញាប់ អនុវត្តដោយអត់ធ្មត់
