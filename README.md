# LibraryofBabel.info Python API
An unofficial Python API for Searching and Browsing libraryofbabel.info

### Usage:
Place the script inside your Project and use `import babble_api` to import its functions.

```python
babble_api.browse(hex,wall,shelf,volume,page) #Returns text contained from a specific location
babble_api.search(field,method) #Searches for location containing exact text- returns it as list
```


### Additional Background and Information:
This API was made in an attempt to understand how the Library of Babel website works. The text locations generated are often shorter than the 3200 characters it can potentially contain, so I wanted to explore its use as a form of compression.
This Project is still under development and is more educational than utilitary. Special credits to Victor Cortez's Library of Babel Python API (https://github.com/victor-cortez/Library-of-Babel-Python-API) which was used as a reference to learn Beautiful Soup.
