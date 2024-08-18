# VS CODE

## Get current Extensions

```bash
code --list-extensions > extensions.txt
```

## Import Extensions

```bash
cat extensions.txt | xargs -L 1 code --install-extension
```
