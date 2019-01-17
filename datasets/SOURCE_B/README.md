# SOURCE_B

**Loading data from this source is a stretch goal (optional).** Please do not attempt to write an ETL script / program for this until you have completed one for `SOURCE_A`.

- `SOURCE_B` is a relative small sample of online signatures
- Assume these signatures are in an image format
- For the purpose of this exercise, the signature files are intentionally blank (no parsing needed)
- There is an `INDEX` file keeping track of relationships between signatures (requires parsing)


## File Naming / Directory Convention

**Format:**

- The first line of `INDEX` is the number of signatures in the dataset
- After the first line, each line represents a signature ID, and its parent signature ID (separated by 4 spaces)
- If a signature has a parent signature ID, it is a forged signature
- The signatures are clustered into directories by the first character of the ID
- The first 8 characters of a signature ID are used for the file name

**Examples:**

Give an `INDEX` of:

```
2
04235c8e-7038-43fc-a9c6-229320c36557    8bbaea6a-b51f-4fce-8b5f-a05cdf0eebea
8bbaea6a-b51f-4fce-8b5f-a05cdf0eebea    
```

There should be two directories:

```
./0
./8
```

Within `./0`, we should find a file named `04235c8e`. And within `./8` we should find `8bbaea6a`.

`04235c8e-7038-43fc-a9c6-229320c36557` is a forgery of `8bbaea6a-b51f-4fce-8b5f-a05cdf0eebea`.
