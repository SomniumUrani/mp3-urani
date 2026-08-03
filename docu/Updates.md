---

---
---
## SOURCE-A

| Info           | Value               |
| -------------- | ------------------- |
| Code           | SOURCE-A            |
| Ordinal number | 1                   |
| Changes        | Component selection |
| Status         | Planning            |
**Replacing components because of nonviable pricing.**

| Before               | After                | PCB change | B        | A                      |
| -------------------- | -------------------- | ---------- | -------- | ---------------------- |
| STM6600DA55DM6F      | STM6600CS25DM6F      | None       | C2066705 | C443976                |
| STM32F412CEU6        | STM32F412RET6TR      | Low        | C1337664 | C2053584 (or C2053691) |
| TPS7A4701xRGW        | TPS7A7200RGWR        | Low        | C68214   | C140257                |
| =*                   | TLV1117LV18DCYR      | Low        | =        | C80105                 |
| ? (Capacitor 10uF)   | CL05A106MQ5NUNC      | Low        | ?        | C15525                 |
|                      | BQ24610RGER          | Low        |          | C19384                 |
| 1.2k R (0402 metric) | 1.2k R (0805 metric) | Low        | C25862   | C53463892              |
> \*cheaper replacement for 1.8v rail
### JUSTIFICATIONS
#### Usage of a cheaper LDO (TLV) for 1v8 instead of using a double more expensive MPN (TPS) LDO for 3v3 and 1v8
TPS price table:

| **Qty** | **Unit Price** |
| ------- | -------------- |
| 1+      | $1.3619        |
| 10+     | $1.1473        |
| 30+     | $1.0295        |
| 100+    | $0.8956        |
| 500+    | $0.8359        |
| 1000+   | $0.8084        |

TLV price table:

| **Qty** | **Unit Price** |
| ------- | -------------- |
| 1+      | $0.2347        |
| 50+     | $0.1859        |
| 150+    | $0.1651        |
| 500+    | $0.1391        |
| 2500+   | $0.1275        |
| 5000+   | $0.1206        |

##### Graphical comparison.
![[TPS-TLV.png]]
### XPT2046 evaluation
XPT2046 can be discarted. It is 0.3 USD, 9 dollars by 10 units + 3 dollars.