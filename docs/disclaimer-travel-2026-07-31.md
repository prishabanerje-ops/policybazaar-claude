# Travel Insurance — Inline Trust Signal & Accordion Disclaimer

**Vertical:** Travel Insurance
**Prepared:** 2026-07-31

Mirrors the approved health components in structure and tone. Two differences: the DHA permit is excluded, since Dubai Health Authority does not regulate travel insurance, and "medical advice" becomes "insurance advice" with a visa clause added.

## Links used

| Credential | Number | Links to |
|---|---|---|
| Central Bank of the UAE registration | 123 | `https://cdn.policybazaar.ae/pbuae/images/IA-License-Renewal-2026.pdf` |
| Emirates Insurance Federation membership | B81 | `https://static.pbcdn.ae/pbuae/images/Policybazaar-Middle-East-Insurance-Brokers-LLC.pdf` |

Both verified against the source documents on 2026-07-31. The DHA permit BRK-00041 must not appear on any travel page.

---

## 1. Inline Trust Signal

### English

> Licensed by the Central Bank of the UAE (Registration No. 123) · Emirates Insurance Federation Membership No. B81
> Information on this page is for general guidance only — not personalised financial or insurance advice. Speak to one of our advisors →

```html
<div class="trust-signal" lang="en">
  <p class="trust-signal__credentials">
    Licensed by the Central Bank of the UAE
    (<a href="https://cdn.policybazaar.ae/pbuae/images/IA-License-Renewal-2026.pdf" target="_blank" rel="noopener">Registration No. 123</a>)
    ·
    Emirates Insurance Federation Membership No.
    <a href="https://static.pbcdn.ae/pbuae/images/Policybazaar-Middle-East-Insurance-Brokers-LLC.pdf" target="_blank" rel="noopener">B81</a>
  </p>
  <p class="trust-signal__advice">
    Information on this page is for general guidance only — not personalised financial or insurance advice.
    <a href="/contact-us/">Speak to one of our advisors →</a>
  </p>
</div>
```

### Arabic

> مرخصة من قِبل مصرف الإمارات العربية المتحدة المركزي (رقم التسجيل: 123) · عضوية اتحاد التأمين الإماراتي رقم B81
> المعلومات الواردة في هذه الصفحة للتوجيه العام فقط — وليست نصيحة مالية أو تأمينية مخصصة. تحدّث إلى أحد مستشارينا ←

```html
<div class="trust-signal" lang="ar" dir="rtl">
  <p class="trust-signal__credentials">
    مرخصة من قِبل مصرف الإمارات العربية المتحدة المركزي
    (<a href="https://cdn.policybazaar.ae/pbuae/images/IA-License-Renewal-2026.pdf" target="_blank" rel="noopener">رقم التسجيل: <bdi>123</bdi></a>)
    ·
    عضوية اتحاد التأمين الإماراتي رقم
    <a href="https://static.pbcdn.ae/pbuae/images/Policybazaar-Middle-East-Insurance-Brokers-LLC.pdf" target="_blank" rel="noopener"><bdi>B81</bdi></a>
  </p>
  <p class="trust-signal__advice">
    المعلومات الواردة في هذه الصفحة للتوجيه العام فقط — وليست نصيحة مالية أو تأمينية مخصصة.
    <a href="/ar-ae/contact-us/">تحدّث إلى أحد مستشارينا ←</a>
  </p>
</div>
```

`<bdi>` keeps the Latin-script numbers from being reversed inside right-to-left text.

---

## 2. Accordion Disclaimer

### English

> **Disclaimer**
> This page is published by Policybazaar Middle East Insurance Brokers LLC, licensed and regulated by the Central Bank of the UAE (Registration No. 123). Member of Emirates Insurance Federation, Membership No. B81.
> Content on this page is for general informational purposes only and does not constitute personalised financial, insurance or travel advice. Coverage terms, premiums, exclusions and eligibility vary by insurer, destination, trip duration, traveller age and pre-existing medical conditions. Where a policy is bought to support a visa application, cover must meet the minimum requirements set by the destination's embassy or consulate. We strongly recommend speaking with one of our licensed advisors before purchasing any travel insurance policy.
> *T&C Apply.

```html
<details class="disclaimer" lang="en">
  <summary>Disclaimer</summary>
  <div class="disclaimer__body">
    <p>
      This page is published by Policybazaar Middle East Insurance Brokers LLC, licensed and regulated by the Central Bank of the UAE
      (<a href="https://cdn.policybazaar.ae/pbuae/images/IA-License-Renewal-2026.pdf" target="_blank" rel="noopener">Registration No. 123</a>).
      Member of Emirates Insurance Federation, Membership No.
      <a href="https://static.pbcdn.ae/pbuae/images/Policybazaar-Middle-East-Insurance-Brokers-LLC.pdf" target="_blank" rel="noopener">B81</a>.
    </p>
    <p>
      Content on this page is for general informational purposes only and does not constitute personalised financial, insurance or travel advice.
      Coverage terms, premiums, exclusions and eligibility vary by insurer, destination, trip duration, traveller age and pre-existing medical conditions.
      Where a policy is bought to support a visa application, cover must meet the minimum requirements set by the destination's embassy or consulate.
      We strongly recommend speaking with one of our licensed advisors before purchasing any travel insurance policy.
    </p>
    <p class="disclaimer__tc">*T&amp;C Apply.</p>
  </div>
</details>
```

### Arabic

> إخلاء المسؤولية
>
> هذه الصفحة منشورة من قبل شركة بوليسي بازار الشرق الأوسط لوساطة التأمين ذ.م.م، المرخصة والخاضعة لرقابة مصرف الإمارات العربية المتحدة المركزي (رقم التسجيل: 123)، وعضو اتحاد التأمين الإماراتي برقم العضوية B81.
>
> المعلومات والمحتوى الواردان في هذه الصفحة مخصصان لأغراض المعلومات والتوعية العامة فقط، ولا يشكلان نصيحة مالية أو تأمينية أو متعلقة بالسفر مخصصة. قد تختلف شروط التغطية التأمينية والأقساط والاستثناءات ومعايير الأهلية وفقاً لشركة التأمين وجهة السفر ومدة الرحلة وعمر المسافر وحالته الصحية السابقة.
>
> وفي حال شراء البوليصة لأغراض التقدّم بطلب تأشيرة، يجب أن تستوفي التغطية الحدّ الأدنى من الشروط التي تحدّدها سفارة أو قنصلية بلد السفر.
>
> ننصح بالتحدث إلى أحد مستشارينا المرخصين قبل شراء أي بوليصة تأمين سفر.
>
> *تسري الشروط والأحكام.

```html
<details class="disclaimer" lang="ar" dir="rtl">
  <summary>إخلاء المسؤولية</summary>
  <div class="disclaimer__body">
    <p>
      هذه الصفحة منشورة من قبل شركة بوليسي بازار الشرق الأوسط لوساطة التأمين ذ.م.م، المرخصة والخاضعة لرقابة مصرف الإمارات العربية المتحدة المركزي
      (<a href="https://cdn.policybazaar.ae/pbuae/images/IA-License-Renewal-2026.pdf" target="_blank" rel="noopener">رقم التسجيل: <bdi>123</bdi></a>)،
      وعضو اتحاد التأمين الإماراتي برقم العضوية
      <a href="https://static.pbcdn.ae/pbuae/images/Policybazaar-Middle-East-Insurance-Brokers-LLC.pdf" target="_blank" rel="noopener"><bdi>B81</bdi></a>.
    </p>
    <p>
      المعلومات والمحتوى الواردان في هذه الصفحة مخصصان لأغراض المعلومات والتوعية العامة فقط، ولا يشكلان نصيحة مالية أو تأمينية أو متعلقة بالسفر مخصصة.
      قد تختلف شروط التغطية التأمينية والأقساط والاستثناءات ومعايير الأهلية وفقاً لشركة التأمين وجهة السفر ومدة الرحلة وعمر المسافر وحالته الصحية السابقة.
    </p>
    <p>وفي حال شراء البوليصة لأغراض التقدّم بطلب تأشيرة، يجب أن تستوفي التغطية الحدّ الأدنى من الشروط التي تحدّدها سفارة أو قنصلية بلد السفر.</p>
    <p>ننصح بالتحدث إلى أحد مستشارينا المرخصين قبل شراء أي بوليصة تأمين سفر.</p>
    <p class="disclaimer__tc">*تسري الشروط والأحكام.</p>
  </div>
</details>
```

---

Health equivalent: `docs/disclaimer-health-2026-07-31.md`
