# .github/SECURITY.advisories.yml
# GitHub Security Advisories — примеры для Python и Node.js

advisories:
  - id: PYSEC-2025-0001
    title: Insecure Deserialization in harmony-fdl (Python)
    published: false
    withdrawn: false
    severity: high
    identifiers:
      - type: GHSA
        value: GHSA-xxxx-yyyy-zzzz
      - type: CVE
        value: CVE-2025-12345
    affected:
      package:
        ecosystem: pypi
        name: harmony-fdl
      ranges:
        - type: ECOSYSTEM
          events:
            - introduced: 1.0.0
            - fixed: 1.2.4
    references:
      - type: ADVISORY
        url: https://github.com/NOVEYA-UA/Harmony-Development-FDL/security/advisories
    details: |
      Уязвимость небезопасной десериализации в модуле harmony-fdl.
      Злоумышленник может передать специально созданные данные,
      что приведёт к удалённому выполнению кода (RCE).
      Рекомендуется обновиться до версии >= 1.2.4.
    credits:
      - name: "Иван Иванов"
        contact: "ivan.security@example.com"

  - id: JSSEC-2025-0002
    title: XSS Vulnerability in harmony-ui (Node.js)
    published: false
    withdrawn: false
    severity: moderate
    identifiers:
      - type: GHSA
        value: GHSA-abcd-efgh-ijkl
    affected:
      package:
        ecosystem: npm
        name: harmony-ui
      ranges:
        - type: ECOSYSTEM
          events:
            - introduced: 2.0.0
            - fixed: 2.1.1
    references:
      - type: ADVISORY
        url: https://github.com/NOVEYA-UA/Harmony-Development-FDL/security/advisories
    details: |
      Уязвимость XSS при рендеринге пользовательского ввода в компоненте harmony-ui.
      Может привести к внедрению произвольного JavaScript-кода при использовании
      небезопасных данных без экранирования. Исправлено в версии >= 2.1.1.
    credits:
      - name: "Security Lab"
        contact: "security-lab@example.com"
