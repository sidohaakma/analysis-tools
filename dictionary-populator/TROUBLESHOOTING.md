# TROUBLESHOOTING

## Trouble when installing the dictionary-populator
When you try to install the **dictipnary-populator**.

```bash
pip install dictionary-populator
```

When this error occurs:

```bash
Permission denied /Library/Frameworks/Python/versions/2.7
```

This could solve the problem.

```bash
pip install --extra-index-url https://registry.molgenis.org/repository/pypi dictionary-populator --user
```