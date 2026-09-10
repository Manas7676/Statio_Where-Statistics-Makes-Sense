# Descriptive Statistics

Descriptive statistics are methods used to summarize, describe, and
understand the main characteristics of a dataset.

Statio provides simple statistical functions with a focus on
readability, correctness, clear input handling, and useful results.

---

## Available Statistics

Statio's descriptive statistics module is planned to include:

| Statistic | Status |
|-----------|--------|
| Mean | ✅ Implemented |
| Median | ✅ Implemented |
| Mode | ✅ Implemented |
| Variance | 🚧 Planned |
| Standard Deviation | 🚧 Planned |
| Range | 🚧 Planned |
| Quartiles | 🚧 Planned |
| Percentile | 🚧 Planned |
| Interquartile Range (IQR) | 🚧 Planned |
| Z-Score | 🚧 Planned |

---

# Mean

The **mean** is the arithmetic average of a dataset.

It is calculated by adding all values and dividing the result by the
number of observations.

### Formula

\[
\bar{x} = \frac{\sum_{i=1}^{n}x_i}{n}
\]

Where:

- \(x_i\) = each observation
- \(n\) = number of observations
- \(\bar{x}\) = arithmetic mean

### Example

```python
from statio.descriptive.mean import mean

data = [10, 20, 30, 40]

result = mean(data)

print(result)
# 25.0