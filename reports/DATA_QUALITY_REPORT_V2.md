# Bolivia Deforestation — Data Quality Report V2

## 1. Project Scope

- Source: Global Nature Watch
- Geographic scope: Bolivia, Subnational 2
- Integrated period: 2001–2025
- Primary forest data: 2002–2025
- Integrated canopy threshold: 30%
- Original datasets: 5
- Integrated observations: 2,800
- Integrated columns: 23

## 2. Structural Validation

- Passed checks: 10/10
- Duplicate composite keys: 0
- Original source records preserved: Yes

| Validation                               | Passed   |
|:-----------------------------------------|:---------|
| Row count preserved                      | True     |
| Unique composite keys                    | True     |
| Valid threshold                          | True     |
| Valid year range                         | True     |
| Tree loss available                      | True     |
| No primary loss values in 2001           | True     |
| carbon availability consistency          | True     |
| primary_loss availability consistency    | True     |
| drivers availability consistency         | True     |
| primary_drivers availability consistency | True     |

## 3. Source Coverage

| Source          |   Matched |   Unmatched |   Coverage (%) |
|:----------------|----------:|------------:|---------------:|
| carbon          |      2800 |           0 |         100    |
| primary_loss    |      1296 |        1504 |          46.29 |
| drivers         |      1636 |        1164 |          58.43 |
| primary_drivers |      1272 |        1528 |          45.43 |

Missing source observations are preserved as null values.

## 4. Statistical Outlier Detection

Method: Interquartile Range (IQR), multiplier 1.5.

| Dataset         |   Observations |   Outliers |   Outliers (%) |
|:----------------|---------------:|-----------:|---------------:|
| carbon          |           2800 |        476 |          17    |
| tree_cover      |           2800 |        473 |          16.89 |
| drivers         |           8351 |       1298 |          15.54 |
| primary_drivers |           6506 |        944 |          14.51 |
| primary_loss    |           1296 |        165 |          12.73 |

Outliers were flagged but not automatically removed.

## 5. Cross-Dataset Reconciliation

- Matched observations: 1,636
- Tree Cover total: 10,543,870 ha
- Drivers total: 10,519,423 ha
- Net relative difference: -0.23%
- Absolute reconciliation gap: 0.23%

Differences do not automatically indicate source errors.

## 6. Processing Decisions

| Issue | Decision |
|---|---|
| Missing primary forest data in 2001 | Preserve null |
| Unmatched source observations | Preserve null |
| IQR statistical outliers | Retain and document |
| Tree Cover vs Drivers discrepancies | Preserve original values |
| Canopy threshold differences | Integrate using threshold 30 |
| Driver categories | Preserve in original detailed datasets |

## 7. Limitations

- Statistical outliers are not confirmed data errors.
- Structural validation does not establish measurement accuracy.
- Coverage differs between original sources.
- The integrated dataset is restricted to threshold 30.
- Driver classifications and scientific measurements are not independently verified.
- Reconciliation results describe matched observations only.

## 8. Conclusion

The project demonstrates data profiling, integrity validation,
multi-source integration, statistical anomaly detection,
reconciliation and reproducible analytical processing.

No unsupported numerical corrections were applied.

## 9. Primary Forest Reconciliation

- Matched observations: 1,272
- Only Primary Loss: 24
- Exact numerical matches: 157
- Numerical discrepancies: 1,115
- Net relative gap: -0.1796%
- Absolute reconciliation gap: 0.1802%

### Processing Decision

Original values were preserved. Numerical discrepancies
are documented and require methodological investigation.

No automatic corrections or outlier removal were applied.
