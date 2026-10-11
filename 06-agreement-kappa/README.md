# Inter-Annotator Agreement (Cohen's Kappa)

When two people label the same responses, a simple "percent agreement" can look high even when they are guessing. Cohen's kappa corrects for that chance agreement.

Rough guide: above 0.8 is strong, 0.6 to 0.8 is substantial, and below 0.4 means your guidelines need work.

**Skills shown:** statistics for evaluation quality, reading agreement data, explaining guideline problems to a team.

## Run the tests

```
python3 -m unittest -v
```

## Example

```python
from kappa import cohens_kappa

rater_1 = ["safe", "unsafe", "safe", "safe"]
rater_2 = ["safe", "safe", "safe", "unsafe"]
print(round(cohens_kappa(rater_1, rater_2), 3))
```
