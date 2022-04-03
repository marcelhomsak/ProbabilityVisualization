# ProbabilityVisualization
## Calculating probability and displaying it's distribution





Display probability for a given X on mouse hover:

![image](https://user-images.githubusercontent.com/38257325/161432496-a5de94e1-1ec3-4267-b922-e9c92247fe8a.png)

Display expected value:

![image](https://user-images.githubusercontent.com/38257325/161432520-4b662cd1-e0e5-45d9-8670-19e97e371c40.png)

### Required libraries to install:
- matplotlab (https://pypi.org/project/matplotlib/)
- mplcursors (https://pypi.org/project/mplcursors/)
##### Installing with pip:
- ```pip install matplotlib```
- ```pip install mplcursors```
##### Installing with conda:
- ```conda install -c conda-forge matplotlib```
- ```conda install -c conda-forge mplcursors```

### Running in console:

```python file scheme [expected_value]```

schemes:
- sbinom(n, p)
- sgeom(p, to=50)
- snbinom(n, p, to=50)
- shyper(r, b, n)
- spois(lam, to=50)

expected_values:
- ebinom(n, p)
- egeom(p)
- enbinom(n, p)
- ehyper(r, b, n)
- epois(lam)
