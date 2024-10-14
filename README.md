# LibraryofBabel.info Python API
An unofficial Python API for Searching and Browsing libraryofbabel.info

### Usage:
Place the script inside your Project and use `import babble_api` to import its functions.

```python
babble_api.browse(hex,wall,shelf,volume,page) #Returns text contained from a specific location
babble_api.search(field,method) #Searches for location containing exact text- returns it as list
```
