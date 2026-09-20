# Health Insurance — Inline Trust Signal & Accordion Disclaimer

**Vertical:** Health Insurance, including Critical Illness
**Prepared:** 2026-07-31

Approved copy, reproduced verbatim. The only addition is that the three credential numbers are now hyperlinked to their source documents. No wording changed.

## Links used

| Credential | Number | Links to |
|---|---|---|
| Central Bank of the UAE registration | 123 | `https://cdn.policybazaar.ae/pbuae/images/IA-License-Renewal-2026.pdf` |
| DHA health insurance intermediary permit | BRK-00041 | `https://www.isahd.ae/Home/PermittedIntermediaries` |
| Emirates Insurance Federation membership | B81 | `https://static.pbcdn.ae/pbuae/images/Policybazaar-Middle-East-Insurance-Brokers-LLC.pdf` |

All three verified against the source documents on 2026-07-31.

---

## 1. Inline Trust Signal

### English

> Licensed by the Central Bank of the UAE (Registration No. 123) · DHA Health Insurance Intermediary Permit No. BRK-00041 · Emirates Insurance Federation Membership No. B81
> Information on this page is for general guidance only — not personalised financial or medical advice. Speak to one of our advisors →

```html
<div class="trust-signal" lang="en">
  <p class="trust-signal__credentials">
    Licensed by the Central Bank of the UAE
    (<a href="https://cdn.policybazaar.ae/pbuae/images/IA-License-Renewal-2026.pdf" target="_blank" rel="noopener">Registration No. 123</a>)
    ·
    DHA Health Insurance Intermediary Permit No.
    <a href="https://www.isahd.ae/Home/PermittedIntermediaries" target="_blank" rel="noopener">BRK-00041</a>
    ·
    Emirates Insurance Federation Membership No.
    <a href="https://static.pbcdn.ae/pbuae/images/Policybazaar-Middle-East-Insurance-Brokers-LLC.pdf" target="_blank" rel="noopener">B81</a>
  </p>
  <p class="trust-signal__advice">
    Information on this page is for general guidance only — not personalised financial or medical advice.
    <a href="/contact-us/">Speak to one of our advisors →</a>
  </p>
</div>
```

### Arabic

> مرخصة من قِبل مصرف الإمارات العربية المتحدة المركزي (رقم التسجيل: 123) · تصريح وسيط التأمين الصحي من هيئة الصحة بدبي رقم BRK-00041 · عضوية اتحاد التأمين الإماراتي رقم B81
> المعلومات الواردة في هذه الصفحة للتوجيه العام فقط — وليست نصيحة مالية أو طبية مخصصة. تحدّث إلى أحد مستشارينا ←

```html
<div class="trust-signal" lang="ar" dir="rtl">
  <p class="trust-signal__credentials">
    مرخصة من قِبل مصرف الإمارات العربية المتحدة المركزي
    (<a href="https://cdn.policybazaar.ae/pbuae/images/IA-License-Renewal-2026.pdf" target="_blank" rel="noopener">رقم التسجيل: <bdi>123</bdi></a>)
    ·
    تصريح وسيط التأمين الصحي من هيئة الصحة بدبي رقم
    <a href="https://www.isahd.ae/Home/PermittedIntermediaries" target="_blank" rel="noopener"><bdi>BRK-00041</bdi></a>
    ·
    عضوية اتحاد التأمين الإماراتي رقم
    <a href="https://static.pbcdn.ae/pbuae/images/Policybazaar-Middle-East-Insurance-Brokers-LLC.pdf" target="_blank" rel="noopener"><bdi>B81</bdi></a>
  </p>
  <p class="trust-signal__advice">
    المعلومات الواردة في هذه الصفحة للتوجيه العام فقط — وليست نصيحة مالية أو طبية مخصصة.
    <a href="/ar-ae/contact-us/">تحدّث إلى أحد مستشارينا ←</a>
  </p>
</div>
```

`<bdi>` keeps the Latin-script numbers from being reversed inside right-to-left text.

---

## 2. Accordion Disclaimer

### English

> **Disclaimer**
> This page is published by Policybazaar Middle East Insurance Brokers LLC, licensed and regulated by the Central Bank of the UAE (Registration No. 123).
> Health Insurance Intermediary: Dubai Health Authority Permit No. BRK-00041. Member of Emirates Insurance Federation, Membership No. B81.
> Content on this page is for general informational purposes only and does not constitute personalised financial or medical advice. Coverage terms, premiums, and eligibility vary by insurer and individual circumstances. We strongly recommend speaking with one of our licensed advisors before purchasing any health insurance product.
> *T&C Apply.

```html
<details class="disclaimer" lang="en">
  <summary>Disclaimer</summary>
  <div class="disclaimer__body">
    <p>
      This page is published by Policybazaar Middle East Insurance Brokers LLC, licensed and regulated by the Central Bank of the UAE
      (<a href="https://cdn.policybazaar.ae/pbuae/images/IA-License-Renewal-2026.pdf" target="_blank" rel="noopener">Registration No. 123</a>).
    </p>
    <p>
      Health Insurance Intermediary: Dubai Health Authority Permit No.
      <a href="https://www.isahd.ae/Home/PermittedIntermediaries" target="_blank" rel="noopener">BRK-00041</a>.
      Member of Emirates Insurance Federation, Membership No.
      <a href="https://static.pbcdn.ae/pbuae/images/Policybazaar-Middle-East-Insurance-Brokers-LLC.pdf" target="_blank" rel="noopener">B81</a>.
    </p>
    <p>
      Content on this page is for general informational purposes only and does not constitute personalised financial or medical advice.
      Coverage terms, premiums, and eligibility vary by insurer and individual circumstances.
      We strongly recommend speaking with one of our licensed advisors before purchasing any health insurance product.
    </p>
    <p class="disclaimer__tc">*T&amp;C Apply.</p>
  </div>
</details>
```

### Arabic

> إخلاء المسؤولية
>
> هذه الصفحة منشورة من قبل شركة بوليسي بازار الشرق الأوسط لوساطة التأمين ذ.م.م، المرخصة والخاضعة لرقابة مصرف الإمارات العربية المتحدة المركزي (رقم التسجيل: 123)، والحاصلة على تصريح وسيط التأمين الصحي رقم BRK-00041 الصادر عن هيئة الصحة بدبي، وعضو اتحاد التأمين الإماراتي برقم العضوية B81.
>
> المعلومات والمحتوى الواردان في هذه الصفحة مخصصان لأغراض المعلومات والتوعية العامة فقط، ولا يشكلان نصيحة مالية أو طبية مخصصة. قد تختلف شروط التغطية التأمينية والأقساط ومعايير الأهلية وفقاً لشركة التأمين والظروف الفردية لكل عميل.
>
> ننصح بالتحدث إلى أحد مستشارينا المرخصين قبل شراء أي منتج للتأمين الصحي.
>
> *تسري الشروط والأحكام.

The approved text ended `*تسري الشروط والأحكا`, missing the final `م`. Corrected above.

```html
<details class="disclaimer" lang="ar" dir="rtl">
  <summary>إخلاء المسؤولية</summary>
  <div class="disclaimer__body">
    <p>
      هذه الصفحة منشورة من قبل شركة بوليسي بازار الشرق الأوسط لوساطة التأمين ذ.م.م، المرخصة والخاضعة لرقابة مصرف الإمارات العربية المتحدة المركزي
      (<a href="https://cdn.policybazaar.ae/pbuae/images/IA-License-Renewal-2026.pdf" target="_blank" rel="noopener">رقم التسجيل: <bdi>123</bdi></a>)،
      والحاصلة على تصريح وسيط التأمين الصحي رقم
      <a href="https://www.isahd.ae/Home/PermittedIntermediaries" target="_blank" rel="noopener"><bdi>BRK-00041</bdi></a>
      الصادر عن هيئة الصحة بدبي، وعضو اتحاد التأمين الإماراتي برقم العضوية
      <a href="https://static.pbcdn.ae/pbuae/images/Policybazaar-Middle-East-Insurance-Brokers-LLC.pdf" target="_blank" rel="noopener"><bdi>B81</bdi></a>.
    </p>
    <p>
      المعلومات والمحتوى الواردان في هذه الصفحة مخصصان لأغراض المعلومات والتوعية العامة فقط، ولا يشكلان نصيحة مالية أو طبية مخصصة.
      قد تختلف شروط التغطية التأمينية والأقساط ومعايير الأهلية وفقاً لشركة التأمين والظروف الفردية لكل عميل.
    </p>
    <p>ننصح بالتحدث إلى أحد مستشارينا المرخصين قبل شراء أي منتج للتأمين الصحي.</p>
    <p class="disclaimer__tc">*تسري الشروط والأحكام.</p>
  </div>
</details>
```

---

Travel equivalent: `docs/disclaimer-travel-2026-07-31.md`
