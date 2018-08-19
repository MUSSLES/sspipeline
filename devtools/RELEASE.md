# Release Checklist

### PyPI Source:
```
python3 setup.py sdist
twine upload --repository-url https://test.pypi.org/legacy/ sdist/
```